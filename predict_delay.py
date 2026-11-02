import joblib
import numpy as np
import pandas as pd

from src.shipment_prep import clean_shipments, build_features

raw_new = pd.read_csv("data/new_shipments.csv")
hubs = pd.read_csv("data/hubs.csv")

model = joblib.load("models/delay_model.pkl")
threshold = float(pd.read_csv("models/delay_threshold.csv").iloc[0]["threshold"])
feature_order = pd.read_csv("models/feature_order.csv")["feature"].tolist()
medians_df = pd.read_csv("models/impute_values.csv")
medians = dict(zip(medians_df["column"], medians_df["median"]))

segments = pd.read_csv("outputs/hub_segments.csv")[
    ["hub_id", "segment"]
]

clean_new, _ = clean_shipments(raw_new, medians=medians)
features = build_features(clean_new, hubs)

# Keep the feature order exactly the same as training
X_new = features[feature_order]
probabilities = model.predict_proba(X_new)[:, 1]

actions = pd.DataFrame({
    "shipment_id": features["shipment_id"],
    "hub_id": features["hub_id"],
    "delay_probability": np.round(probabilities, 4),
    "flagged": (probabilities >= threshold).astype(int)
})

actions = actions.merge(
    segments, on="hub_id", how="left", validate="many_to_one"
)

def choose_action(row):
    if row["flagged"] == 0:
        return "No action"
    if row["segment"] == "Escalate":
        return "Escalate to hub manager"
    return "Proactive customer call"

actions["action"] = actions.apply(choose_action, axis=1)

actions = actions[
    ["shipment_id", "hub_id", "segment",
     "delay_probability", "flagged", "action"]
]

actions.to_csv("outputs/new_shipment_actions.csv", index=False)

print("Prediction completed.")
print("New shipments:", len(actions))
print("Flagged shipments:", int(actions["flagged"].sum()))
print(
    "Hub-manager escalations:",
    int(((actions["flagged"] == 1) &
         (actions["action"] == "Escalate to hub manager")).sum())
)
print(actions.head(10))

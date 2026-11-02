# Shipment Delay Intelligence Project


## Data findings

- **Service delays:** Express has the highest delay rate at 0.4897 (119 delayed out of 243 shipments).
- **Hub tiers:** Tier 1 has a delay rate of 0.0400, compared with 0.4400 for Tier 3.
- **Distance:** Delay rates across distance bands are: 0-200 = 0.0219, 201-400 = 0.1368, 401-600 = 0.4364, 601+ = 0.8523.
- **Delivery-hour correlations:** The three strongest absolute correlations with delivery_hours are promised_hours (+0.8372), distance_km (+0.4013), n_stops (+0.3247).
- **Log transformation:** The filled declared-value column has mean INR 1533.05 and median INR 1121.50; after the natural-log transformation, the mean is 7.0277 and median is 7.0224. The transformation reduces the influence of large values and makes the distribution easier to model.



## Model results (regression)

- The mean baseline has validation R² = -0.0212; it is a simple reference model that ignores shipment-specific features.
- The lowest validation RMSE belongs to **linear_regression**, at 4.8912 hours.
- Tree-depth results are in `outputs/part_b_tree_depth.csv`. Shallow trees can underfit; deep trees can overfit when the validation RMSE is much higher than training RMSE.
- The best tested learning rate by validation R² is 0.1, with R² = 0.9306. A very low learning rate may learn too slowly, while a high rate may overshoot.
- Cross-validation results are in `outputs/part_b_cv.csv`. Compare them with the validation ranking before deciding which model to deploy.



## Model results (classification)

- The blind all-on-time baseline has validation accuracy 0.7667, but recall is zero because it fails to identify delayed parcels.
- The five bookkeeping/noise columns together contribute 0.2245 of the full forest's feature importance.
- The top seven F-score features are: distance_km, hub_tier, hub_daily_capacity, n_stops, promised_hours, rain_flag, sale_event_flag. The `part_c_selectk.csv` file shows how validation F1 changes with the number of selected features.
- The best tuning row by validation F1 is `default_forest_same_7_features` (F1 = 0.8333). Because validation contains only 180 rows, small score differences may not generalize.
- The selected alert threshold is 0.5. It is chosen by the rule requiring validation recall of at least 0.80 where possible.
- Test precision = 0.6889, recall = 0.7561, and F1 = 0.7209. The test set contains only 41 delayed parcels, so its recall estimate is uncertain.



## Operations recommendation

- The Escalate segment contains 9 hubs, with average hub-level delay rate 0.4600.
- Tier/segment mismatches are listed in `outputs/tier_vs_segment_mismatch.csv`. Use the observed segment alongside the official tier instead of assuming the tier label always describes current operating performance.
- The alert threshold is 0.5. Test precision of 0.6889 means approximately 6.9 of every 10 flagged parcels are delayed; test recall of 0.7561 means approximately 7.6 of every 10 delayed parcels are caught.
- Of the 48 new parcels, 8 were flagged and 6 require a hub-manager escalation.
- K = 3 is retained because operations needs three playbooks. Although the separation ratio can rise for K = 4 and K = 5, those solutions include clusters with fewer than six hubs, making them less practical as separate operating groups. See `outputs/part_d_separation.csv`.



## Production plan

- **Accuracy:** Track regression errors and classification precision, recall, and F1 in the output CSVs.
- **Reliability:** Keep the saved-model reload check in `outputs/part_d_reload_check.csv`.
- **Reproducibility:** Keep fixed random seeds, pinned package versions, and the provided data generator unchanged.
- **Maintainability:** Keep shared cleaning and feature engineering in `src/shipment_prep.py`.
- **Consistency:** Use the same shared preprocessing in training and prediction.
- **Monitorability:** Save shipment probabilities, flags, actions, and model evaluation metrics.

Suggested monitoring triggers:
1. Investigate if the weekly delayed share changes by more than 5 percentage points compared with a comparable period.
2. Review operations if the weekly flagged share changes by more than 5 percentage points.
3. Investigate if measured recall on parcels with known outcomes falls below 0.80 for two consecutive weekly reviews.

Retrain quarterly, or earlier if performance or data quality triggers are breached. Compare the 15–28 September sale window with similar sale periods rather than ordinary weeks. Data drift may appear as changing distance, service mix, hub-tier profiles, dispatch hours, or feature distributions.



## Limitations

- The dataset is synthetic and may not reflect real logistics operations.
- The test set contains only 41 delayed parcels, so precision and recall can vary with a small number of predictions.
- The alert threshold is selected from one validation split and may not remain optimal over time.
- K-Means assigns each hub to a segment based on the selected profile features; it does not prove that a particular operational intervention will improve outcomes.



## How to run

From the repository root, run these commands in order:

```bash
pip install -r requirements.txt
python generate_data.py
python part_a_clean_eda.py
python part_b_regression.py
python part_c_classification.py
python part_d_segments.py
python package_model.py
python predict_delay.py

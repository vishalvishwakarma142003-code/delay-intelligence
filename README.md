# 🚚 Delay Intelligence — Shipment Delay Prediction

## 📌 Project Overview
Delay Intelligence is a Machine Learning project designed to analyze shipment data, predict delivery delays, and support data-driven logistics decisions.

The project uses historical shipment information to build predictive models and applies them to new shipments to generate useful insights and actions.

## 🎯 Project Objectives
- Clean and preprocess shipment data.
- Perform Exploratory Data Analysis (EDA).
- Predict delivery time using Regression.
- Classify shipments based on delay risk.
- Segment shipments to identify operational patterns.
- Package the trained model for reuse.
- Generate predictions for new shipments.

## 🛠️ Technologies Used
- Python
- NumPy
- Pandas
- Matplotlib / Seaborn
- Scikit-learn
- Machine Learning
- Google Colab
- GitHub

## 📂 Repository Structure

```text
delay-intelligence/
│
├── README.md
├── requirements.txt
├── generate_data.py
│
├── data/
│   ├── hubs.csv
│   ├── raw_shipments.csv
│   ├── new_shipments.csv
│   └── modelling_table.csv
│
├── src/
│   └── shipment_prep.py
│
├── part_a_clean_eda.py
├── part_b_regression.py
├── part_c_classification.py
├── part_d_segments.py
│
├── package_model.py
├── predict_delay.py
│
├── models/
│   ├── delay_model.pkl
│   ├── delay_threshold.csv
│   ├── feature_order.csv
│   └── impute_values.csv
│
└── outputs/
    └── Project output CSV files
```

## 📊 Project Workflow

### Part A — Data Cleaning & Exploratory Data Analysis
- Data quality checks
- Missing value treatment
- Data preprocessing
- Exploratory Data Analysis
- Modelling table preparation

### Part B — Regression
- Train a regression model to predict shipment delivery time.
- Evaluate model performance using appropriate regression metrics.

### Part C — Classification
- Build a classification model to identify shipment delay risk.
- Evaluate classification performance.

### Part D — Shipment Segmentation
- Apply clustering techniques to identify shipment patterns and groups.

### Model Packaging & Prediction
- Save the trained model and supporting files.
- Generate predictions and actions for new shipments.

## 📁 Dataset Information
The project uses generated shipment data containing historical shipments, hub information, and new shipments for prediction.

| Dataset | Records |
|---|---:|
| Historical modelling data | 1,200 |
| New shipments | 48 |
| Hubs | 24 |

## 🚀 How to Run the Project

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Generate the dataset

```bash
python generate_data.py
```

### 3. Run the project scripts in order

```bash
python part_a_clean_eda.py
python part_b_regression.py
python part_c_classification.py
python part_d_segments.py
python package_model.py
python predict_delay.py
```

## 📈 Results & Outputs
The project generates data analysis results, model evaluation outputs, shipment delay predictions, and actionable information for new shipments.

Refer to the `outputs/` directory for generated CSV files and the `models/` directory for saved model artifacts.

## 👨‍💻 Author
**Vishal Vishwakarma**

AI/ML Student | Aspiring Data Analyst & Data Scientist

## ⭐ Project Purpose
This project was developed as a Machine Learning capstone to demonstrate skills in data preprocessing, exploratory analysis, predictive modelling, clustering, and model deployment preparation.

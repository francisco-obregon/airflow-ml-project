# 🚀 ML Pipeline with Airflow

## 📌 Overview
This project implements an end-to-end machine learning pipeline using Apache Airflow.

The pipeline automates:
- Model training
- Feature persistence
- Batch predictions over large datasets

## 🧠 Architecture

Airflow DAG structure:

train_model >> predict_model

- **train_model**: trains the ML model and saves artifacts
- **predict_model**: loads the model and generates predictions

## ⚙️ Tech Stack
- Python
- Apache Airflow
- Pandas
- Scikit-learn
- Joblib

## 📂 Project Structure

```
proyecto_portfolio/
│
├── airflow/
│   └── dags/
│       └── ml_pipeline.py
│
├── ml/
│   ├── train_model.py
│   ├── predict.py
│   ├── model.pkl
│   ├── features.pkl
│
├── data/
│   ├── raw/
│   │   └── import_data.csv
│   └── processed/
│       └── predictions.csv
│
├── README.md
├── requirements.txt
```

## 📊 Results

- R² Score: **0.9984**
- MAE: **120.62**
- Total predictions: **37,191 rows**
- No missing data during prediction

Example output:

```
[INFO] Filas usadas: 37191
[INFO] Predicciones guardadas en: data/processed/predictions.csv
[INFO] Primeras 5: [2508.73, 2415.59, 1756.45, 4098.79, 1805.56]
```

## ▶️ How to Run

### 1. Set environment variable

```bash
export BASE_PATH=/ruta/a/proyecto_portfolio
```

### 2. Start Airflow

```bash
airflow standalone
```

### 3. Trigger DAG

- Open Airflow UI
- Run: `ml_training_prediction_pipeline`

## 🎯 Key Features

- Automated ML workflow orchestration
- Reproducible pipeline
- Feature consistency between training and prediction
- Scalable batch processing

## 💼 Business Value

This pipeline simulates a real-world scenario where:
- Models are retrained automatically
- Predictions are generated on new incoming data
- Results are stored for downstream analysis

## 👨‍💻 Author

Francisco Obregon (Data Scientist / ML Pipeline Developer)
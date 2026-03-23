import os
os.environ["OBJC_DISABLE_INITIALIZE_FORK_SAFETY"] = "YES"

import joblib
import pandas as pd

BASE_PATH = os.getenv("BASE_PATH")

# cargar modelo
model = joblib.load(f"{BASE_PATH}/ml/model.pkl")

# cargar features
features = joblib.load(f"{BASE_PATH}/ml/features.pkl")

# cargar datos
DATA_PATH = f"{BASE_PATH}/data/raw/import_data.csv"
df = pd.read_csv(DATA_PATH, encoding="latin1", sep=";")

# limpiar columnas
df.columns = df.columns.str.strip()

# validar columnas
missing_cols = [col for col in features if col not in df.columns]
if missing_cols:
    raise ValueError(f"Faltan columnas en el dataset: {missing_cols}")

# usar mismas features
X = df[features].dropna()

print(f"[INFO] Filas usadas: {len(X)}")
print(f"[INFO] Filas descartadas: {len(df) - len(X)}")

# predicciones
preds = model.predict(X)

# guardar en nueva columna
df.loc[X.index, "prediction"] = preds

# guardar output
OUTPUT_PATH = f"{BASE_PATH}/data/processed/predictions.csv"
os.makedirs(f"{BASE_PATH}/data/processed", exist_ok=True)

df.to_csv(OUTPUT_PATH, index=False)

# logs
print(f"[INFO] Predicciones guardadas en: {OUTPUT_PATH}")
print(f"[INFO] Total predicciones: {len(preds)}")
print(f"[INFO] Primeras 5: {preds[:5]}")
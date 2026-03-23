import os
os.environ["OBJC_DISABLE_INITIALIZE_FORK_SAFETY"] = "YES"

import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.ensemble import RandomForestRegressor

# BASE PATH
BASE_PATH = os.getenv("BASE_PATH")

# asegurar carpeta ml
os.makedirs(f"{BASE_PATH}/ml", exist_ok=True)

# cargar datos
DATA_PATH = f"{BASE_PATH}/data/raw/import_data.csv"
df = pd.read_csv(DATA_PATH, encoding="latin1", sep=";")

# limpiar columnas
df.columns = df.columns.str.strip()

# seleccionar solo numéricas
df_numeric = df.select_dtypes(include=["int64", "float64"]).dropna()

# separar X e y (ajusta target si quieres)
X = df_numeric.drop(columns=["FOB"], errors="ignore")
y = df_numeric["FOB"]

# split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# modelo
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# evaluación
preds = model.predict(X_test)

mae = mean_absolute_error(y_test, preds)
r2 = r2_score(y_test, preds)

print("MAE:", mae)
print("R2:", r2)

# guardar modelo y features
joblib.dump(model, f"{BASE_PATH}/ml/model.pkl")
joblib.dump(X.columns.tolist(), f"{BASE_PATH}/ml/features.pkl")

print("Modelo y features guardados correctamente")
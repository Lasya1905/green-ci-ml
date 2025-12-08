import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error
import joblib
import sys

try:
    df = pd.read_csv("pipeline_data.csv")
except FileNotFoundError:
    print("pipeline_data.csv not found. Run prepare_dataset.py first.")
    sys.exit(1)

# Choose features and target
X = df[['duration_s', 'co2_g']]
y = df['energy_kWh']

# Basic check
if len(df) < 5:
    print("Warning: small dataset (<5 rows). Model may be unreliable.")

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

preds = model.predict(X_test)
r2 = r2_score(y_test, preds)
mae = mean_absolute_error(y_test, preds)

print(f"R² Score: {r2:.4f}")
print(f"MAE: {mae:.6f} kWh")

joblib.dump(model, "energy_model.pkl")
print("✅ Model saved as energy_model.pkl")

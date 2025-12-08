import joblib
import pandas as pd

model = joblib.load("energy_model.pkl")

# Replace these values with new run specifics
duration = float(input("Enter job duration in seconds: "))
co2 = float(input("Enter CO2 emission in grams: "))

df = pd.DataFrame({"duration_s":[duration], "co2_g":[co2]})
pred = model.predict(df)[0]
print(f"Predicted Energy (kWh): {pred:.6f}")

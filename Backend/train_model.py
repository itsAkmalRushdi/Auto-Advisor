import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
import joblib

# Load dataset
df = pd.read_csv("dataset/clean_cars.csv")

# Encode brand
le = LabelEncoder()
df["brand"] = le.fit_transform(df["brand"])

# Features and target
X = df[["brand", "year"]]
y = df["price"]

# Train test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestRegressor()
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "car_price_model.pkl")
joblib.dump(le, "brand_encoder.pkl")

print("Model trained successfully")
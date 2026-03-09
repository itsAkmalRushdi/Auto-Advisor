from fastapi import FastAPI
import pandas as pd

app = FastAPI()

# Load dataset
data = pd.read_csv("dataset/clean_cars.csv")
data.columns = data.columns.str.strip()

@app.get("/")
def home():
    return {"message": "AutoAdvisor Vehicle Recommendation API"}


# ---------------------------
# DROPDOWN DATA
# ---------------------------

@app.get("/brands")
def get_brands():
    return sorted(data["brand"].dropna().unique().tolist())


@app.get("/models")
def get_models():
    return sorted(data["model"].dropna().unique().tolist())


@app.get("/years")
def get_years():
    return sorted(data["year"].dropna().unique().tolist())


# ---------------------------
# RECOMMEND VEHICLE
# ---------------------------

@app.get("/recommend")
def recommend_vehicle(
    income: int,
    brand: str = None,
    model: str = None,
    year: int = None
):

    df = data.copy()

    max_price = income * 40

    df["price"] = pd.to_numeric(df["price"], errors="coerce")

    df = df[df["price"] <= max_price]

    if brand:
        df = df[df["brand"].str.contains(brand, case=False, na=False)]

    if model:
        df = df[df["model"].str.contains(model, case=False, na=False)]

    if year:
        df = df[df["year"] == year]

    result = df[["brand", "model", "year", "price", "location", "link"]].head(10)

    return {
        "income": income,
        "max_price_lkr": max_price,
        "recommended_vehicles": result.to_dict(orient="records")
    }


# ---------------------------
# VIEW ALL VEHICLES
# ---------------------------

@app.get("/vehicles")
def get_all_vehicles(limit: int = 50):

    df = data.head(limit)

    return df.to_dict(orient="records")


# ---------------------------
# LEASING INFORMATION
# ---------------------------

@app.get("/leasing-info")
def leasing_info():

    return {
        "description": "Vehicle leasing allows customers to purchase a vehicle by paying monthly installments instead of full cash.",
        "typical_downpayment": "20% - 30%",
        "leasing_period": "3 - 7 years",
        "requirements": [
            "NIC copy",
            "Proof of income",
            "Bank statements",
            "Address verification"
        ],
        "major_leasing_companies": [
            "LB Finance",
            "People's Leasing",
            "LOLC Finance",
            "HNB Finance",
            "Singer Finance"
        ]
    }
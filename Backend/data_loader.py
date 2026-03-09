import pandas as pd

def load_cars():

    df = pd.read_csv("data/cardata.csv")

    # convert price from lakhs INR to LKR
    df["price_lkr"] = df["Selling_Price"] * 100000 * 3.6

    # rename columns for easier use
    df = df.rename(columns={
        "Car_Name": "model",
        "Year": "year",
        "Fuel_Type": "fuel",
        "Transmission": "transmission",
        "Kms_Driven": "kms"
    })

    return df
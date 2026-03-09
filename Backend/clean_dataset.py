import pandas as pd
import re

df = pd.read_csv("dataset/ikman_cars.csv")

df = df.dropna(subset=["price"])

df["price"] = df["price"].astype(str)
df["price"] = df["price"].str.replace(",", "", regex=False)
df["price"] = df["price"].str.extract(r"(\d+)")
df["price"] = pd.to_numeric(df["price"], errors="coerce")

# Extract year
df["year"] = df["title"].str.extract(r"(20\d{2}|19\d{2})")

brands = [
    "Toyota","Honda","Suzuki","Nissan","Mitsubishi",
    "Mazda","BMW","Mercedes","Audi","Hyundai","Kia"
]

def extract_brand(title):
    for brand in brands:
        if brand.lower() in str(title).lower():
            return brand
    return "Other"

df["brand"] = df["title"].apply(extract_brand)

# Extract model (word after brand)
def extract_model(title, brand):
    try:
        words = title.split()
        brand_index = words.index(brand)
        return words[brand_index + 1]
    except:
        return "Unknown"

df["model"] = df.apply(lambda x: extract_model(x["title"], x["brand"]), axis=1)

df = df.dropna(subset=["price","year"])

df.to_csv("dataset/clean_cars.csv", index=False)

print("Clean dataset saved:", len(df))
from data_loader import load_cars

cars_df = load_cars()

def retrieve_cars(budget):

    filtered = cars_df[cars_df["price_lkr"] <= budget]

    filtered = filtered.sort_values(by="price_lkr", ascending=False)

    return filtered.head(5).to_dict(orient="records")
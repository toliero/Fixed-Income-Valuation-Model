import pandas as pd

def process_yield_curve(data):
    """
    Processes raw yield curve data, extracting relevant information.
    """
    data["Rate"] = data["Rate"].astype(float)
    data = data.sort_values(by="Date", ascending=True)
    return data

if __name__ == "__main__":
    df = pd.read_csv("../data/raw/treasury_yield_curve.csv")
    processed_df = process_yield_curve(df)
    processed_df.to_csv("../data/processed/processed_yield_curve.csv", index=False)
    print(processed_df.head())

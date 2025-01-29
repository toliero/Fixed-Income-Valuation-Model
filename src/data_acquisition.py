import pandas as pd
import requests

def fetch_treasury_yield_curve():
    """
    Fetches U.S. Treasury yield curve data from the U.S. Treasury API.
    """
    url = "https://api.fiscaldata.treasury.gov/services/api/fiscal_service/v1/accounting/od/avg_interest_rates"
    response = requests.get(url)

    if response.status_code != 200:
        print("Failed to fetch data. Using local CSV instead.")
        return pd.read_csv("../data/raw/treasury_yield_curve.csv")

    data = response.json()["data"]
    df = pd.DataFrame(data)
    df = df[["record_date", "avg_interest_rate_amt"]]
    df.columns = ["Date", "Rate"]
    df["Date"] = pd.to_datetime(df["Date"])
    return df

if __name__ == "__main__":
    df = fetch_treasury_yield_curve()
    print(df.head())
    df.to_csv("../data/raw/treasury_yield_curve.csv", index=False)

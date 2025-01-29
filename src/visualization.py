import matplotlib.pyplot as plt
import seaborn as sns

def plot_yield_curve(spot_rates):
    """
    Plots the yield curve.
    """
    plt.figure(figsize=(8,5))
    sns.lineplot(x=spot_rates['Date'], y=spot_rates['Rate'], marker="o", color="b")
    plt.xlabel("Date")
    plt.ylabel("Yield (%)")
    plt.title("Yield Curve")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    import pandas as pd
    df = pd.read_csv("../data/processed/processed_yield_curve.csv")
    plot_yield_curve(df)

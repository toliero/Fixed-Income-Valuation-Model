import pandas as pd
from src.data_acquisition import fetch_treasury_yield_curve
from src.data_processing import process_yield_curve
from src.valuation import construct_yield_curve, bond_valuation
from src.visualization import plot_yield_curve

def run_interactive():
    print("Fixed Income Valuation Model")
    face_value = float(input("Enter face value of bond ($1000 default): ") or 1000)
    coupon_rate = float(input("Enter coupon rate (0.05 default): ") or 0.05)
    maturity = int(input("Enter bond maturity (10 default): ") or 10)

    raw_data = fetch_treasury_yield_curve()
    processed_data = process_yield_curve(raw_data)
    yield_curve = construct_yield_curve(processed_data)

    price = bond_valuation(face_value, coupon_rate, maturity, yield_curve)
    print(f"\nEstimated Bond Price: ${price:.2f}")

    plot_yield_curve(processed_data)

if __name__ == "__main__":
    run_interactive()


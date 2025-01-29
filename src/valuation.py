import numpy as np
from scipy.interpolate import interp1d

def construct_yield_curve(spot_rates):
    """
    Constructs an interpolated yield curve.
    """
    return interp1d(spot_rates['Date'].astype(int), spot_rates['Rate'], kind='linear', fill_value="extrapolate")

def bond_valuation(face_value, coupon_rate, maturity, yield_curve):
    """
    Computes bond price using present value of future cash flows.
    """
    cash_flows = [coupon_rate * face_value] * (maturity - 1) + [coupon_rate * face_value + face_value]
    discount_factors = [(1 + yield_curve(i) / 100) ** i for i in range(1, maturity + 1)]
    present_values = [cf / df for cf, df in zip(cash_flows, discount_factors)]
    return sum(present_values)

if __name__ == "__main__":
    import pandas as pd
    df = pd.read_csv("../data/processed/processed_yield_curve.csv")
    yield_curve = construct_yield_curve(df)
    price = bond_valuation(1000, 0.05, 10, yield_curve)
    print(f"Bond Price: {price:.2f}")

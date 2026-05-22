import marimo

__generated_with = "0.23.6"
app = marimo.App(width="full", auto_download=["ipynb"])


@app.cell
def _():
    import marimo as mo
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt

    return mo, pd


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Module 3: Cardinality & Categorical Encoding
    ## Core Principle
    ML models = numerical engines → **Must convert text to numbers**

    ## Cardinality = Number of unique values in a categorical column
    **Determines which encoding strategy to use**

    ---

    ## Strategy 1: One-Hot Encoding (OHE)

    - Creates **new binary columns** (0/1) for each unique value
    - ✅ **Use for:** Low cardinality (< 10 unique values)
    - ❌ **Avoid for:** High cardinality (e.g., 1,200 job titles → adds 1,200 columns!)
    - ⚠️ **Risk:** Dimensionality explosion → sparse matrix + overfitting + memory crash
    """)
    return


@app.cell
def _(pd):
    df = pd.read_csv('dataset_step1_cleaned.csv')
    print("--- Day 3 Baseline Data ---")
    print(df[['Age', 'City', 'Annual_Income_USD', 'Coupon_Code']].head(10))

    print("\nMissing values status:\n", df.isna().sum())
    return (df,)


@app.cell
def _(df, pd):
    df_ohe = pd.get_dummies(df, columns=['Coupon_Code'], drop_first=True, dtype=int)

    print('--- One Hot Encoded Structural Layout ---')
    print(df_ohe.head(5))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Strategy 2: Label & Ordinal Encoding

    - Maps each unique text to a single integer
    - **Ordinal Encoding:** Preserves explicit rank order (e.g., Low=0, Medium=1, High=2)
    - ✅ **Use when:** Natural hierarchy exists (education level, size, ranking)
    - ⚠️ **Warning:** Without explicit mapping, models may misinterpret numeric relationships
    """)
    return


@app.cell
def _(df):
    # create an explicit manual hierarchy dictionary
    priority_mapping = {'None_Used': 0, 'SAVE10': 1, 'WELCOME': 2, 'FLASH20': 3}

    # vectorized mapping technique across the series array
    df_ordinal = df # Copy original df
    df_ordinal['Coupon_Rank'] = df_ordinal['Coupon_Code'].map(priority_mapping)

    print("--- Ordinal Hierarchical Transformation ---")
    print(df_ordinal[['Coupon_Code', 'Coupon_Rank']].head(5))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Strategy 3: Frequency / Count Encoding

    - Replaces text with **how often it appears** (count or percentage)
    - ✅ **Gold standard for High Cardinality** (ZIP codes, IP addresses, device IDs)
    - 💡 **Why it works:** Rarity = strong predictive signal (e.g., fraud detection: rare IP ≠ common hub IP)
    - 🎯 **Benefit:** No new columns, compresses wide text into informative density scale
    """)
    return


@app.cell
def _(df):
    df_freq = df

    # Step 1: Calculate baseline frequency percentage
    city_frequencies = df_freq['City'].value_counts(normalize=True) # normalize=True gives normalized percentage value

    # Step 2: Use a vectorized map to inject the percentage
    df_freq['City_Encoded'] = df_freq['City'].map(city_frequencies)

    print("--- High Cardinality Frequency Compression ---")
    print(df_freq[['City', 'City_Encoded']].head(6))


    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Quick Decision Guide

    | Cardinality | Recommended Strategy |
    |-------------|----------------------|
    | Low (<10) | One-Hot Encoding |
    | Ordered hierarchy | Ordinal Encoding |
    | High (100s-1000s) | Frequency Encoding |
    """)
    return


@app.cell
def _(pd):
    # 1. Load your clean state from Day 2
    df_day3_base = pd.read_csv('dataset_step1_cleaned.csv')

    # 2. Deploy your chosen Frequency Encoding blueprint for City
    city_freq = df_day3_base['City'].value_counts(normalize=True)
    df_day3_base['City_Encoded'] = df_day3_base['City'].map(city_freq)

    # 3. Deploy your chosen One-Hot Encoding blueprint for Coupon_Code
    # Fix the ordinal mapping bug we spotted by adding 'None_Used'
    pr_mapping = {'None_Used': 0, 'SAVE10': 1, 'WELCOME': 2, 'FLASH20': 3}
    df_day3_base['Coupon_Rank'] = df_day3_base['Coupon_Code'].map(pr_mapping)

    # 4. Save this unified feature matrix state cleanly for Day 3
    df_day3_base.to_csv('dataset_step2_encoded.csv', index=False)
    print("🎯 Unified baseline encoded dataset saved successfully!")
    return


if __name__ == "__main__":
    app.run()

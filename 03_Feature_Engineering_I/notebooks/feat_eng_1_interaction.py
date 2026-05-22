import marimo

__generated_with = "0.23.6"
app = marimo.App(width="full", auto_download=["ipynb"])


@app.cell
def _():
    import marimo as mo
    import pandas as pd
    import numpy as np

    return mo, pd


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Interaction Features & Continuous Binning

    ## Part 1: Interaction Features (Force Multipliers)

    ### Why Create Interaction Features?

    **The Insight:** Most powerful signals live in **relationships between columns**, not single columns alone

    **Benefits:**
    - Turns complex non-linear problems → clean linear problems
    - Helps tree models (XGBoost/LightGBM) learn faster with less data
    - Makes patterns **explicit** instead of forcing model to discover them

    > ⚡ **Analogy:** Like giving someone a map instead of making them explore blindly
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Three Operational Approaches

    | Operation | Formula | Best For | Example |
    |-----------|---------|----------|---------|
    | **Ratio** (÷) | Col A / Col B | Normalizing, efficiency metrics | Debt / Income = Risk Score |
    | **Product** (×) | Col A × Col B | Combined effects | Lot Frontage × Depth = Total Area |
    | **Difference** (-) | Col A - Col B | Gaps, progress, change | Listed Price - Sold Price = Discount |

    #### Concrete Examples

    ```python
    # Ratio: Debt-to-income for loan risk
    df['debt_to_income'] = df['total_debt'] / df['annual_income']

    # Product: Total lot area for house price
    df['total_lot_area'] = df['lot_frontage'] * df['lot_depth']

    # Difference: Budget variance
    df['budget_variance'] = df['budgeted'] - df['actual']
    ```
    """)
    return


@app.cell
def _(pd):
    df_interact = pd.read_csv('datasets/dataset_step3_scaled.csv')

    # --- DOMAIN-SPECIFIC INTERACTION FEATURE ---
    # We have Annual_Income_USD and Age. Let's engineer an 'Income_Per_Year_Of_Age' ratio.
    # This serves as a proxy for career trajectory or financial velocity.

    df_interact['Income_Velocity'] = df_interact['Annual_Income_USD'] / df_interact['Age']

    print("--- Interaction Feature Matrix Output ---")
    print(df_interact[['Customer_ID', 'Age', 'Annual_Income_USD', 'Income_Velocity']].head(5))
    return (df_interact,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Part 2: Continuous Binning (Quantization)

    ### Why Bin Continuous Data?

    **The Problem:** Small fluctuations = pure noise

    - Is there a real difference between 25.4 and 25.6 years old? **No.**

    **Benefits of Binning:**
    - Strips away meaningless variance
    - Forces model to focus on **stable behavioral groups**
    - Captures **non-linear thresholds** (e.g., 59 = fail, 60 = pass)

    ---

    ### Two Methods: `pd.cut()` vs `pd.qcut()`

    | Aspect | `pd.cut()` | `pd.qcut()` |
    |--------|-----------|-------------|
    | **Logic** | Fixed value ranges | Equal number of rows per bin |
    | **Bin widths** | Set by you (e.g., 0-18, 18-35) | Automatically determined |
    | **Row distribution** | Uneven (can be empty bins) | Equal (each bin has same count) |
    | **Best for** | Regulatory boundaries (age groups, tax brackets) | Skewed data (wealth, transactions) |

    ---

    ### Visual Comparison

    **Data:** 1000 people's incomes (highly skewed)

    #### `pd.cut()` — Range-Based
    ```
    [$0-$50k]     : 700 people  ← crowded
    [$50k-$100k]  : 200 people
    [$100k-$1M]   : 100 people  ← sparse
    ```

    #### `pd.qcut(q=4)` — Quantile-Based (4 bins)
    ```
    Bin 1: 250 people (lowest 25% incomes)
    Bin 2: 250 people
    Bin 3: 250 people
    Bin 4: 250 people (top 25% incomes)
    ```

    ---

    ### Code Examples

    ```python
    import pandas as pd

    # Range-based: Fixed age groups
    df['age_group'] = pd.cut(df['age'],
                              bins=[0, 18, 35, 60, 100],
                              labels=['Child', 'Young', 'Adult', 'Senior'])

    # Quantile-based: Equal customer tiers
    df['spending_tier'] = pd.qcut(df['transaction_amount'],
                                   q=4,  # 4 equal groups
                                   labels=['Low', 'Medium', 'High', 'Very High'])
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Quick Decision Guide

    | Scenario | Best Approach |
    |----------|--------------|
    | Relationship between columns matters | Create **interaction feature** |
    | Efficiency metric needed (debt/income) | **Ratio** |
    | Two dimensions combine to one (area) | **Product** |
    | Capture change over time | **Difference** |
    | Data has meaningless small fluctuations | **Bin it** |
    | Need fixed real-world boundaries | `pd.cut()` |
    | Skewed data, want balanced groups | `pd.qcut()` |
    | Detecting passing/failing thresholds | **Bin at the threshold** |

    ## Pro Tips for Datathons

    1. **Interaction first, then bin** — Sometimes bin the ratio!
    2. **Don't overdo it** — Each new feature adds complexity
    3. **Tree models love `pd.qcut()`** — Especially for skewed features
    4. **Test both** — Try raw, binned, and interaction versions separately
    """)
    return


@app.cell
def _(df_interact, pd):
    df_bin = df_interact.copy()

    # Approach 01: Ranged based binning
    age_bins = [0, 25, 45, 100]
    age_labels = ['Youth', 'Mid_Age', 'Senior']
    df_bin['Age_Group'] = pd.cut(df_bin['Age'], bins=age_bins, labels=age_labels)


    # Approach 02: Quantile based binning
    income_labels = ['Tier_3_Low', 'Tied_2_Med', 'Tier_1_High']
    df_bin['Income_Tier'] = pd.qcut(df_bin['Annual_Income_USD'], q=3, labels=income_labels)

    print("--- Continous Quantization Layer Map ---")
    print(df_bin[['Customer_ID', 'Age', 'Age_Group', 'Annual_Income_USD', 'Income_Tier']].head(6))

    # Verify qcut distribution
    print("\nRow distribution per income tier (roughly equal counts)")
    print(df_bin['Income_Tier'].value_counts())
    return


if __name__ == "__main__":
    app.run()

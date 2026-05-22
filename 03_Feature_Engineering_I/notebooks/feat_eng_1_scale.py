import marimo

__generated_with = "0.23.6"
app = marimo.App(width="full", auto_download=["ipynb"])


@app.cell
def _():
    import marimo as mo
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt

    return mo, np, pd


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Numerical Scaling & Skewness Transformations

    ## Why Scale Your Features?

    **The Problem:** Algorithms treat large-number features as "more important"

    - `Age`: 18-80
    - `Income`: $30,000 - $1,500,000

    → Income's massive values **bully** Age into irrelevance

    **Affected Models:**
    - Distance-based: KNN, SVM, K-Means
    - Gradient-based: Neural Networks, Linear Regression

    **⚠️ Tree-Based Exception:** XGBoost, Random Forest, LightGBM don't need scaling (they use order, not distance)

    > **Best Practice:** Scale anyway if you might ensemble tree models with neural networks
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Scaling Methods

    ### 1. Standard Scaling (Z-Score)

    ```
    New Value = (x - mean) / standard deviation
    ```

    - **Result:** Mean = 0, Std Dev = 1
    - **Use when:** Data follows symmetric bell curve (normal distribution)
    """)
    return


@app.cell
def _(StandardScaler, pd):
    # Dont run this, this is an example 

    df_scale = pd.read_csv('datasets/dataset_step2_encoded.csv')

    std_scaler = StandardScaler()
    df_scale['Age_Scaled'] = std_scaler.fit_transform(df_scale[['Age']]) # double [[]] mandatory as scikit-learn requires 2D matrix inptu
    return (df_scale,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 2. MinMax Scaling

    ```
    New Value = (x - min) / (max - min)
    ```

    - **Result:** All values squeezed into [0, 1] range
    - **Essential for:** Neural networks
    - **⚠️ Hazard:** Extreme outliers break this
      - One massive outlier becomes 1.0
      - Regular values get crushed to ~0.0001 (lost resolution)
    """)
    return


@app.cell
def _(df_scale):
    # Dont run this, this is an example 

    from sklearn.preprocessing import MinMaxScaler

    minmax_scaler = MinMaxScaler()
    df_scale['Age_MinMax'] = minmax_scaler.fit_transform(df_scale[['Age']])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Log Transformation: Taming Skewed Data

    ### The Problem: Right Skewness

    Real-world data often has a **long tail of outliers**:
    - Incomes, transaction amounts, web traffic

    ```
    [█▂▁▁▁]  →  [█████]  (after log transform)
    Many small values    Compressed tail
    + few huge outliers  + stretched small values
    ```

    ### Log(x + 1) — The "Safe Log"

    | Issue | Solution |
    |-------|----------|
    | `log(0)` = undefined ($-\infty$) | Add 1 before logging |
    | Data contains zeros (e.g., $0 spent) | `log(x + 1)` fixes it |

    **Implementation:**
    ```python
    # Correct way
    np.log1p(df['income'])  # log(income + 1)

    # Wrong way (crashes on zeros)
    np.log(df['income'])
    ```
    """)
    return


@app.cell
def _(df_scale, np):
    # Dont run this, this is an example 
    df_scale['Income_Log'] = np.log1p(df_scale['Annual_Income_USD'])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Quick Decision Guide

    | Data Characteristic | Best Transformation |
    |--------------------|--------------------|
    | Normal distribution | Standard Scaling |
    | Bounded range needed (e.g., neural nets) | MinMax Scaling |
    | Right-skewed (long tail of outliers) | Log Transformation |
    | Has zeros in the data | Use `log1p` not `log` |
    | Tree-based model only | No scaling needed |

    ---

    ## Before vs After: Visual Intuition

    **Right-Skewed Income Data:**
    ```
    Before: [100, 200, 300, 500, 1000, 50000] ← outlier
    After log: [4.6, 5.3, 5.7, 6.2, 6.9, 10.8] ← compressed tail
    ```

    **Key Insight:** Log transform turns multiplicative relationships into additive ones, making linear models work better!
    """)
    return


@app.cell
def _(np, pd):
    # Based on our dataset, we have an outlier for customer 1003 having income 150k. So do log transformation first to fix the skew. Then apply scaling
    # Run this

    from sklearn.preprocessing import MinMaxScaler, StandardScaler

    df_num = pd.read_csv('datasets/dataset_step2_encoded.csv')

    # Log transformation for taming the outlier
    df_num['Income_Log'] = np.log1p(df_num['Annual_Income_USD'])

    # Standard Scaling (Z Score) on Age
    age_scaler = StandardScaler()
    df_num['Age_Scaled'] = age_scaler.fit_transform(df_num[['Age']])

    # Min_Max Scaling on Income
    income_scaler = MinMaxScaler()
    df_num['Income_Scaled'] = income_scaler.fit_transform(df_num[['Income_Log']])

    print("--- Cleaned, Encoded, Sclaed Feature Set ---")
    columns_to_print = ['Customer_ID', 'Age_Scaled', 'Annual_Income_USD', 'Income_Log', 'Income_Scaled']
    print(df_num[columns_to_print].head(6))
    return StandardScaler, df_num


@app.cell
def _(df_num):
    # Save the dataset
    df_num.to_csv('datasets/dataset_step3_scaled.csv', index=False)
    print('Scaled Dataset saved successfully.')
    return


if __name__ == "__main__":
    app.run()

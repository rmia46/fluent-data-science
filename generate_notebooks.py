import json
import os

def create_notebook(cells, filename):
    notebook = {
        "cells": cells,
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 5
    }
    # Ensure directory exists
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w') as f:
        json.dump(notebook, f, indent=2)

def md_cell(text):
    return {"cell_type": "markdown", "metadata": {}, "source": [line + "\n" for line in text.split("\n")]}

def code_cell(code):
    return {"cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [], "source": [line + "\n" for line in code.split("\n")]}

# --- Day 1: Mathematics ---
math_cells = [
    md_cell("# Day 1 Practice: Mathematics for Machine Learning & Data Science\n\nComplete the following code implementations. Run the validation cells to check your results."),
    code_cell("import numpy as np\nimport sys\nimport os\n\n# Install ipytest if not present (Colab/Kaggle compatibility)\ntry:\n    import ipytest\nexcept ImportError:\n    !pip install -q ipytest\n    import ipytest\n\n# Handle validation script import (Colab specific: users might need to upload it)\nif not os.path.exists('validate_day1.py'):\n    print('⚠️ validate_day1.py not found! Please upload it to your Colab workspace.')\nelse:\n    import validate_day1\n\nipytest.autoconfig()"),
    
    md_cell("## Session 1: Linear Algebra\n**Task 1:** Create two random $3 \\times 3$ matrices `A` and `B`. Compute `dot_product` and `element_wise` product."),
    code_cell("A = np.random.rand(3, 3)\nB = np.random.rand(3, 3)\ndot_product = None\nelement_wise = None"),
    code_cell("%%ipytest -qq\ntry:\n    validate_day1.test_task_1()\nexcept NameError:\n    print('Skip: validate_day1 not imported')"),
    
    md_cell("**Task 2:** Solve for `solution`: \n$2x + y = 5$\n$x - 3y = -1$"),
    code_cell("solution = None"),
    code_cell("%%ipytest -qq\ntry:\n    validate_day1.test_task_2()\nexcept NameError:\n    print('Skip: validate_day1 not imported')"),
    
    md_cell("## Session 2: Calculus & Gradient Descent\n**Task 3:** Implement Gradient Descent to minimize $f(x) = x^2 - 4x + 4$. Store result in `x`."),
    code_cell("x = 10.0\nlearning_rate = 0.1\n# Your loop here"),
    code_cell("%%ipytest -qq\ntry:\n    validate_day1.test_task_3()\nexcept NameError:\n    print('Skip: validate_day1 not imported')"),
    
    md_cell("## Session 3: Probability & Statistics\n**Task 4:** Generate 1000 `samples` from Normal(50, 15). Calculate `mean`, `median`, and `variance`."),
    code_cell("samples = None\nmean = None\nmedian = None\nvariance = None"),
    code_cell("%%ipytest -qq\ntry:\n    validate_day1.test_task_4()\nexcept NameError:\n    print('Skip: validate_day1 not imported')")
]

create_notebook(math_cells, '01_Mathematics_for_ML/notebooks/Day1_Mathematics_for_ML_Practice.ipynb')

# --- Day 2: Tabular Foundations ---
pandas_cells = [
    md_cell("# Day 2 Practice: Tabular Foundations & Fast Data Manipulation\n\nMastering pandas is essential for any datathon. Complete these high-speed data manipulation challenges."),
    code_cell("import pandas as pd\nimport numpy as np\nimport sys\nimport os\n\n# Setup validation\ntry:\n    import ipytest\nexcept ImportError:\n    !pip install -q ipytest\n    import ipytest\n\nif not os.path.exists('validate_day2.py'):\n    print('⚠️ validate_day2.py not found! Please upload it.')\nelse:\n    import validate_day2\n\nipytest.autoconfig()"),
    
    md_cell("## 1. Setup Sample Data\nRun the cell below to create the initial dataset for practice."),
    code_cell("df = pd.DataFrame({\n    'ID': range(1, 11),\n    'City': ['Dhaka', 'Chittagong', 'Dhaka', 'Sylhet', 'Dhaka', 'Sylhet', 'Chittagong', 'Dhaka', 'Rajshahi', 'Sylhet'],\n    'Price': [100, 250, 150, 300, 200, 450, 120, 350, 220, 180],\n    'Quantity': [2, 1, 5, 3, 2, 1, 4, 2, 5, 3],\n    'Score': [85, 92, np.nan, 78, 95, 88, np.nan, 82, 90, 75]\n})"),
    
    md_cell("## 2. Vectorization (The Loops Ban)\n**Task 1:** Calculate a new column `Total` which is `Price` multiplied by `Quantity`. Use vectorized operations, NOT a loop."),
    code_cell("# Your code here\n# df['Total'] = ..."),
    code_cell("%%ipytest -qq\ntry:\n    validate_day2.test_task_1()\nexcept NameError: pass"),
    
    md_cell("## 3. Advanced Filtering & Indexing\n**Task 2:** Create a new DataFrame `df_filtered` containing only rows where:\n- `Score` is greater than 80\n- `City` is either 'Dhaka' or 'Sylhet'\nUse Boolean Indexing with bitwise operators."),
    code_cell("# Your code here\n# df_filtered = ..."),
    code_cell("%%ipytest -qq\ntry:\n    validate_day2.test_task_2()\nexcept NameError: pass"),
    
    md_cell("## 4. Grouping & Aggregating\n**Task 3:** Create a summary table `city_summary` that shows the **mean** and **count** of `Score` for each `City`."),
    code_cell("# Your code here\n# city_summary = ..."),
    code_cell("%%ipytest -qq\ntry:\n    validate_day2.test_task_3()\nexcept NameError: pass"),
    
    md_cell("## 5. Merging Datasets\n**Task 4:** Create a mapping DataFrame `df_region` with columns `City` and `Region`. Merge it with your main `df` using a **left join** so you don't lose any students. Store in `df_merged`."),
    code_cell("df_region = pd.DataFrame({'City': ['Dhaka', 'Chittagong', 'Sylhet', 'Rajshahi'], 'Region': ['Central', 'East', 'North', 'West']})\n# Your code here\n# df_merged = ..."),
    code_cell("%%ipytest -qq\ntry:\n    validate_day2.test_task_4()\nexcept NameError: pass"),
    
    md_cell("## 6. Diagnostic Data Cleaning\n**Task 5:** Create a binary indicator column `Score_was_missing` for the `Score` column. Then, fill the missing values in `Score` with its **median**."),
    code_cell("# Your code here\n# df['Score_was_missing'] = ...\n# df['Score'] = ..."),
    code_cell("%%ipytest -qq\ntry:\n    validate_day2.test_task_5()\nexcept NameError: pass")
]

# --- Day 3: Feature Engineering I ---
fe_cells = [
    md_cell("# Day 3 Practice: Feature Engineering I\n\nTransforming raw data into predictive signals. Complete the tasks below."),
    code_cell("import pandas as pd\nimport numpy as np\nfrom sklearn.preprocessing import StandardScaler\nimport sys\nimport os\n\n# Setup validation\ntry:\n    import ipytest\nexcept ImportError:\n    !pip install -q ipytest\n    import ipytest\n\nif not os.path.exists('validate_day3.py'):\n    print('⚠️ validate_day3.py not found! Please upload it.')\nelse:\n    import validate_day3\n\nipytest.autoconfig()"),
    
    md_cell("## 1. Setup Sample Data\nRun this cell to create the dataset for today's practice."),
    code_cell("df = pd.DataFrame({\n    'User_ID': range(1, 11),\n    'City': ['Dhaka', 'Dhaka', 'Chittagong', 'Sylhet', 'Dhaka', 'Chittagong', 'Rajshahi', 'Dhaka', 'Sylhet', 'Dhaka'],\n    'Priority': ['Low', 'High', 'Medium', 'Low', 'High', 'Medium', 'Low', 'Medium', 'High', 'Low'],\n    'Age': [25, 45, 30, 22, 55, 35, 28, 40, 50, 19],\n    'Income': [50000, 120000, 75000, 45000, 250000, 90000, 60000, 85000, 150000, 35000],\n    'Total_Spend': [1200, 5000, 2500, 800, 15000, 3200, 1500, 2800, 6000, 400],\n    'Years_Member': [2, 5, 3, 1, 10, 4, 2, 3, 6, 1]\n})"),
    
    md_cell("## 2. Categorical Encoding\n**Task 1:** \n- Create a new column `Priority_Level` by ordinally encoding `Priority` (Low=0, Medium=1, High=2).\n- Create a new column `City_Freq` using **Frequency Encoding** for the `City` column."),
    code_cell("# Your code here\n"),
    code_cell("%%ipytest -qq\ntry:\n    validate_day3.test_task_1()\nexcept NameError: pass"),
    
    md_cell("## 3. Numerical Transformations\n**Task 2:** \n- Apply a **Log Transformation** to the `Income` column and store it in `Income_Log`.\n- Apply **Standard Scaling** to the `Age` column and store it in `Age_Scaled`."),
    code_cell("# Your code here\n"),
    code_cell("%%ipytest -qq\ntry:\n    validate_day3.test_task_2()\nexcept NameError: pass"),
    
    md_cell("## 4. Interaction Features\n**Task 3:** Create an interaction feature `Spend_Per_Year` which is `Total_Spend` divided by `Years_Member`."),
    code_cell("# Your code here\n"),
    code_cell("%%ipytest -qq\ntry:\n    validate_day3.test_task_3()\nexcept NameError: pass"),
    
    md_cell("## 5. Continuous Binning\n**Task 4:** Create a new categorical column `Age_Group` by binning the `Age` column into 4 equal-frequency quartiles using `pd.qcut`."),
    code_cell("# Your code here\n"),
    code_cell("%%ipytest -qq\ntry:\n    validate_day3.test_task_4()\nexcept NameError: pass")
]

# --- Day 4: Advanced Feature Engineering (The Grandmaster's Toolkit) ---
fe2_cells = [
    md_cell("# Day 4 Practice: Advanced Golden Features & Automated Selection\n\n**Role:** Competitive Kaggle Grandmaster\n\nWelcome to the elite level of feature engineering. Today, we move beyond simple scaling and categorical maps. You will implement high-performance, leakage-proof transformations and automated pruning loops to handle high-dimensional, complex relational data."),
    code_cell("import pandas as pd\nimport numpy as np\nimport lightgbm as lgb\nfrom sklearn.model_selection import KFold\nimport sys\nimport os\n\n# Setup validation\ntry:\n    import ipytest\nexcept ImportError:\n    !pip install -q ipytest\n    import ipytest\n\nif not os.path.exists('validate_day4.py'):\n    print('⚠️ validate_day4.py not found!')\nelse:\n    import validate_day4\n\nipytest.autoconfig()"),
    
    md_cell("## 1. Synthetic Relational Dataset\nRun the cell below to generate our competition-style dataset. It contains user transaction sequences, high-cardinality categories, and collinear noise."),
    code_cell("np.random.seed(42)\nn_users = 1000\nrows_per_user = 5\nn_rows = n_users * rows_per_user\n\ndf = pd.DataFrame({\n    'User_ID': np.repeat(np.arange(n_users), rows_per_user),\n    'High_Card_Cat': np.random.choice([f'Cat_{i}' for i in range(250)], n_rows),\n    'Spend': np.random.gamma(2, 50, n_rows),\n    'Transaction_Seq': np.tile(np.arange(rows_per_user), n_users),\n    'Target': np.random.randint(0, 2, n_rows)\n})\n\n# Adding intentional collinearity (> 0.92 correlation)\ndf['Collinear_Feature'] = df['Spend'] * 1.5 + np.random.normal(0, 0.5, n_rows)\ndf['Random_Noise'] = np.random.randn(n_rows)\n\nprint(f\"Dataset Shape: {df.shape}\")\ndf.head()"),
    
    md_cell("## Challenge 1: Leakage-Proof Custom Target Encoder\n**Task:** Implement a Target Encoder from scratch. \n1. Use **5-Fold Out-of-Fold (OOF)** cross-validation to calculate means (i.e., the mean for a row in Fold 1 must be calculated using only Folds 2-5).\n2. Apply **Smoothing** with $m=10$ to handle rare categories.\n3. Store result in `Category_Target`."),
    code_cell("# YOUR CODE HERE\n# 1. Init Category_Target column\n# 2. Setup KFold(n_splits=5)\n# 3. Loop: Calc smoothed means on Train-folds, map to Val-fold\n# Formula: (mean * count + global_mean * m) / (count + m)"),
    code_cell("%%ipytest -qq\ntry:\n    validate_day4.test_task_1()\nexcept NameError: pass"),
    
    md_cell("## Challenge 2: Contextual Behavioral Features\n**Task:** Use Pandas `.transform()` to create 3 features that give the model context about a user's spending habits:\n1. `User_Mean_Spend`: Average spend per `User_ID`.\n2. `User_Spend_Std`: Standard deviation of spend per `User_ID`.\n3. `Spend_Rel_to_User`: Current `Spend` minus `User_Mean_Spend`."),
    code_cell("# YOUR CODE HERE\n"),
    code_cell("%%ipytest -qq\ntry:\n    validate_day4.test_task_2()\nexcept NameError: pass"),
    
    md_cell("## Challenge 3: Automated Collinear Pruning\n**Task:** Write a loop that inspects the correlation matrix. Identify and store the names of all columns that have a correlation $> 0.92$ with *any other column already in the set*. Store these names in a list called `to_drop`."),
    code_cell("# YOUR CODE HERE\n# Hint: Use df.corr().abs() and np.triu(..., k=1)"),
    code_cell("%%ipytest -qq\ntry:\n    validate_day4.test_task_3()\nexcept NameError: pass"),
    
    md_cell("## Challenge 4: Feature Importance Ranking\n**Task:** Use a default `LGBMClassifier` to rank all features (excluding the `Target` and `User_ID`). Store the resulting importances in a Series named `feature_importances`."),
    code_cell("# YOUR CODE HERE\n"),
    code_cell("%%ipytest -qq\ntry:\n    validate_day4.test_task_4()\nexcept NameError: pass"),
    
    md_cell("<details>\n<summary style='color: #d35400; font-weight: bold; cursor: pointer;'>🏆 Click for Grandmaster Optimized Solutions</summary>\n\n```python\n# Solution 1: OOF Target Encoding\nm = 10\nglobal_mean = df['Target'].mean()\ndf['Category_Target'] = 0.0\nkf = KFold(n_splits=5, shuffle=True, random_state=42)\n\nfor train_idx, val_idx in kf.split(df):\n    train_fold = df.iloc[train_idx]\n    agg = train_fold.groupby('High_Card_Cat')['Target'].agg(['count', 'mean'])\n    smoothed = (agg['mean'] * agg['count'] + global_mean * m) / (agg['count'] + m)\n    df.loc[df.index[val_idx], 'Category_Target'] = df.loc[df.index[val_idx], 'High_Card_Cat'].map(smoothed).fillna(global_mean)\n\n# Solution 2: Contextual Features\ndf['User_Mean_Spend'] = df.groupby('User_ID')['Spend'].transform('mean')\ndf['User_Spend_Std'] = df.groupby('User_ID')['Spend'].transform('std')\ndf['Spend_Rel_to_User'] = df['Spend'] - df['User_Mean_Spend']\n\n# Solution 3: Collinear Pruning\ncorr_matrix = df.select_dtypes(include=[np.number]).corr().abs()\nupper = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(bool))\nto_drop = [column for column in upper.columns if any(upper[column] > 0.92)]\n\n# Solution 4: LightGBM Importance\nX = df.select_dtypes(include=[np.number]).drop(columns=['Target', 'User_ID'])\ny = df['Target']\nmodel = lgb.LGBMClassifier(verbose=-1).fit(X, y)\nfeature_importances = pd.Series(model.feature_importances_, index=X.columns).sort_values(ascending=False)\n```\n</details>")
]

# --- Day 6: Tree-Based Models ---
tree_cells = [
    md_cell("# Day 6 Practice: Tree-Based Models & Regularization\n\n**Role:** Competitive Kaggle Grandmaster\n\nToday, we benchmark the heavy hitters: LightGBM and XGBoost. You will build cross-validation pipelines, map overfitting curves, and learn to tame complex trees using stochastic regularization."),
    code_cell("import pandas as pd\nimport numpy as np\nimport lightgbm as lgb\nimport xgboost as xgb\nfrom sklearn.model_selection import StratifiedKFold\nfrom sklearn.metrics import log_loss\nimport matplotlib.pyplot as plt\nimport sys\nimport os\n\n# Setup validation\ntry:\n    import ipytest\nexcept ImportError:\n    !pip install -q ipytest\n    import ipytest\n\nif not os.path.exists('validate_day6.py'):\n    print('⚠️ validate_day6.py not found!')\nelse:\n    import validate_day6\n\nipytest.autoconfig()"),
    
    md_cell("## 1. Setup Synthetic Dataset\nGenerating a dataset with missing values and mixed types (categoricals)."),
    code_cell("np.random.seed(42)\nn_rows = 5000\ndf = pd.DataFrame({\n    'f1': np.random.randn(n_rows),\n    'f2': np.random.randn(n_rows),\n    'f3': np.random.choice(['A', 'B', 'C', np.nan], n_rows),\n    'Target': np.random.randint(0, 2, n_rows)\n})\ndf['f3'] = df['f3'].astype('category')\nX = df.drop(columns='Target')\ny = df['Target']"),
    
    md_cell("## Challenge 1: LightGBM OOF Loop\n**Task:** Train a baseline `LGBMClassifier` inside a 5-fold CV loop. Track the predictions in `lgbm_oof_preds`."),
    code_cell("# YOUR CODE HERE"),
    code_cell("%%ipytest -qq\ntry:\n    validate_day6.test_task_1()\nexcept NameError: pass"),
    
    md_cell("## Challenge 2: XGBoost Baseline\n**Task:** Re-run the CV loop using an `XGBClassifier`. Use the same KFold indices as Challenge 1. Store in `xgb_oof_preds`."),
    code_cell("# YOUR CODE HERE"),
    code_cell("%%ipytest -qq\ntry:\n    validate_day6.test_task_2()\nexcept NameError: pass"),
    
    md_cell("## Challenge 3: Overfitting Curve\n**Task:** Iterate through depths [2, 5, 10, 20, 50]. Train LGBM and record log-loss for both Train and Val sets. Plot to see where they diverge."),
    code_cell("# YOUR CODE HERE\n# train_scores = []; val_scores = []"),
    code_cell("%%ipytest -qq\ntry:\n    validate_day6.test_task_3()\nexcept NameError: pass"),
    
    md_cell("## Challenge 4: Stochastic Regularization\n**Task:** Apply `subsample=0.8` and `colsample_bytree=0.8` to your best performing model. Check if the validation score (`reg_val_score`) improves compared to the overfitted baseline."),
    code_cell("# YOUR CODE HERE"),
    code_cell("%%ipytest -qq\ntry:\n    validate_day6.test_task_4()\nexcept NameError: pass"),
    
    md_cell("<details>\n<summary style='color: #d35400; font-weight: bold; cursor: pointer;'>🏆 Click for Grandmaster Optimized Solutions</summary>\n\n```python\n# 1 & 2. OOF Baselines\nskf = StratifiedKFold(n_splits=5)\nlgbm_oof_preds = np.zeros(len(df))\nxgb_oof_preds = np.zeros(len(df))\nfor tr, val in skf.split(X, y):\n    lgbm_oof_preds[val] = lgb.LGBMClassifier().fit(X.iloc[tr], y.iloc[tr]).predict_proba(X.iloc[val])[:,1]\n    xgb_oof_preds[val] = xgb.XGBClassifier().fit(X.iloc[tr], y.iloc[tr]).predict_proba(X.iloc[val])[:,1]\n\n# 3. Overfitting Curve\ntrain_scores, val_scores = [], []\nfor d in [2, 5, 10, 20, 50]:\n    model = lgb.LGBMClassifier(max_depth=d).fit(X.iloc[tr], y.iloc[tr])\n    train_scores.append(log_loss(y.iloc[tr], model.predict_proba(X.iloc[tr])[:,1]))\n    val_scores.append(log_loss(y.iloc[val], model.predict_proba(X.iloc[val])[:,1]))\n\n# 4. Stochastic Regularization\nreg_model = lgb.LGBMClassifier(subsample=0.8, colsample_bytree=0.8, max_depth=50).fit(X.iloc[tr], y.iloc[tr])\nreg_val_score = log_loss(y.iloc[val], reg_model.predict_proba(X.iloc[val])[:,1])\n```\n</details>")
]

# --- Day 7: Optimization & Ensembling ---
opt_cells = [
    md_cell("# Day 7 Practice: Optimization & Ensembling (Grandmaster Level)\n\n**Role:** Competitive Kaggle Grandmaster\n\nToday, you go for the gold. You will build a complete optimization and ensembling pipeline: tuning models with Optuna, extracting OOF predictions, blending model outputs, and finally performing a post-processing threshold sweep to maximize your metric."),
    code_cell("import pandas as pd\nimport numpy as np\nimport lightgbm as lgb\nimport xgboost as xgb\nimport optuna\nfrom sklearn.model_selection import StratifiedKFold\nfrom sklearn.metrics import f1_score\nimport sys\nimport os\n\n# Setup validation\ntry:\n    import ipytest\nexcept ImportError:\n    !pip install -q ipytest\n    import ipytest\n\nif not os.path.exists('validate_day7.py'):\n    print('⚠️ validate_day7.py not found!')\nelse:\n    import validate_day7\n\nipytest.autoconfig()"),
    
    md_cell("## 1. Dataset Generation\nGenerating a synthetic imbalanced dataset."),
    code_cell("from sklearn.datasets import make_classification\nX, y = make_classification(n_samples=2000, n_features=20, n_informative=10, weights=[0.9, 0.1], random_state=42)\ndf = pd.DataFrame(X, columns=[f'f{i}' for i in range(20)])\ndf['Target'] = y"),
    
    md_cell("## Challenge 1: Optuna Objective Function\n**Task:** Write an objective function to tune 5 LightGBM params (`num_leaves`, `learning_rate`, `n_estimators`, `max_depth`, `subsample`) over 20 trials."),
    code_cell("# YOUR CODE HERE\n# def objective(trial):\n# ... return CV score"),
    code_cell("%%ipytest -qq\ntry:\n    validate_day7.test_task_1()\nexcept NameError: pass"),
    
    md_cell("## Challenge 2: OOF Extraction\n**Task:** Run optimized LGBM and XGBoost models using 5-Fold CV. Store OOF probabilities in `lgbm_oof` and `xgb_oof`."),
    code_cell("# YOUR CODE HERE"),
    code_cell("%%ipytest -qq\ntry:\n    validate_day7.test_task_2()\nexcept NameError: pass"),
    
    md_cell("## Challenge 3: Blending\n**Task:** Compute a weighted blend: `blend_preds = w * lgbm_oof + (1-w) * xgb_oof`. Find the `w` (0.0 to 1.0) that maximizes the F1 score."),
    code_cell("# YOUR CODE HERE"),
    code_cell("%%ipytest -qq\ntry:\n    validate_day7.test_task_3()\nexcept NameError: pass"),
    
    md_cell("## Challenge 4: Post-Processing Threshold Search\n**Task:** Sweep probability thresholds from 0.01 to 0.99. Find the `best_threshold` that yields the maximum F1-score."),
    code_cell("# YOUR CODE HERE"),
    code_cell("%%ipytest -qq\ntry:\n    validate_day7.test_task_4()\nexcept NameError: pass"),
    
    md_cell("<details>\n<summary style='color: #d35400; font-weight: bold; cursor: pointer;'>🏆 Click for Grandmaster Optimized Solutions</summary>\n\n```python\n# 1. Optuna\ndef objective(trial):\n    params = { 'num_leaves': trial.suggest_int('nl', 20, 100), 'learning_rate': trial.suggest_float('lr', 0.01, 0.3), ... }\n    # ... CV ...\nstudy = optuna.create_study(direction='maximize').optimize(objective, n_trials=20)\nbest_params = study.best_params\n\n# 2. OOF\n# ... CV loop extracting lgbm_oof and xgb_oof ...\n\n# 3. Blending\nscores = [f1_score(y, (w * lgbm_oof + (1-w) * xgb_oof) > 0.5) for w in np.linspace(0,1,10)]\nblend_preds = 0.5 * lgbm_oof + 0.5 * xgb_oof\n\n# 4. Threshold search\nthresholds = np.linspace(0.01, 0.99, 100)\nscores = [f1_score(y, blend_preds > t) for t in thresholds]\nbest_threshold = thresholds[np.argmax(scores)]\nbest_f1 = max(scores)\n```\n</details>")
]

create_notebook(opt_cells, '07_Optimization_and_Ensembling/notebooks/Day7_Optimization_and_Ensembling_Practice.ipynb')


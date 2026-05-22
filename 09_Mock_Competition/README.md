# Module 09 Mock Competition: Customer Churn Challenge

## Objective
Predict whether a user will churn (binary classification).

## The Dataset
We provide three files:
1. `train.csv`: User demographics and the churn target.
2. `test.csv`: User demographics for inference.
3. `transactions.csv`: Historical transaction history per user.

## The Challenge
1. **Relational Engineering:** Merge transaction data (aggregated) with user profiles.
2. **Contextual Signals:** Engineer features like 'Spend vs Personal Average' or 'Spend Z-score per Zip'.
3. **Advanced Encoding:** Use Smoothed Target Encoding for the high-cardinality `zip_code` feature.
4. **Validation Strategy:** Implement a robust 5-Fold Stratified CV.
5. **Adversarial Drift Check:** Detect and handle the intentional 'Age Drift' between train and test.

## Common Pitfalls to Avoid
- **Leakage:** Do not use target encoding across the whole dataset.
- **Drift:** Observe the age shift in the test set. Decide whether to drop the `age` feature or transform it to be invariant to the shift.
- **Redundancy:** Prune highly collinear features generated during feature engineering.

## Submission
- Export your OOF predictions and your final test predictions.
- Evaluate performance using F1-score (due to class imbalance).

# Fluent Data Science: Datathon Curriculum

**Built in a few hours using Gemini AI guidance to sprint-train for a University Datathon.**

This repository contains a comprehensive curriculum designed for competitive data science. We cover the topics from mathematical foundations to production-grade model ensembling. Note that some advanced topics may be missing due to time constraints and a pure focus on the specific needs of a datathon contest.

## Curriculum Structure

The curriculum is organized into modular directories, each containing:
- **`notebooks/`**: Theory and Practice Jupyter Notebooks, optimized for Google Colab and Kaggle, featuring automated validation logic (`ipytest`).
- **`theory_tex/`**: Professional LaTeX source files for high-quality, comprehensive theory reading materials.
- **`pdf_materials/`**: Compiled PDFs for student distribution.
- **`Validation.py`**: Automated test scripts that verify code correctness in student exercises.

## Modules

- **01: Mathematics for ML**: Linear Algebra, Calculus, and Probability/Statistics foundations.
- **02: Tabular Foundations**: Pandas high-speed data manipulation, indexing, and cleaning.
- **03: Feature Engineering I**: Categorical encoding, numerical transformations, interactions, and binning.
- **04: Feature Engineering II**: Advanced OOF Target Encoding, contextual group-level transforms, and automated feature selection.
- **05: Validation Architecture**: Robust Stratified K-Fold CV, leakage detection, and baseline models.
- **06: Tree-Based Models**: LightGBM/XGBoost baseline training, overfitting analysis, and regularization.
- **07: Optimization & Ensembling**: Optuna hyperparameter tuning, OOF blending, and threshold optimization.
- **08: Production Pipelines**: Architectural guides for scaling models to production.
- **09: Mock Competition**: A comprehensive churn-prediction capstone challenge with real-world complexities.

## Development & Usage
- **Notebook Validation**: Practice notebooks utilize `ipytest` to provide immediate pass/fail feedback.
- **Git Workflow**: This repository is version-controlled to allow for iterative updates and collaborative development.
EOF

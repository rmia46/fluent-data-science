import numpy as np
import pandas as pd
import sys
from sklearn.metrics import roc_auc_score

def test_task_1():
    """Validates Stratified 5-Fold OOF loop structure"""
    main = sys.modules.get('__main__')
    if not main: return
    
    assert hasattr(main, 'oof_preds'), "OOF predictions array missing."
    assert len(main.oof_preds) == len(main.df), "OOF array length does not match dataset."
    # Ensure not all predictions are the same
    assert len(np.unique(main.oof_preds)) > 1, "OOF predictions look constant."

def test_task_2():
    """Validates RF Baseline & Submission format"""
    main = sys.modules.get('__main__')
    if not main: return
    
    assert hasattr(main, 'submission'), "Submission dataframe missing."
    assert 'ID' in main.submission.columns and 'Prediction' in main.submission.columns, "Submission format incorrect."
    assert len(main.submission) == len(main.df_test), "Submission length mismatch."

def test_task_3():
    """Validates Leaked Logic detection"""
    main = sys.modules.get('__main__')
    if not main: return
    
    # Check if a model using global scaling performs significantly better than a proper one
    assert hasattr(main, 'leaked_score'), "Leaked score not tracked."
    assert hasattr(main, 'robust_score'), "Robust score not tracked."
    assert main.leaked_score > main.robust_score, "Leaked score should be artificially higher."

def test_task_4():
    """Validates Refactored Leakage-Free Pipeline"""
    main = sys.modules.get('__main__')
    if not main: return
    
    # Logic: ensure scaler was fitted only on train fold
    # We can check if the final robust AUC is realistic
    assert main.robust_score > 0.5, "Robust model performance is too low; check folding logic."

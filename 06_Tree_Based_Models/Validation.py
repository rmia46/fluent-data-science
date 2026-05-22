import numpy as np
import pandas as pd
import sys
from sklearn.metrics import log_loss

def test_task_1():
    """Validates LGBM OOF baseline"""
    main = sys.modules.get('__main__')
    if not main: return
    
    assert hasattr(main, 'lgbm_oof_preds'), "lgbm_oof_preds missing."
    assert len(main.lgbm_oof_preds) == len(main.df), "Prediction length mismatch."
    assert not np.isnan(main.lgbm_oof_preds).any(), "Found NaNs in predictions."

def test_task_2():
    """Validates XGBoost OOF baseline"""
    main = sys.modules.get('__main__')
    if not main: return
    
    assert hasattr(main, 'xgb_oof_preds'), "xgb_oof_preds missing."
    assert len(main.xgb_oof_preds) == len(main.df), "Prediction length mismatch."
    assert not np.isnan(main.xgb_oof_preds).any(), "Found NaNs in predictions."

def test_task_3():
    """Validates Overfitting Visualization Logic"""
    main = sys.modules.get('__main__')
    if not main: return
    
    assert hasattr(main, 'train_scores'), "train_scores list missing."
    assert hasattr(main, 'val_scores'), "val_scores list missing."
    assert len(main.train_scores) == len(main.val_scores), "Length mismatch."
    assert main.train_scores[-1] < main.val_scores[-1], "Model is not clearly overfitting (Train < Val expected)."

def test_task_4():
    """Validates Regularization effect"""
    main = sys.modules.get('__main__')
    if not main: return
    
    assert hasattr(main, 'reg_val_score'), "reg_val_score missing."
    assert main.reg_val_score < main.val_scores[-1], "Regularized score should be better than the overfitted score."

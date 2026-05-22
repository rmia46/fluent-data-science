import numpy as np
import pandas as pd
import sys
from sklearn.metrics import f1_score

def test_task_1():
    """Validates Optuna Optimization"""
    main = sys.modules.get('__main__')
    if not main: return
    
    assert hasattr(main, 'best_params'), "best_params missing."
    assert len(main.best_params) >= 5, "Not all 5 hyperparameters were tuned."
    assert isinstance(main.best_params, dict), "best_params should be a dictionary."

def test_task_2():
    """Validates OOF extraction"""
    main = sys.modules.get('__main__')
    if not main: return
    
    assert hasattr(main, 'lgbm_oof'), "lgbm_oof missing."
    assert hasattr(main, 'xgb_oof'), "xgb_oof missing."
    assert len(main.lgbm_oof) == len(main.df), "Prediction length mismatch."

def test_task_3():
    """Validates Blending"""
    main = sys.modules.get('__main__')
    if not main: return
    
    assert hasattr(main, 'blend_preds'), "blend_preds missing."
    assert np.all((main.blend_preds >= 0) & (main.blend_preds <= 1)), "Blended predictions should be probabilities [0, 1]."

def test_task_4():
    """Validates Threshold Search"""
    main = sys.modules.get('__main__')
    if not main: return
    
    assert hasattr(main, 'best_threshold'), "best_threshold missing."
    assert 0.01 <= main.best_threshold <= 0.99, "Threshold out of range."
    assert hasattr(main, 'best_f1'), "best_f1 not found."

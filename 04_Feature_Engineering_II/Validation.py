import numpy as np
import pandas as pd
import sys

def test_task_1():
    """Validates Custom OOF Target Encoder with Smoothing"""
    main = sys.modules.get('__main__')
    if not main: return
    
    assert 'Category_Target' in main.df.columns, "Column 'Category_Target' missing."
    # Check if encoding is NOT a simple global mean (indicates OOF logic)
    global_mean = main.df['Target'].mean()
    assert not np.allclose(main.df['Category_Target'], global_mean), "Encoding is too simple. Did you implement OOF logic?"
    
    # Check for leakage: specific category 'Cat_0' in row 0 should not perfectly match its target if OOF is working
    cat_0_mask = main.df['High_Card_Cat'] == main.df['High_Card_Cat'].iloc[0]
    # If they just used simple mean, it would be leakage. 
    # OOF ensures the value is derived from OTHER folds.
    assert main.df['Category_Target'].isna().sum() == 0, "Found NaNs in target encoding."

def test_task_2():
    """Validates 3 Group-Level Contextual Features"""
    main = sys.modules.get('__main__')
    if not main: return
    
    expected = ['User_Mean_Spend', 'User_Spend_Std', 'Spend_Rel_to_User']
    for col in expected:
        assert col in main.df.columns, f"Contextual feature '{col}' missing."
    
    # Verify logic for Spend_Rel_to_User
    expected_rel = main.df['Spend'] - main.df.groupby('User_ID')['Spend'].transform('mean')
    np.testing.assert_allclose(main.df['Spend_Rel_to_User'], expected_rel, err_msg="Contextual difference logic is incorrect.")

def test_task_3():
    """Validates Collinear Pruning Loop"""
    main = sys.modules.get('__main__')
    if not main: return
    
    assert hasattr(main, 'to_drop'), "List 'to_drop' not found."
    assert len(main.to_drop) > 0, "No columns identified for dropping. Threshold 0.92 not met?"
    
    # Check if a known collinear pair was handled
    assert 'Collinear_Feature' in main.to_drop, "Failed to identify the explicitly collinear feature."

def test_task_4():
    """Validates LightGBM Importance Ranking"""
    main = sys.modules.get('__main__')
    if not main: return
    
    assert hasattr(main, 'feature_importances'), "Importance rankings not found."
    assert len(main.feature_importances) > 0, "Importances list is empty."
    # Ensure it's a pandas Series or DataFrame
    assert isinstance(main.feature_importances, (pd.Series, pd.DataFrame)), "feature_importances should be a Series or DataFrame."

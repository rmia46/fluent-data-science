import numpy as np
import pandas as pd
import sys

def test_task_1():
    """Validates Categorical Encoding"""
    main = sys.modules.get('__main__')
    if not main: return
    
    # 1. Check Ordinal Encoding
    assert 'Priority_Level' in main.df.columns, "Column 'Priority_Level' not found."
    assert main.df['Priority_Level'].dtype in ['int64', 'float64'], "Priority_Level should be numeric."
    
    # 2. Check Frequency Encoding
    assert 'City_Freq' in main.df.columns, "Column 'City_Freq' not found."
    expected_freq = main.df['City'].value_counts(normalize=True)
    assert np.isclose(main.df['City_Freq'].iloc[0], expected_freq[main.df['City'].iloc[0]]), "City_Freq calculation is incorrect."

def test_task_2():
    """Validates Scaling & Transformations"""
    main = sys.modules.get('__main__')
    if not main: return
    
    # 1. Check Log Transformation
    assert 'Income_Log' in main.df.columns, "Column 'Income_Log' not found."
    np.testing.assert_allclose(main.df['Income_Log'], np.log1p(main.df['Income']), err_msg="Log transformation should use np.log1p.")
    
    # 2. Check Standard Scaling
    assert 'Age_Scaled' in main.df.columns, "Column 'Age_Scaled' not found."
    assert np.isclose(main.df['Age_Scaled'].mean(), 0, atol=1e-7), "Age_Scaled mean should be ~0."
    assert np.isclose(main.df['Age_Scaled'].std(), 1, atol=1e-1), "Age_Scaled std should be ~1."

def test_task_3():
    """Validates Interaction Features"""
    main = sys.modules.get('__main__')
    if not main: return
    
    assert 'Spend_Per_Year' in main.df.columns, "Column 'Spend_Per_Year' not found."
    expected = main.df['Total_Spend'] / main.df['Years_Member']
    pd.testing.assert_series_equal(main.df['Spend_Per_Year'], expected, check_names=False)

def test_task_4():
    """Validates Binning"""
    main = sys.modules.get('__main__')
    if not main: return
    
    assert 'Age_Group' in main.df.columns, "Column 'Age_Group' not found."
    # Check if it's categorical/object
    assert main.df['Age_Group'].dtype.name in ['category', 'object'], "Age_Group should be a category or object."
    # Check if 4 bins were created
    assert len(main.df['Age_Group'].unique()) >= 3, "Not enough bins detected in Age_Group."

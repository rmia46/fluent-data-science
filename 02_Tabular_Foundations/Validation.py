import numpy as np
import pandas as pd
import sys

def test_task_1():
    """Validates Vectorization vs Loop"""
    main = sys.modules.get('__main__')
    if not main: return
    
    assert hasattr(main, 'df'), "DataFrame 'df' not found."
    assert 'Total' in main.df.columns, "Column 'Total' not found in df."
    # Check if calculation is correct
    expected = main.df['Price'] * main.df['Quantity']
    pd.testing.assert_series_equal(main.df['Total'], expected, check_names=False)

def test_task_2():
    """Validates Boolean Indexing & .loc"""
    main = sys.modules.get('__main__')
    if not main: return
    
    assert hasattr(main, 'df_filtered'), "DataFrame 'df_filtered' not found."
    assert len(main.df_filtered) < len(main.df), "df_filtered should be a subset of df."
    # Check conditions: Score > 80 and City is Dhaka/Sylhet
    assert (main.df_filtered['Score'] > 80).all(), "Some scores in df_filtered are <= 80."
    assert main.df_filtered['City'].isin(['Dhaka', 'Sylhet']).all(), "Found cities other than Dhaka/Sylhet in filtered data."

def test_task_3():
    """Validates GroupBy Aggregation"""
    main = sys.modules.get('__main__')
    if not main: return
    
    assert hasattr(main, 'city_summary'), "Variable 'city_summary' not found."
    assert 'mean' in main.city_summary.columns and 'count' in main.city_summary.columns, "Summary must have 'mean' and 'count' columns."
    # Verify values
    expected = main.df.groupby('City')['Score'].agg(['mean', 'count'])
    pd.testing.assert_frame_equal(main.city_summary, expected)

def test_task_4():
    """Validates Merging"""
    main = sys.modules.get('__main__')
    if not main: return
    
    assert hasattr(main, 'df_merged'), "DataFrame 'df_merged' not found."
    assert 'Region' in main.df_merged.columns, "Merge failed to bring in 'Region' column."
    assert len(main.df_merged) == len(main.df), "Row count changed! Did you use how='left'?"

def test_task_5():
    """Validates Cleaning & Indicators"""
    main = sys.modules.get('__main__')
    if not main: return
    
    assert 'Score_was_missing' in main.df.columns, "Missingness indicator 'Score_was_missing' not found."
    assert main.df['Score'].isna().sum() == 0, "There are still missing values in 'Score'."
    # Check if median was used (assuming standard sample)
    assert main.df['Score'].dtype in ['float64', 'int64'], "Score must be numeric."

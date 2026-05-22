import numpy as np
import sys

def test_task_1():
    """Validates Task 1: Matrix Dot Product and Element-wise Product"""
    main = sys.modules.get('__main__')
    if not main: return
    
    # Check if variables exist
    for var in ['A', 'B', 'dot_product', 'element_wise']:
        assert hasattr(main, var), f"Variable '{var}' not found. Please ensure you name your variables exactly as requested."
    
    A, B = main.A, main.B
    # Assertions
    assert A.shape == (3, 3), f"Matrix A should be 3x3, but got {A.shape}"
    assert B.shape == (3, 3), f"Matrix B should be 3x3, but got {B.shape}"
    np.testing.assert_allclose(main.dot_product, np.dot(A, B), err_msg="Dot product calculation is incorrect.")
    np.testing.assert_allclose(main.element_wise, A * B, err_msg="Element-wise product calculation is incorrect.")

def test_task_2():
    """Validates Task 2: Solving System of Linear Equations"""
    main = sys.modules.get('__main__')
    if not main: return
    
    assert hasattr(main, 'solution'), "Variable 'solution' not found."
    x_sol, y_sol = main.solution
    
    # 2x + y = 5
    # x - 3y = -1
    assert np.isclose(2*x_sol + y_sol, 5), "The solution does not satisfy the first equation (2x + y = 5)."
    assert np.isclose(x_sol - 3*y_sol, -1), "The solution does not satisfy the second equation (x - 3y = -1)."

def test_task_3():
    """Validates Task 3: Gradient Descent Optimization"""
    main = sys.modules.get('__main__')
    if not main: return
    
    assert hasattr(main, 'x'), "Variable 'x' (final position) not found."
    # f(x) = x^2 - 4x + 4, min at x=2
    assert np.isclose(main.x, 2.0, atol=1e-1), f"Gradient descent did not converge to the minimum. Expected ~2.0, got {main.x:.4f}"

def test_task_4():
    """Validates Task 4: Statistics and Distributions"""
    main = sys.modules.get('__main__')
    if not main: return
    
    for var in ['samples', 'mean', 'median', 'variance']:
        assert hasattr(main, var), f"Variable '{var}' not found."
    
    samples = main.samples
    assert len(samples) == 1000, f"Expected 1000 samples, but got {len(samples)}"
    
    np.testing.assert_allclose(main.mean, np.mean(samples), err_msg="Mean calculation is incorrect.")
    np.testing.assert_allclose(main.median, np.median(samples), err_msg="Median calculation is incorrect.")
    np.testing.assert_allclose(main.variance, np.var(samples), err_msg="Variance calculation is incorrect.")

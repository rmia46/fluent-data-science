import re

with open('plan.htm', 'r') as f:
    content = f.read()

# Update span
content = content.replace('7 Days + 1 Mock Day', '8 Days + 1 Mock Day')
content = content.replace('Section 1: The 7-Day Hyper-Drive Plan', 'Section 1: The 8-Day Hyper-Drive Plan')
content = content.replace('Section 2: Day 8 — The 4-Hour Custom Mock Competition', 'Section 2: Day 9 — The 4-Hour Custom Mock Competition')

# Shift days 1 to 7 -> 2 to 8
for i in range(7, 0, -1):
    content = content.replace(f'Day {i}:', f'Day {i+1}:')

# Insert Day 1 (Math)
math_day_html = """
        <div class="day-card">
            <div class="day-header">
                <span>Day 1: Mathematics for Machine Learning & Data Science</span>
            </div>
            <div class="day-body">
                <div class="session-grid">
                    <div class="session-box">
                        <h4>Session 1: Linear Algebra Foundations</h4>
                        <div class="session-component"><strong>Lecture</strong><p>Vectors, matrices, dot products, and matrix multiplication. Understanding dimensions and shapes in datasets.</p></div>
                        <div class="session-component practice"><strong>Practice</strong><p>Implement matrix operations using NumPy and solve a basic system of linear equations.</p></div>
                    </div>
                    <div class="session-box">
                        <h4>Session 2: Calculus & Gradient Descent</h4>
                        <div class="session-component"><strong>Lecture</strong><p>Derivatives, partial derivatives, and the chain rule. Intuition behind Gradient Descent optimization.</p></div>
                        <div class="session-component practice"><strong>Practice</strong><p>Write a simple gradient descent loop from scratch to minimize a basic cost function.</p></div>
                    </div>
                    <div class="session-box">
                        <h4>Session 3: Probability & Statistics</h4>
                        <div class="session-component"><strong>Lecture</strong><p>Distributions (Normal, Binomial), expectation, variance, and Bayes' Theorem. Hypothesis testing intuition.</p></div>
                        <div class="session-component practice"><strong>Practice</strong><p>Simulate distributions, calculate z-scores, and write a function to apply Bayes' theorem to a medical dataset.</p></div>
                    </div>
                </div>
            </div>
        </div>
"""

content = content.replace('<h2>Section 1: The 8-Day Hyper-Drive Plan</h2>', '<h2>Section 1: The 8-Day Hyper-Drive Plan</h2>\n' + math_day_html)

with open('plan.htm', 'w') as f:
    f.write(content)

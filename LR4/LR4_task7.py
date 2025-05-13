import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial.polynomial import Polynomial
from sklearn.linear_model import LinearRegression

# Experimental data
X = np.array([-5, -4, 0, 1, 3, 5])
Y = np.array([5.3, 20.7, 21.7, 9.2, 55.4, 64.3])

# Reshape for sklearn LinearRegression
X_reshaped = X.reshape(-1, 1)

# Apply Least Squares Method (Linear Regression)
model = LinearRegression()
model.fit(X_reshaped, Y)

# Get parameters
slope = model.coef_[0]
intercept = model.intercept_

# Generate approximating function
X_fit = np.linspace(min(X), max(X), 100)
Y_fit = model.predict(X_fit.reshape(-1, 1))

# Plotting
plt.figure(figsize=(8, 5))
plt.scatter(X, Y, color='red', label='Experimental points')
plt.plot(X_fit, Y_fit, label=f'Approximation: Y = {intercept:.2f} + {slope:.2f}X')
plt.title('Least Squares Approximation')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

(intercept, slope)

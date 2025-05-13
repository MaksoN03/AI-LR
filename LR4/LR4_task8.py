import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial import Polynomial

# Given data
x = np.array([0.1, 0.3, 0.4, 0.6, 0.7])
y = np.array([3.2, 3.0, 1.0, 1.8, 1.9])

# 1. Create Vandermonde matrix for polynomial of degree 4
X_matrix = np.vander(x, N=5, increasing=True)

# 2. Solve for polynomial coefficients
coefficients = np.linalg.solve(X_matrix, y)

# 3. Define the polynomial function
p = Polynomial(coefficients)

# 4. Plotting
x_plot = np.linspace(0.05, 0.75, 300)
y_plot = p(x_plot)

plt.figure(figsize=(8, 5))
plt.plot(x_plot, y_plot, label='Interpolating Polynomial', color='blue')
plt.scatter(x, y, color='red', label='Data points')
plt.title("Polynomial Interpolation (degree 4)")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# 5. Compute values at intermediate points
y_02 = p(0.2)
y_05 = p(0.5)

(coefficients, y_02, y_05)
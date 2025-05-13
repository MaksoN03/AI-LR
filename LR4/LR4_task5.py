import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# Налаштування генерації (фіксований seed для стабільності)
np.random.seed(13)

# Задання параметрів варіанту 5
m = 100
X = 6 * np.random.rand(m, 1) - 3
y = 0.4 * X ** 2 + X + 4 + np.random.randn(m, 1)

# Побудова графіка початкових даних
plt.figure(figsize=(10, 6))
plt.scatter(X, y, color='blue', label='Випадкові дані')

# Лінійна регресія
lin_reg = LinearRegression()
lin_reg.fit(X, y)
y_lin_pred = lin_reg.predict(X)

# Побудова лінійної регресії
plt.plot(X, y_lin_pred, color='red', label='Лінійна регресія')

# Поліноміальна регресія ступеня 2
poly_features = PolynomialFeatures(degree=2, include_bias=False)
X_poly = poly_features.fit_transform(X)

# Показати, як виглядає X[0] і X_poly[0]
print("X[0]:", X[0])
print("X_poly[0]:", X_poly[0])

# Модель для поліноміальної регресії
poly_reg = LinearRegression()
poly_reg.fit(X_poly, y)
y_poly_pred = poly_reg.predict(X_poly)

# Побудова поліноміальної регресії
# Для згладженої лінії:
X_new = np.linspace(X.min(), X.max(), 200).reshape(200, 1)
X_new_poly = poly_features.transform(X_new)
y_new_poly = poly_reg.predict(X_new_poly)
plt.plot(X_new, y_new_poly, color='green', label='Поліноміальна регресія (ступінь 2)')

# Графік
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.title('Порівняння лінійної та поліноміальної регресії')
plt.grid(True)
plt.tight_layout()
plt.show()

# Виведення коефіцієнтів поліноміальної моделі
print("\nПоліноміальна регресійна модель:")
print("Інтерсепт (вільний член):", poly_reg.intercept_)
print("Коефіцієнти:", poly_reg.coef_)


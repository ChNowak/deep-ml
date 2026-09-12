import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
	# X.T @ X @ b = X.T @ y
	# b = (X.T @ X).inv @ X.T @ y
	X = np.array(X)
	y = np.array(y)
	return np.linalg.inv(X.T@X) @ X.T @ y
	
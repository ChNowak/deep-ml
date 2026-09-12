import numpy as np
def solve_jacobi(A: np.ndarray, b: np.ndarray, n: int) -> list:
	# Ax = b
	# Dx + Rx = b
	# x = D.inv(b - Rx)
	# x[k+1] = D.inv(b-Rx[k])
	shape_a = np.shape(A)[0]
	I = np.eye(shape_a)
	D = A*I
	D_inv = np.linalg.inv(D)
	R = A-D
	x = np.zeros(shape_a)
	for k in range(n):
		x = D_inv@(b-R@x)
	return x
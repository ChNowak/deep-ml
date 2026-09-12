import numpy as np
def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
	v_arr = np.array(vectors)
	return np.cov(v_arr)
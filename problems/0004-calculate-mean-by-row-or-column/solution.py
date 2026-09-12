import numpy as np

def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	m_arr = np.array(matrix)
	if mode == "row":
		return np.mean(m_arr, axis=1)
	if mode == "column":
		return np.mean(m_arr, axis=0)
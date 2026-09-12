import numpy as np
def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	m_arr = np.array(matrix)
	eigenvalues = np.linalg.eigvals(m_arr)
	return eigenvalues
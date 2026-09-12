import numpy as np
def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	m_arr = np.array(matrix)
	return m_arr * scalar
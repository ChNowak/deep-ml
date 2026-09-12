import numpy as np
def determinant_4x4(matrix: list[list[int|float]]) -> float:
	m_arr = np.array(matrix)
	m_shape = np.shape(m_arr)[0]
	if m_shape == 2:
		a = m_arr[0,0]
		b = m_arr[0,1]
		c = m_arr[1,0]
		d = m_arr[1,1]
		return (a*d - b*c)
	det = 0
	for i in range(m_shape):
		op_matrix = m_arr[1:]
		op_matrix = np.delete(op_matrix, i, axis=1)
		det += m_arr[0,i] * determinant_4x4(op_matrix) * (-2*(i%2)+1)
	return det
import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:
	a_arr = np.array(A)
	t_arr = np.array(T)
	s_arr = np.array(S)
	try:
		t_inv = np.linalg.inv(T)
		np.linalg.inv(S)
	except:
		return -1
	return t_inv@a_arr@s_arr
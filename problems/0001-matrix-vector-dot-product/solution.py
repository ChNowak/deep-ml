def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	try:
		import numpy as np
		a_arr = np.array(a)
		b_arr = np.array(b)
		dot = a_arr@b_arr
		return dot
	except:
		return -1
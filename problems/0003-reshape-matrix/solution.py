import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
	try:
		a_arr = np.array(a)
		reshaped_matrix = np.reshape(a_arr, new_shape)
		return reshaped_matrix
	except:
		return []
import numpy as np

def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
              a_arr = np.array(a)
              b_arr = np.array(b)
              try:
                return a_arr@b_arr
              except:
                return -1
###############
# Authored by Weisheng Jiang
# Book 4  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############

# Bk4_Ch4_08.py

import numpy as np

from numpy.linalg import matrix_power as pw

A = np.array([[1.0, 2.0], [3.0, 4.0]])
print(A)

# matrix inverse
A_3 = pw(A, 3)
print(A_3)
A_3_v3 = A @ A @ A
print(A_3_v3)

# piecewise power
A_3_piecewise = A**3

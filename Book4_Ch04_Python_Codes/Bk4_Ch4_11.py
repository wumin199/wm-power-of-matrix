###############
# Authored by Weisheng Jiang
# Book 4  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############

# Bk4_Ch4_11.py

import numpy as np
from numpy.linalg import inv

A = np.array([[1.0, 2.0], [3.0, 4.0]])

# matrix inverse
A_inverse = inv(A)
A_times_A_inv = A @ A_inverse

print(A)
print(A_inverse)
print(A_times_A_inv)

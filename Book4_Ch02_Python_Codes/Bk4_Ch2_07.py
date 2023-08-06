###############
# Authored by Weisheng Jiang
# Book 4  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############

# Bk4_Ch2_07.py

import numpy as np

a = np.array([[2, 3], [3, 4]])
print(a)
b = np.array([[3, 4], [5, 6]])
print(b)

res = np.dot(a, b)
print(res)


res = a @ b
print(res)

# a_@_b = np.dot(a,b)
# # a@b

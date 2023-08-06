###############
# Authored by Weisheng Jiang
# Book 4  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############

# Bk4_Ch2_10.py

from scipy.spatial import distance
from sklearn import datasets
import numpy as np

# import the iris data
iris = datasets.load_iris()

print("iris: \n{}".format(iris))
print("type: {}".format(type(iris)))
# print("iris.data: \n{}".format(iris.data))

# Only use the first two features: sepal length, sepal width
X = iris.data[:, :]
print("X: {}".format(X))
print("type(X): {}".format(type(X)))
# Extract 4 data points
x1_data = X[0, :]
print("x1_data = {}".format(x1_data))
x2_data = X[1, :]
x51_data = X[50, :]
x101_data = X[100, :]

# calculate cosine distance
x1_x2_cos_dist = distance.cosine(x1_data, x2_data)
x1_norm = np.linalg.norm(x1_data)
x2_norm = np.linalg.norm(x2_data)
x1_dot_x2 = x1_data.T @ x2_data
x1_x2_cos = x1_dot_x2 / x1_norm / x2_norm


x1_x51_cos_dist = distance.cosine(x1_data, x51_data)

x1_x101_cos_dist = distance.cosine(x1_data, x101_data)

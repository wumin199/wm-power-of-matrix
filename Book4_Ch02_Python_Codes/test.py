import numpy as np
import matplotlib.pyplot as plt

# 创建示例数据
x = np.arange(-2, 3)
y = np.arange(-2, 3)
print("x = ", x)
print("y = ", y)

X, Y = np.meshgrid(x, y)
U = X
V = Y
print("X = {}".format(X))
print("Y = {}".format(Y))
print("U = {}".format(U))
print("V = {}".format(V))

# 绘制矢量场图
# plt.quiver(X, Y, U, V, angles="xy", scale_units="xy")
plt.quiver(X, Y, X, Y, angles="xy", scale_units="xy")

# 设置坐标轴范围
plt.xlim(-3, 3)
plt.ylim(-3, 3)

# 显示图形
plt.show()

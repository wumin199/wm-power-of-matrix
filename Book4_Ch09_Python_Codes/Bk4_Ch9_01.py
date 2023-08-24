###############
# Authored by Weisheng Jiang
# Book 4  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############

# Bk4_Ch9_01.py

import numpy as np
import matplotlib.pyplot as plt

thetas = np.linspace(0, np.pi, 25)

x = np.array([[4], [3]])

fig, axes = plt.subplots()

for theta in thetas:
    v = np.array([[np.cos(theta)], [np.sin(theta)]])

    proj = v.T @ x
    print(proj)

    # 将一条从点 (-v[0] * 6, -v[1] * 6) 到点 (v[0] * 6, v[1] * 6) 的折线绘制在图形上
    # plot([x1, x2], [y1, y2]) -> (x1,y1) -> (x2, y2)
    plt.plot([-v[0] * 6, v[0] * 6], [-v[1] * 6, v[1] * 6])  # 使用plot绘制直线， 绘制空间均匀的线条
    # 绘制垂直线， 如果其中一个是单位向量，则proj_v(x) = <x,v>*v
    plt.plot([x[0], v[0] * proj], [x[1], v[1] * proj], color="k")
    # 如果plot只有一个点，则绘制的是marker，这里就是投影点
    plt.plot(v[0] * proj, v[1] * proj, color="r", marker="x")

    # 绘制箭头
    plt.quiver(0, 0, v[0], v[1], angles="xy", scale_units="xy", scale=1)

plt.plot(x[0], x[1], marker="x", color="r")
plt.axis("scaled")
plt.show()

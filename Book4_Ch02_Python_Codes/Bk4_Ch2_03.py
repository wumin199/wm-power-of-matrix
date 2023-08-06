###############
# Authored by Weisheng Jiang
# Book 4  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############

# Bk4_Ch1_03.py

import matplotlib.pyplot as plt
import numpy as np

x1 = np.linspace(-10, 10, num=201)
x2 = x1

xx1, xx2 = np.meshgrid(x1, x2)
p = 2
zz = ((np.abs((xx1)) ** p) + (np.abs((xx2)) ** p)) ** (1.0 / p)

fig, ax = plt.subplots(figsize=(12, 12))

ax.contour(xx1, xx2, zz, levels=np.arange(11), cmap="RdYlBu_r")

ax.axhline(y=0, color="k", linewidth=0.25)
ax.axvline(x=0, color="k", linewidth=0.25)
ax.set_xlim(-12, 12)
ax.set_ylim(-12, 12)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["bottom"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.set_xlabel("$x_1$")
ax.set_ylabel("$x_2$")

# "equal" 是 set_aspect() 方法的第一个参数，表示将纵横比例设置为相等，即使图像被拉伸或压缩也保持一致。
# "box" 是 set_aspect() 方法的第二个参数，表示保持数据的纵横比例不变，但允许图像的边界被改变以适应图形容器的大小。
ax.set_aspect("equal", adjustable="box")
plt.show()

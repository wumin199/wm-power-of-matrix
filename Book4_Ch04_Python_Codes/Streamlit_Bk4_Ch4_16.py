###############
# Authored by Weisheng Jiang
# Book 4  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############

import plotly.graph_objects as go
import numpy as np
from plotly.subplots import make_subplots
import streamlit as st


def bmatrix(a):
    """Returns a LaTeX bmatrix

    :a: numpy array
    :returns: LaTeX bmatrix as a string
    """
    if len(a.shape) > 2:
        raise ValueError("bmatrix can at most display two dimensions")
    lines = str(a).replace("[", "").replace("]", "").splitlines()
    rv = [r"\begin{bmatrix}"]
    rv += ["  " + " & ".join(l.split()) + r"\\" for l in lines]
    rv += [r"\end{bmatrix}"]
    return "\n".join(rv)


n = m = 20

# 最后，通过 fig.add_trace 函数将一个 Scatter 类型的图表对象添加到子图布局的第一个子图中。
#
# 该 Scatter 图表对象的 x 坐标使用 xv 列表，y 坐标使用 yv 列表。图表对象的 mode 设置为 "lines" 表示要绘制连续的线段，线宽使用变量 lw 指定，线的颜色设置为红色。

# 这段代码的目的是使用 Plotly 库中的 make_subplots 函数创建一个具有 1 行 2 列的子图布局，然后在第一个子图中绘制一条以 xv 和 yv 列表为数据点坐标的红色线段。
#
# 通过在数据点序列中使用 NaN 值来分隔不同的曲线段或路径段。

fig = make_subplots(rows=1, cols=2, horizontal_spacing=0.035)

xv = []
yv = []

for k in range(-n, n + 1):
    # 生成的数据点序列中的 NaN 值可以用来分隔不同的曲线段或路径段
    xv.extend([k, k, np.nan])
    yv.extend([-m, m, np.nan])

# print("xv: ", xv)
# print("yv: ", yv)

lw = 1  # line_width


# go.Scatter 是 Plotly 库中的一个函数，用于创建 Scatter 类型的图表对象。

# Scatter 类型图表对象用于绘制散点图、线图或线段等可视化图形。可以通过指定不同的模式（mode）参数来控制 Scatter 图表对象的绘制方式。

fig.add_trace(
    # 有n个点，每个点的坐标是(xv[n], yv[n])，然后每个点都连线起来，如果一个点是[np.nan, np.nan]，则和前后点不连起来
    go.Scatter(x=xv, y=yv, mode="lines", line_width=lw, line_color="red"),
    1,
    1,
)
# set up  the lists  of  horizontal line x and y-end coordinates


xh = []
yh = []
for k in range(-m, m + 1):
    xh.extend([-m, m, np.nan])
    yh.extend([k, k, np.nan])
    fig.add_trace(
        go.Scatter(x=xh, y=yh, mode="lines", line_width=lw, line_color="blue"), 1, 1
    )


with st.sidebar:
    st.latex(
        r"""
             A = \begin{bmatrix}
    a & b\\
    c & d
    \end{bmatrix}"""
    )

    a = st.slider("a", -2.0, 2.0, step=0.1, value=1.0)
    b = st.slider("b", -2.0, 2.0, step=0.1, value=0.0)
    c = st.slider("c", -2.0, 2.0, step=0.1, value=0.0)
    d = st.slider("c", -2.0, 2.0, step=0.1, value=1.0)


theta = np.pi / 6
A = np.array([[a, b], [c, d]], dtype=float)

# get only the coordinates from -3 to 3
# X = np.array(xv[6:-6])
# Y = np.array(yv[6:-6])

print("---")

print("xv: ", xv)
print("yv: ", yv)

X = np.array(xv)
Y = np.array(yv)

# np.stack((X, Y))是垂直方向的网格线
# Txvyv就是被A变换过的新的网格线

# transform by T the vector of coordinates [x, y]^T where the vector runs over the columns of np.stack((X, Y))
Txvyv = A @ np.stack((X, Y))  # transform by T the vertical lines


print("Txvyv: ", Txvyv)

# X = np.array(xh[6:-6])
# Y = np.array(yh[6:-6])


X = np.array(xh)
Y = np.array(yh)

Txhyh = A @ np.stack((X, Y))  # #transform by T the horizontal lines

# np.stack((X, Y))是水平方向的网格线
# Txhyh就是被A变换过的新的网格线


st.latex(r"A = " + bmatrix(A))

a1 = A[:, 0].reshape((-1, 1))
a2 = A[:, 1].reshape((-1, 1))

st.latex(
    r"""
         a_1 = Ae_1 = """
    + bmatrix(A)
    + "e_1 = "
    + bmatrix(a1)
)

st.latex(
    r"""
         a_2 = Ae_2 = """
    + bmatrix(A)
    + "e_2 = "
    + bmatrix(a2)
)


st.latex(r"\begin{vmatrix} A \end{vmatrix} = " + str(np.linalg.det(A)))
square_x = np.array([0, 1, 1, 0])
square_y = np.array([0, 0, 1, 1])
square_array = np.stack((square_x, square_y))

fig.add_trace(
    go.Scatter(x=square_x, y=square_y, fill="toself", line_color="orange"), 1, 1
)


A_times_square_array = A @ square_array

fig.add_trace(
    go.Scatter(
        x=A_times_square_array[0, :],
        y=A_times_square_array[1, :],
        fill="toself",
        line_color="orange",
    ),
    1,
    2,
)

# 行和列都重绘，都画在第一行第二列

fig.add_trace(
    go.Scatter(x=Txvyv[0], y=Txvyv[1], mode="lines", line_width=lw, line_color="red"),
    1,
    2,
)

fig.add_trace(
    go.Scatter(x=Txhyh[0], y=Txhyh[1], mode="lines", line_width=lw, line_color="blue"),
    1,
    2,
)

fig.update_xaxes(range=[-4, 4])
fig.update_yaxes(range=[-4, 4])
fig.update_layout(
    width=800,
    height=500,
    showlegend=False,
    template="none",
    plot_bgcolor="white",
    yaxis2_showgrid=False,
    xaxis2_showgrid=False,
)

st.plotly_chart(fig)

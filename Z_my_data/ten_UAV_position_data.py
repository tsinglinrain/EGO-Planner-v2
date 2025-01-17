# 观察十个坐标的位置

import matplotlib.pyplot as plt
import numpy as np

# 读取数据
data = np.array([[-3.18E-05, -12], [-7.053443637, -9.708188959], 
                 [-11.4126841, -3.708185762], [-11.41267426, 3.708216046], 
                 [-7.053417875, 9.708207676], [0, 12], 
                 [7.053417875, 9.708207676], [11.41267426, 3.708216046], 
                 [11.4126841, -3.708185762], [7.053443637, -9.708188959]])
theta = np.linspace(0, 2*np.pi, 60)
x_r2 = 12*np.cos(theta)
y_r2 = 12*np.sin(theta)


# 画图
fig, ax = plt.subplots(figsize=(7, 7))
ax.scatter(data[:, 0], data[:, 1], s=100, c='r', marker='o')

ax.plot(x_r2, y_r2, color="magenta", label='circle', linewidth=1)

ax.plot(data[0, 0], data[0, 1], color="yellow", label='circle', marker='o')

# set axis,  把坐标轴移动到中心，并且右，上的两个轴不可见
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['left'].set_position(('data', 0)) # data方便一些
ax.spines['bottom'].set_position(('data', 0))

# set label
ax.set_xlabel('x', loc='right', fontsize=14)  # Add an x-label to the axes.
ax.set_ylabel('y', loc='top', fontsize=14)  # Add a y-label to the axes.
ax.set_title("Distribution map of ten UAVs", fontstyle="italic")  # Add a title to the axes.


ax.grid()   # 感觉好看一些就加了

# plt.savefig('circle_exchange_ten') # 需要保存的时候再反注释，否则编译慢

plt.show()
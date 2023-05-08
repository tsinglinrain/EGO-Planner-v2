# 画一个散点图，又是个坐标

import matplotlib.pyplot as plt
import numpy as np

# 生成数据
alpha = np.array([0, 60, 120, 180, 240, 300]) * np.pi / 180
for i in range(6):
    alpha[i] = alpha[i] + np.pi / 6
data = np.zeros((6, 2))
for i in range(6):
    data[i, 0] = 10 * np.cos(alpha[i])
    data[i, 1] = 10 * np.sin(alpha[i])

# 将data写入文件,保留10位小数

np.savetxt('circle_exchange_six_data.txt', data, fmt='%.14f', delimiter=' ')

# 生成圆的数据
theta = np.linspace(0, 2*np.pi, 60) # 有点误差，画出多出一点点，减去0.15作为修正
x_r2 = 10*np.cos(theta)
y_r2 = 10*np.sin(theta)    # \varphi 的圆弧


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

ax.grid()

# plt.savefig('circle_exchange_six') # 需要保存的时候再反注释，否则编译慢

plt.show()
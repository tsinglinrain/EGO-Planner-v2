# six_UAV_position_data

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
# np.savetxt('circle_exchange_six_data.txt', data, fmt='%.14f', delimiter=' ')

# 生成圆的数据
theta = np.linspace(0, 2*np.pi, 60) 
x_r2 = 10*np.cos(theta)
y_r2 = 10*np.sin(theta)


# 画图
fig, ax = plt.subplots(figsize=(7, 7))
ax.scatter(data[:, 0], data[:, 1], color='red',label='AUV', marker='o', s=100)
ax.plot(x_r2, y_r2, color="blue", label='Circle', linewidth=1)
ax.plot([data[0, 0],data[3, 0]], [data[0, 1],data[3, 1]], color="magenta", linewidth=2)
ax.plot([data[1, 0],data[4, 0]], [data[1, 1],data[4, 1]], color="magenta", linewidth=2.5)
ax.plot([data[2, 0],data[5, 0]], [data[2, 1],data[5, 1]], color="magenta", label='Trajectory', linewidth=2)
# ax.plot(data[0, 0], data[0, 1], color="yellow", label='AUV', marker='o')

ax.text(-1.3, -1.3, 'O', fontsize=14, fontstyle='italic')
ax.text(data[0, 0]+0.2, data[0, 1]+0.2, 'AUV1', fontsize=14, fontstyle='italic')
ax.text(data[1, 0]+0.2, data[1, 1]+0.2, 'AUV2', fontsize=14, fontstyle='italic')
ax.text(data[2, 0]+0.3, data[2, 1]+0.2, 'AUV3', fontsize=14, fontstyle='italic')
ax.text(data[3, 0]+0.2, data[3, 1]+0.2, 'AUV4', fontsize=14, fontstyle='italic')
ax.text(data[4, 0]+0.2, data[4, 1]+0.5, 'AUV5', fontsize=14, fontstyle='italic')
ax.text(data[5, 0]+0.3, data[5, 1]+0.2, 'AUV6', fontsize=14, fontstyle='italic')

# set axis,  把坐标轴移动到中心，并且右，上的两个轴不可见
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['left'].set_position(('data', 0)) # data方便一些
ax.spines['bottom'].set_position(('data', 0))

# set label
ax.set_xlabel('x', loc='right', fontsize=14)  # Add an x-label to the axes.
ax.set_ylabel('y', loc='top', fontsize=14)  # Add a y-label to the axes.
ax.set_title("Distribution map of ten UAVs", fontstyle="italic")  # Add a title to the axes.

ax.set_xlim(-10.8, 10.8)
ax.set_ylim(-10.8, 10.8)


ax.grid()
ax.legend(loc='upper left');  # Add a legend.默认放置再中间，感觉不right啊

plt.savefig('circle_exchange_six') # 需要保存的时候再反注释，否则编译慢

plt.show()
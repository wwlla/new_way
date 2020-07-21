import matplotlib.pyplot as plt
import numpy as np


# # 散点图
n = 1024
# # 正态分布 参数：均值 差值 点个数
X = np.random.normal(0, 1, n)
Y = np.random.normal(0, 1, n)
T = np.arctan2(X, Y)
print(T)
# 绘制点状图
plt.scatter(X, Y)

# 清除纵横轴显示
plt.xticks(())
plt.yticks(())

plt.show()
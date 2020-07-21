import matplotlib.pyplot as plt
import numpy as np
import matplotlib

def get_height(x, y):
# np.exp(e) 求e幂次方
    return (1-x/2+x**5+y**3)*np.exp(-x**2-y**2)

n = 256
x = np.linspace(-3, 3, n)
y = np.linspace(-3, 3, n)
# np.meshgrid 生成网格点坐标矩阵
X, Y = np.meshgrid(x, y)

plt.figure(figsize=(14, 8))
# 参数： 横坐标 纵坐标 高度 等高分层数量 透明度 cmap是颜色对应表 等高线的填充颜色
plt.contourf(X, Y, get_height(X, Y), 16, alpah=0.7, cmap=plt.cm.hot )

#等高线的线
C = plt.contour(X,Y, get_height(X, Y), 16, color='black', linewidth=.5)

# 增加标签
plt.clabel(C, inline=True, fontsize=16)

# 删除 坐标轴
plt.xticks(())
plt.yticks(())

plt.show()
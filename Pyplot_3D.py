import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import  Axes3D
import PySimpleGUI as sg
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# 正常显示中文
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号


fig = plt.figure(figsize=(6, 4))
ax = Axes3D(fig)

X = np.arange(-4, 4, 0.25)  # 等差数列
Y = np.arange(-4, 4, 0.25)   # 等差数列
X,Y = np.meshgrid(X, Y)   # 网格矩阵
R = np.sqrt(X**2+Y**2)  # 计算平方根

# 高值
Z = np.sin(R)

# 绘 图
ax.plot_surface(X, Y, Z,
                rstride=1,  # 行的跨度
                cstride=1,  # 列的跨度
                cmap=plt.get_cmap('rainbow') # 颜色映射样式设置
                )

# offset 表示距离zdir的轴距离
ax.contour(X, Y, Z, zdir='z', offset=-2, cmap='rainbow')
ax.set_zlim(-2,2)


# plt.show()



# matplotlib助手代码
# FigureCanvasXAgg就是一个渲染器，渲染器的工作就是drawing，执行绘图的这个动作。
def draw_figure(canvas, figure, loc=(0, 0)):
    figure_canvas_agg = FigureCanvasTkAgg(figure,canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg


# GUI代码
sg.theme('Light Brown 3')
# fig1 =plt.gcf() # 获取figure
# 获取figure 长宽 及坐标
figure_x, figure_y, figure_w, figure_h = fig.bbox.bounds

# 画图
layout = [
    [sg.Text('动画图例', font='仿宋, 20', pad=((figure_w/2, 0), 3))],
    [sg.Canvas(size=(figure_w, figure_h), key='-CANVAS-'), sg.Canvas(size=(figure_w, figure_h), key='-CANVAS1-')],

    [sg.Button('关闭窗口')]

]
window = sg.Window('动画', layout, force_toplevel=True, finalize=True, grab_anywhere=True)

draw_figure(window['-CANVAS-'].TKCanvas, fig)
draw_figure(window['-CANVAS1-'].TKCanvas, fig)
event, values =window.read()
window.close()
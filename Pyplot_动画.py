import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation
import PySimpleGUI as sg
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# 正常显示中文
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号


# -----Animation 动画------

# 返回一个包含figure和axes对象的元组
# 类似于: fig =plt.figure()   fig.add_subplot(111)
fig, ax = plt.subplots()

# pi 为圆周率
x = np.arange(0, 2*np.pi, 0.01)

# 这里只需要别表的第一个元素，所以就用逗号加空白的形式省略了列表后边的元素
line, = ax.plot(x, np.sin(x))


def animate(i):
    line.set_ydata(np.sin(x+i/100))
    return line,


def init():
    line.set_ydata(np.sin(x))
    # 这里由于仅仅需要列表的第一个参数，所以后边的就直接用空白省略了
    return line,


ani = animation.FuncAnimation(fig=fig,
                              func=animate,  # 动画函数
                              frames=1000,  # 帧数 ,连续动画的帧数
                              init_func=init,  # 初始化函数
                              interval=20,  # 20ms   每帧之间的变化时差
                              blit=True)

# 取消显示，在GUI中显示
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
fig1 =plt.gcf() # 获取figure
# 获取figure 长宽 及坐标
figure_x, figure_y, figure_w, figure_h = fig.bbox.bounds

# 画图
layout = [
    [sg.Text('动画图例', font='仿宋, 20', pad=((figure_w/2, 0), 3))],
    [sg.Canvas(size=(figure_w, figure_h), key='-CANVAS-')],
    [sg.Button('关闭窗口')]

]
window = sg.Window('动画', layout, force_toplevel=True, finalize=True, grab_anywhere=True)

draw_figure(window['-CANVAS-'].TKCanvas, fig1)
event, values =window.read()
window.close()


import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import PySimpleGUI as sg
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# 正常显示中文
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

x = np.linspace(-1, 1, 50)
# print(x)
y1 = 2*x + 1
y2 = 2**x + 1
# figure1 显示
# plt.figure()
# plt.plot(x, y1)
#
# plt.xlabel('X 轴')
# plt.ylabel('Y 轴')

#缺少逗号，图例legend则无法显示
plt.figure(num=3, figsize=(9, 5))
p1, = plt.plot(x, y2)
p2, = plt.plot(x, y1, color='red', linewidth=5.0, linestyle='--', alpha=0.5) #alpha 透明度

plt.xlim((-1, 2))
plt.ylim((1, 3))

plt.xlabel('X 轴轴')
plt.ylabel('Y 轴轴')

# 设置轴上的数字及字符标识

new_ticks = np.linspace(-1, 2, 5)
plt.xticks(new_ticks)

plt.yticks([-2, -1.8, -1, 1.22, 3], [r'极差', r'差', r'一般', r'良好', r'极好'])


#获取当前轴 并去掉 顶部和右侧的边框

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# 绑定X 轴 和Y 轴

ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
# 设置轴的位置
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))

plt.legend(handles=[p1, p2], labels=['aaa', 'bbb'], loc = 'upper right')


# 显示交叉点
x0 = 1
y0 = 2*x0 + 1
#s 表示点大小
plt.scatter(x0, y0, s=66, color='b')

# 定义线的范围,画线
plt.plot([x0, x0], [y0, 0], 'k-.', lw=2.5)

# 关键位置提示信息
# xy=(横坐标，纵坐标)  箭头尖端
# xytext=(横坐标，纵坐标) 文字的坐标，指的是最左边的坐标
# arrowprops= {        facecolor= '颜色',        shrink = '数字' <1  收缩箭头
plt.annotate(r'2x+1=%s'% y0, xy=(x0, y0), xycoords='data', xytext=(30, -30),textcoords='offset points', fontsize=16
             )

#输入文字
plt.text(0, 3, '这是什么',fontdict={'size':16, 'color':'r'})

#设置lable透明度
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(12)
    label.set_bbox(dict(facecolor='y',edgecolor='None', alpha=0.7))


#要在GUI中显示，取消show显示
# plt.show()

# matplotlib助手代码
# FigureCanvasXAgg就是一个渲染器，渲染器的工作就是drawing，执行绘图的这个动作。
def draw_figure(canvas, figure, loc=(0, 0)):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both',expand=1)
    return figure_canvas_agg

#画面代码

sg.theme('Light Brown 3')
# 获取 figure
fig = plt.gcf()

# 获取figure 位置 及长宽
figure_x, figure_y, figure_w, figure_h = fig.bbox.bounds

# 画图
laout = [
    [sg.Text('Pyplot_曲线', font='宋体 18')],
    [sg.Canvas(size=(figure_w, figure_h), key='-CANVAS-')],
    [sg.OK(pad=((figure_w/2,0), 3), size=(4, 2))]
]

window = sg.Window('Pyplot_曲线', laout, force_toplevel=True,finalize=True,grab_anywhere=True)

# Pyplot引入GUI
draw_figure(window['-CANVAS-'].TKCanvas, fig)

event, values = window.read()

window.close()

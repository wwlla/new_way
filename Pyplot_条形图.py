import matplotlib.pyplot as plt
import numpy as np
import PySimpleGUI as sg
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# 正常显示中文
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

n = 12
x = np.arange(n)  # 0~11
print(x)
# np.random.uniform(0.5, 1.0, n) 生产n个 0.5~1.0中随机数
y1 = (1-x/float(n))*np.random.uniform(0.5, 1.0, n)
y2 = (1-x/float(n))*np.random.uniform(0.5, 1.0, n)

plt.figure(figsize=(6, 4))
plt.bar(x, +y1, facecolor='#9999ff', edgecolor='white')
plt.bar(x, -y2, facecolor='#ff9999', edgecolor='blue')

# zip 将 两个列表打包为元组的列表  ha 水平方向 va 垂直方向
for a, b in zip(x, y1):
    plt.text(a, b+0.05, '%.2f'% b, ha='center', va='bottom')

for a, b in zip(x, -y2):
    plt.text(a, b-0.05, '%.2f' % b, ha='center', va='top')

# 定义范围和标签
plt.xlim(-.5, n)
plt.xticks(())
plt.ylim(-1.25, 1.25)
plt.yticks(())

# 取消显示，在GUI中显示
# plt.show()

# matplotlib助手代码
# FigureCanvasXAgg就是一个渲染器，渲染器的工作就是drawing，执行绘图的这个动作。
def draw_figure(canvas, figure, loc=(0, 0)):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg

# GUI代码
sg.theme('Light Drown 3')
# 获取 figure
fig = plt.gcf()
# 获取尺寸坐标
figure_x, figure_y, figure_w, figure_h = fig.bbox.bounds

# 画图
layout = [
    [sg.Text('Pyplot_条形图',pad=((figure_w/2, 0), 3))],
    [sg.Canvas(size=(figure_w, figure_h), key='-CANVAS-')],
    [sg.Button('关闭窗口', pad=((figure_w/2, 0), 3), size=(6,2))]
]

window = sg.Window('Pyplot_条形图', layout, force_toplevel=True, finalize=True, grab_anywhere=True)

# 将plt 显示在 Canvas
fig_photo = draw_figure(window['-CANVAS-'].TKCanvas, fig)

event, values =window.read()
window.close()

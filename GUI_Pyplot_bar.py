import PySimpleGUI as sg
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import matplotlib.pyplot as plt


# 正常显示中文
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号


'''
将matplotlib图形嵌入到pysimplegui窗口中
'''


# 正常的matplotlib 代码， 但是不要plt.show()
plt.figure(figsize=(9, 6))
label=['Adventure', 'Action', 'Drama', 'Comedy', 'Thriller/Suspense', 'Horror', 'Romantic Comedy', 'Musical',
         'Documentary', 'Black Comedy', 'Western', 'Concert/Performance', 'Multiple Genres', 'Reality']
no_movies = [941, 854, 4595, 2125, 942,
             509, 548, 149, 1952, 161, 64, 61, 35, 5]

index = np.arange(len(label))
plt.bar(index, no_movies)

plt.xlabel('Genre',fontsize=10)
plt.ylabel('No of Movies', fontsize=10)

plt.xticks(index, label, fontsize=10, rotation=30)
plt.title('柱状图')

# plt.show()


# matplotlib助手代码
# FigureCanvasXAgg就是一个渲染器，渲染器的工作就是drawing，执行绘图的这个动作。
def draw_figure(canvas, figure, loc=(0, 0)):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    # 显示工具条空间？ 否则不能画面
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg

# 以下为GUI程序，将matplotlib显示到GUI里
sg.theme('Light Brown 3')

# 从plot 中获取 figure
fig = plt.gcf()
# 参数[bounds]: 形如（x0， y0， 宽， 高）的序列
figure_x, figure_y, figure_w, figure_h = fig.bbox.bounds
print(figure_x, figure_y, figure_w, figure_h)

# 画面
layout = [
    [sg.Text('Plot 测试', font='Any 18')],
    # canvas 尺寸采用figrue 的尺寸（9,6）
    [sg.Canvas(size=(figure_w, figure_h), key='-CANVAS-')],
    [sg.OK(pad=((figure_w/2, 0), 3), size=(4, 2))]
]

window = sg.Window('GUI_Pyplot测试', layout,force_toplevel=True, finalize=True, grab_anywhere=True)

# 将绘图添加到窗口
fig_photo = draw_figure(window['-CANVAS-'].TKCanvas, fig)

event, values = window.read()

window.close()


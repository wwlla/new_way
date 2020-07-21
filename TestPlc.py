#
#
# import matplotlib.pyplot as plt
# import numpy as np
# import threading
# import sys
# from random import random, randrange
# from time import sleep
#
# '''
# 绘制2x2的画板
# 可设置窗口标题和4个子图标题
# 可更新曲线数据
# '''
# quit_flag = False  # 退出标志
#
#
# class Plot2_2(object):
#     """ 2x2的画板 """
#
#     def __init__(self, wtitle='Figure', p1title='1', p2title='2', p3title='3',
#                  p4title='4'):
#         self.sub_title = [p1title, p2title, p3title, p4title]  # 4个子图的标题
#         self.fig, self.ax = plt.subplots(2, 2)  # 创建2X2子图
#         self.fig.subplots_adjust(wspace=0.3, hspace=0.3)  # 设置子图之间的间距
#         self.fig.canvas.set_window_title(wtitle)  # 设置窗口标题
#
#         # 子图字典，key为子图的序号，value为子图句柄
#         self.axdict = {0: self.ax[0, 0], 1: self.ax[0, 1], 2: self.ax[1, 0], 3: self.ax[1, 1]}
#
#     def showPlot(self):
#         """ 显示曲线 """
#         plt.show()
#
#     def setPlotStyle(self, index):
#         """ 设置子图的样式，这里仅设置了标题 """
#         self.axdict[index].set_title(self.sub_title[index], fontsize=12)
#
#     def updatePlot(self, index, x, y):
#         """
#         更新指定序号的子图
#         :param index: 子图序号
#         :param x: 横轴数据
#         :param y: 纵轴数据
#         :return:
#         """
#         # X轴数据必须和Y轴数据长度一致
#         if len(x) != len(y):
#             ex = ValueError("x and y must have same first dimension")
#             raise ex
#
#         self.axdict[index].cla()  # 清空子图数据
#         self.axdict[index].plot(x, y)  # 绘制最新的数据
#         self.setPlotStyle(index)  # 设置子图样式
#         if min(x) < max(x):
#             self.axdict[index].set_xlim(min(x), max(x))  # 根据X轴数据区间调整X轴范围
#         plt.draw()
#         print("%s end" % sys._getframe().f_code.co_name)
#
#
# def updatePlot(plot):
#     """
#     模拟收到实时数据，更新曲线的操作
#     :param plot: 曲线实例
#     :return:
#     """
#     print("Thread: %s" % threading.current_thread().getName())
#     count = 0
#     global quit_flag
#     print("quit_flag[%s]" % str(quit_flag))
#     while True:
#         if quit_flag:
#             print("quit_flag[%s]" % str(quit_flag))
#             break
#         count += 1
#         print("count#%d" % count)
#         x = np.arange(0, 100, 1)
#         y = np.random.normal(loc=1, scale=1, size=100)  # 产生随机数，模拟变化的曲线
#         index = randrange(4)  # 随机更新某一个子图
#         plot.updatePlot(index, x, y)
#         sleep(random() * 3)
#
#
# def main():
#     p = Plot2_2()  # 创建一个2X2画板
#
#     t = threading.Thread(target=updatePlot, args=(p,))  # 启动一个线程更新曲线数据
#     t.start()
#
#     p.showPlot()  # showPlot方法会阻塞当前线程，直到窗口关闭
#     print("plot close")
#     global quit_flag
#     quit_flag = True  # 通知更新曲线数据的线程退出
#
#     t.join()
#     print("Thread: %s end" % threading.current_thread().getName())
#
#
# if __name__ == '__main__':
#     main()




#!/usr/bin/env python
import PySimpleGUI as sg
from random import randint
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, FigureCanvasAgg
from matplotlib.figure import Figure

# Yet another usage of MatPlotLib with animations.

def draw_figure(canvas, figure, loc=(0, 0)):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg

def main():

    NUM_DATAPOINTS = 10000
    # define the form layout
    layout = [[sg.Text('Animated Matplotlib', size=(40, 1),justification='center', font='Helvetica 20')],
              [sg.Canvas(size=(640, 480), key='-CANVAS-')],
              [sg.Text('Progress through the data')],
              [sg.Slider(range=(0, NUM_DATAPOINTS), size=(60, 10), orientation='h', key='-SLIDER-')],
              [sg.Text('Number of data points to display on screen')],
              [sg.Slider(range=(10, 500), default_value=40, size=(40, 10), orientation='h', key='-SLIDER-DATAPOINTS-')],
              [sg.Button('Exit', size=(10, 1), pad=((280, 0), 3), font='Helvetica 14')]]

    # create the form and show it without the plot
    window = sg.Window('Demo Application - Embedding Matplotlib In PySimpleGUI', layout, finalize=True)

    canvas_elem = window['-CANVAS-']
    slider_elem = window['-SLIDER-']
    canvas = canvas_elem.TKCanvas

    # draw the initial plot in the window
    fig = Figure()
    ax = fig.add_subplot(111)
    ax.set_xlabel("X axis")
    ax.set_ylabel("Y axis")
    ax.grid()
    fig_agg = draw_figure(canvas, fig)
    # make a bunch of random data points
    dpts = [randint(0, 10) for x in range(NUM_DATAPOINTS)]

    for i in range(len(dpts)):

        event, values = window.read(timeout=10)
        if event in ('Exit', None):
            exit(69)
        slider_elem.update(i)       # slider shows "progress" through the data points
        ax.cla()                    # clear the subplot
        ax.grid()                   # draw the grid
        data_points = int(values['-SLIDER-DATAPOINTS-']) # draw this many data points (on next line)
        ax.plot(range(data_points), dpts[i:i+data_points],  color='purple')
        fig_agg.draw()

    window.close()

if __name__ == '__main__':
    main()
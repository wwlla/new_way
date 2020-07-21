import PySimpleGUI as sg
from random import randint
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, FigureCanvasAgg
from matplotlib.figure import Figure

# 渲染函数
def draw_figure(canvas, figure, loc=(0, 0)):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg

# 画面函数

def main():
    NUM_DATAPOINTS = 10000
    layout = [
        [sg.Text('动态 Mateplotlib', size=(40, 1), justification='center', font='宋体 20')],
        [sg.Canvas(size=(640, 480), key='-CANVAS-')],
        [sg.Text('数据进度条')],
        [sg.Slider(range=(0, NUM_DATAPOINTS), size=(60, 10), orientation='h', key='-SLIDER-')],
        [sg.Text('要在画面上显示的数据点数量')],
        [sg.Slider(range=(10, 500), default_value=40, size=(40, 10),
                   orientation='h', key='-SLIDER-DATAPOINTS- ')],
        [sg.Button('退出', size=(10, 1), pad=((280, 0), 3),font='宋体 14')]
    ]

    window = sg.Window('Matplotlib 嵌入式应用', layout, finalize=True)

    canvas_elem = window['-CANVAS-']
    slider_elem = window['-SLIDER-']
    canvas = canvas_elem.TKCanvas

    fig = Figure
    ax = fig.add_subplot(111)
    ax.set_xlable('X轴')
    ax.set_ylable('Y轴')
    ax.grid()

    fig_agg = draw_figure(canvas, fig)


if __name__ == '__main__':
    main()

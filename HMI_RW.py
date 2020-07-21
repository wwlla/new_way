import snap7
from snap7.snap7types import *
import EAF_COMM as EAF
import PySimpleGUI as sg
import math
import numpy as np
import  matplotlib.pyplot as plt
# 创建画布需要的库
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# 正常显示中文
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号


# 弹出画面一（能量输入）
def menu1_window():
    frame1 = [
        [sg.T('项目', size=(10, 1), font='华文中宋', justification='center'),
         sg.T('热量(KJ×1000)',  size=(15, 1), font='华文中宋', justification='center'),
         sg.T('%',  size=(8, 1), font='华文中宋', justification='center'), ],
        [sg.T('电能', size=(10, 1), font='华文中宋', justification='center'),
         sg.InputText(' ', size=(15, 1), font='华文中宋', key='IN_Q1'),
         sg.InputText(' ', size=(8, 1), font='华文中宋', key='IN_Q11')],
        [sg.T('铁水物理热', size=(10, 1), font='华文中宋', justification='center'),
         sg.InputText(' ', size=(15, 1), font='华文中宋', key='IN_Q2'),
         sg.InputText(' ', size=(8, 1), font='华文中宋', key='IN_Q22')],
        [sg.T('物料氧化热', size=(10, 1), font='华文中宋', justification='center'),
         sg.InputText(' ', size=(15, 1), font='华文中宋', key='IN_Q3'),
         sg.InputText(' ', size=(8, 1), font='华文中宋', key='IN_Q33')],
        [sg.T('', size=(10, 1), font='华文中宋', justification='center'),
         sg.T(' ', size=(15, 1), font='华文中宋'),
         sg.T(' ', size=(8, 1), font='华文中宋' )],
        [sg.T('', size=(10, 1), font='华文中宋', justification='center'),
         sg.T(' ', size=(15, 1), font='华文中宋'),
         sg.T(' ', size=(8, 1), font='华文中宋')],
    ]
    frame2 = [
        [sg.T('项目', size=(10, 1), font='华文中宋', justification='center'),
         sg.T('热量(KJ×1000)',  size=(15, 1), font='华文中宋', justification='center'),
         sg.T('%',  size=(8, 1), font='华文中宋', justification='center'), ],
        [sg.T('钢水物理热', size=(10, 1), font='华文中宋', justification='center'),
         sg.InputText(' ', size=(15, 1), font='华文中宋', key='OUT_Q1'),
         sg.InputText(' ', size=(8, 1), font='华文中宋', key='OUT_Q11')],
        [sg.T('炉渣物理热', size=(10, 1), font='华文中宋', justification='center'),
         sg.InputText(' ', size=(15, 1), font='华文中宋', key='OUT_Q2'),
         sg.InputText(' ', size=(8, 1), font='华文中宋', key='OUT_Q22')],
        [sg.T('烟气物理热', size=(10, 1), font='华文中宋', justification='center'),
         sg.InputText(' ', size=(15, 1), font='华文中宋', key='OUT_Q3'),
         sg.InputText(' ', size=(8, 1), font='华文中宋', key='OUT_Q33')],
        [sg.T('冷却水吸热', size=(10, 1), font='华文中宋', justification='center'),
         sg.InputText(' ', size=(15, 1), font='华文中宋', key='OUT_Q4'),
         sg.InputText(' ', size=(8, 1), font='华文中宋', key='OUT_Q44')],
        [sg.T('其他热损失', size=(10, 1), font='华文中宋', justification='center'),
         sg.InputText(' ', size=(15, 1), font='华文中宋', key='OUT_Q5'),
         sg.InputText(' ', size=(8, 1), font='华文中宋', key='OUT_Q55')],
    ]


    layout = [[sg.Frame('能量输入', frame1, title_color='white', relief=sg.RELIEF_SUNKEN,  font='华文中宋, 14'),
               sg.Frame('能量输出', frame2, title_color='white', relief=sg.RELIEF_SUNKEN,  font='华文中宋, 14')]
              ]
    window = sg.Window('能量平衡', layout)
    event, values = window.read()
    window.close()


# 主画面figure1（条状图fig1）
# 氧枪的瞬时能量 RCB1_FLOW RCB2_FLOW RCB3_FLOW RCB4_FLOW  RCB5_FLOW
# 氧枪的累计能量 RCB1_TOTAL RCB2_TOTAL RCB3_TOTAL RCB4_TOTAL RCB5_TOTAL
n = 5
x = np.arange(n)  # 0~11
# np.random.uniform(0.5, 1.0, n) 生产n个 0.5~1.0中随机数
y1 = (1-x/float(n))*np.random.uniform(0.5, 1.0, n)
# y2 = (1-x/float(n))*np.random.uniform(0.5, 1.0, n)
# 瞬时能量赋初始值
RCB1_FLOW, RCB2_FLOW, RCB3_FLOW, RCB4_FLOW, RCB5_FLOW = 11.0, 13.0, 50.0, 16.0, 70.0
Y = [RCB1_FLOW, RCB2_FLOW, RCB3_FLOW, RCB4_FLOW, RCB5_FLOW]
fig1 = plt.figure(figsize=(5, 3), facecolor="y")
plt.bar(x, Y, facecolor='#9999ff', edgecolor='blue')
# plt.bar(x, -y2, facecolor='#ff9999', edgecolor='blue')
plt.title('氧枪瞬时能量')
# zip 将 两个列表打包为元组的列表  ha 水平方向 va 垂直方向

RCB = ['RCB1', 'RCB2', 'RCB3', 'RCB4', 'RCB5']
plt.xticks(x, RCB)


for a, b in zip(x, Y):
    plt.text(a, b+0.05, '%.2f'% b, ha='center', va='bottom')

# for a, b in zip(x, -y2):
#     plt.text(a, b-0.05, '%.2f' % b, ha='center', va='top')



# 主画面figure2（饼状图 fig2）
labels = ['RCB1', 'RCB2', 'RCB3', 'RCB4', 'RCB5']  #饼图外侧说明文字
sizes = [2, 5, 12, 70, 11]   # 每块占用比例，如果综合超过100，就会归一化
explode = [0, 0, 0, 0, 0]  # 每块离开中心的距离

fig2 = plt.figure(figsize=(5, 3), facecolor="y")
# autopct 百分比数值设置格式  startangle 其实绘制角度
plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=False, startangle=150)
plt.title('各氧枪累计能量比例')
plt.axis('equal')  # 使饼图长宽相等
plt.text(1, -1.2, '单位：MW')   # 增加文字说明
# loc='upper right'位于右上角  bbox_to_anchor=[]  #外边距 上边 右边  ncol=2 分两列  borderaxespad=0.3 图例内边距
plt.legend(loc='upper right', fontsize=10, bbox_to_anchor=(1.1, 1.05), ncol=1, borderaxespad=0.3)

# 主画面figure3(等高线 fig3)
def get_height(x, y):
# np.exp(e) 求e幂次方
    return (1-x/2+x**5+y**3)*np.exp(-x**2-y**2)

n = 256
x = np.linspace(-3, 3, n)
y = np.linspace(-3, 3, n)
# np.meshgrid 生成网格点坐标矩阵
X, Y = np.meshgrid(x, y)

fig3 = plt.figure(figsize=(10, 4))
# 参数： 横坐标 纵坐标 高度 等高分层数量 透明度 cmap是颜色对应表 等高线的填充颜色
plt.contourf(X, Y, get_height(X, Y), 160, alpah=0.7, cmap=plt.cm.hot)

#等高线的线
# C = plt.contour(X,Y, get_height(X, Y), 16, color='black', linewidth=.5)

# 增加等高线数值
# plt.clabel(C, inline=True, fontsize=16)

plt.title('电炉熔池热能图')

# 删除纵横坐标
plt.xticks(())
plt.yticks(())


# matplotlib助手代码 （渲染函数）
# FigureCanvasXAgg就是一个渲染器，渲染器的工作就是drawing，执行绘图的这个动作。
def draw_figure(canvas, figure, loc=(0, 0)):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg


# 主函数
def main():
    sg.theme('Dark')
    # 定义菜单集合
    menu_def = [['文件', ['打开', '保存', '退出']],
                ['熔清判定', ['能量输入', '能量输出', '电能谐波'], ],
                # '---' 分割菜单栏
                ['模型', ['---', '电能模型', '供氧模型', '---', '专家系统', '渣厚模型']],
                ['历史记录', ['---', '操作记录', '---', '报表查询']],
                ['&Help', '&About...'], ]
    frame1 = [
        [sg.T('炉号：', size=(15, 1), font='华文中宋, 12'), sg.InputText('', size=(15, 1), font='华文中宋, 12', key='NO_EAF')],
        [sg.T('本炉冶炼时间：', size=(15, 1), font='华文中宋, 12'), sg.InputText('', size=(15, 1), font='华文中宋, 12'),
         sg.T('本炉送电时间：', size=(15, 1), font='华文中宋, 12'), sg.InputText('', size=(15, 1), font='华文中宋, 12')],
        [sg.T('铁水入炉量：', size=(15, 1), font='华文中宋, 12'), sg.InputText('', size=(15, 1), font='华文中宋, 12'),
         sg.T('铁水入炉温度：', size=(15, 1), font='华文中宋, 12'), sg.InputText('', size=(15, 1), font='华文中宋, 12')],
        [sg.T('废钢入炉量：', size=(15, 1), font='华文中宋, 12'), sg.InputText('', size=(15, 1), font='华文中宋, 12'),
         sg.T('废钢种类：', size=(15, 1), font='华文中宋, 12'),
         sg.InputOptionMenu(('小型', '中型', '重型'), default_value='重型', size=(12, 1))]
    ]
    frame2 = [
        [sg.T('废钢熔清进度', size=(50, 1),  font='华文中宋, 14', justification='center')],
        [sg.ProgressBar(1000, orientation='h', size=(60, 30), key='progbar'), sg.InputText('100', size=(5, 1), font='华文中宋, 16', key='value_bar')],
        [sg.T('', size=(50, 2), font='华文中宋, 14', justification='center')],

    ]

    # 获取fig1尺寸坐标
    figure1_x, figure1_y, figure1_w, figure1_h = fig1.bbox.bounds

    # 获取fig2尺寸坐标
    figure2_x, figure2_y, figure2_w, figure2_h = fig2.bbox.bounds

    # 获取fig2尺寸坐标
    figure3_x, figure3_y, figure3_w, figure3_h = fig3.bbox.bounds

    layout = [
        [sg.Menu(menu_def)],
        [sg.T('电炉冶炼智能分析系统', font='华文中宋, 30', size=(55, 1), justification='center', text_color='white')],
        [sg.Frame('炉次信息', frame1, title_color='white', relief=sg.RELIEF_SUNKEN,  font='华文中宋, 14'),
         sg.Frame('熔清判定', frame2, title_color='white', relief=sg.RELIEF_SUNKEN,  font='华文中宋, 14')],
        # [sg.Canvas(size=(1100, 2), background_color='#B09EA9')],
        [sg.Canvas(size=(100, 300), background_color='#B09EA9', key='canvas1'),
         sg.Canvas(size=(figure1_w, figure1_h), background_color='#B09EA9', key='canvas2'),
         sg.Canvas(size=(figure2_w, figure2_h), background_color='#B09EA9', key='canvas3')],
        # [sg.Canvas(size=(1100, 2), background_color='#B09EA9')],
        [sg.Canvas(size=(100, 300), background_color='#B09EA9', key='canvas4'),
         sg.Canvas(size=(figure3_w, figure3_h), background_color='#B09EA9', key='canvas5')],
        [sg.Button('启动', size=(20, 1)), sg.Button('停止', size=(20, 1))]
    ]

    window = sg.Window('测试窗口', layout,force_toplevel=True, finalize=True, grab_anywhere=True)

    # 将figure 显示在 Canvas
    draw_figure(window['canvas2'].TKCanvas, fig1)
    draw_figure(window['canvas3'].TKCanvas, fig2)
    draw_figure(window['canvas5'].TKCanvas, fig3)

    #文字内容
    #获取实例
    cir = window['canvas1'].TKCanvas.create_text(50, 60, text="氧", font="华文中宋, 24", tags = "string")
    cir = window['canvas1'].TKCanvas.create_text(50, 100, text="枪", font="华文中宋, 24", tags="string")
    cir = window['canvas1'].TKCanvas.create_text(50, 140, text="能", font="华文中宋, 24", tags="string")
    cir = window['canvas1'].TKCanvas.create_text(50, 180, text="量", font="华文中宋, 24", tags="string")
    cir = window['canvas1'].TKCanvas.create_text(50, 220, text="输", font="华文中宋, 24", tags="string")
    cir = window['canvas1'].TKCanvas.create_text(50, 260, text="出", font="华文中宋, 24", tags="string")

    cir = window['canvas4'].TKCanvas.create_text(50, 60, text="电", font="华文中宋, 24", tags="string")
    cir = window['canvas4'].TKCanvas.create_text(50, 100, text="炉", font="华文中宋, 24", tags="string")
    cir = window['canvas4'].TKCanvas.create_text(50, 140, text="熔", font="华文中宋, 24", tags="string")
    cir = window['canvas4'].TKCanvas.create_text(50, 180, text="池", font="华文中宋, 24", tags="string")


    #创建PLC的通讯
    # s7400 = snap7.client.Client()
    # EAF.connect(s7400, '192.168.0.20', 0, 3)
    while True:
        event, values = window.read(timeout=1000)
        # #熔清进度
        # window['value_bar'].update( EAF.Read_DB(s7400, 1, 6, 0, S7WLByte))
        # window['progbar'].update_bar(int(values['value_bar']))
        # print(int(values['value_bar']))

        # 条形图
        print(RCB1_FLOW)

        # EAF.Read_M(s7400, 1, 2, S7WLBit)
        # v1 = int(values['T1'])
        # EAF.Write_M(s7400, 410, 0, S7WLReal, v1)
        # value1 = EAF.Read_M(s7400, 410, 0, S7WLReal)
        # # print(value1)
        # tt = window['T']
        # tt.update(value1)
        # print(EAF.Read_Q(s7400, 1, 2))
        # EAF.Write_Q(s7400, 1, 3, 1)
        #
        # print(EAF.Read_DB(s7400,1,0,0,S7WLReal))
        # print(EAF.Read_DB(s7400, 1, 4, 4, S7WLBit))


        if event == None:
            break
        elif event == '能量输入':
            menu1_window()




if __name__ == '__main__':
    main()




import PySimpleGUI as sg
import math
import numpy as np
import  matplotlib.pyplot as plt
# 创建画布需要的库
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# 创建工具栏需要的库
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk
# 快捷键需要的库
from matplotlib.backend_bases import key_press_handler
# 导入画图常用的库
from matplotlib.figure import Figure
import matplotlib
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来显示中文标签

# 定义画面风格
sg.theme('Dark')

# 定义菜单集合
menu_def = [['文件', ['打开', '保存',  '退出']],
            ['熔清判定', ['能量输入', '能量输出', '电能谐波'], ],
            # '---' 分割菜单栏
            ['模型', ['---', '电能模型', '供氧模型', '---', '专家系统', '渣厚模型']],
            ['历史记录', ['---', '操作记录',  '---', '报表查询']],
            ['&Help', '&About...'], ]

layout = [
    [sg.Menu(menu_def)],
    [sg.T('电炉冶炼智能分析系统', font='华文中宋, 30', size=(60, 1), justification='center', text_color='white')],
    [sg.Frame(layout=[
        [sg.T('炉号：', size=(15, 1), font='华文中宋, 12'), sg.InputText('', size=(15, 1), font='华文中宋, 12')],
        [sg.T('本炉冶炼时间：', size=(15, 1), font='华文中宋, 12'), sg.InputText('', size=(15, 1), font='华文中宋, 12'),
         sg.T('本炉送电时间：', size=(15, 1), font='华文中宋, 12'), sg.InputText('', size=(15, 1), font='华文中宋, 12')],
        [sg.T('铁水入炉量：', size=(15, 1), font='华文中宋, 12'), sg.InputText('', size=(15, 1), font='华文中宋, 12'),
         sg.T('铁水入炉温度：', size=(15, 1), font='华文中宋, 12'), sg.InputText('', size=(15, 1), font='华文中宋, 12')],
        [sg.T('钢水入炉量：', size=(15, 1), font='华文中宋, 12'), sg.InputText('', size=(15, 1), font='华文中宋, 12'),
         sg.T('废钢种类：', size=(15, 1), font='华文中宋, 12'), sg.InputOptionMenu(('小型', '中型', '重型'), default_value='重型', size=(12, 1))],
    ], title='炉次信息', title_color='white', relief=sg.RELIEF_SUNKEN,  font='华文中宋, 14')],
    [sg.Canvas(size=(1200, 2), background_color='#B09EA9')],
    [sg.Canvas(size=(700, 300), background_color='#B09EA9', key='canvas1'), sg.Canvas(size=(490, 300), background_color='#B09EA9', key='canvas2')],
    [sg.Canvas(size=(1200, 2), background_color='#B09EA9')],
    [sg.Graph(canvas_size=(700, 300),  graph_bottom_left=(0, 0), graph_top_right=(700, 300), background_color='#B09EA9', key='graph1'),
     sg.Graph(canvas_size=(490, 300),  graph_bottom_left=(-105, -105), graph_top_right=(105, 105),
              background_color='white', key='graph', tooltip='This is a cool graph!')],
 ]

window = sg.Window('HMI', layout,
                   auto_size_text=False, default_element_size=False, text_justification='r', grab_anywhere=True)
window.Finalize()
# 绘制 graph 的图形
graph = window['graph']

# 绘制纵横坐标轴
graph.DrawLine((-100, 0), (100, 0))
graph.DrawLine((0, -100), (0, 100))

# 添加横坐标轴刻度、数字
for x in range(-100, 101, 20):
    graph.DrawLine((x, -3), (x, 3))
    if x != 0:
        graph.DrawText(x, (x, -10), color='green')
# 添加纵坐标轴刻度、数字
for y in range(-100, 101, 20):
    graph.DrawLine((-3,y), (3,y))
    if y != 0:
        graph.DrawText( y, (-10,y), color='blue')

# Draw Graph 绘制曲线
for x in range(-100, 100):
    y = math.sin(x/10)*50
    graph.DrawCircle((x, y), 0.5, line_color='red', fill_color='red')


# 图例一
# 获取实例
canvas1_elem = window['canvas1']
canvas1 = canvas1_elem.TKCanvas

# 创建画布
# matplotlib.style.use("seaborn")  # 设置matplotlib的风格
fig1 = Figure(figsize=(7, 3), facecolor="y")   # 可以设置画布尺寸和 比例
ax1 = fig1.add_subplot(111)
# fig1.tight_layout()  # 调整整体空白

# 把绘制的初始图形显示到pysimplegui上
figure_canvas_agg = FigureCanvasTkAgg(fig1, canvas1)
figure_canvas_agg.draw()
figure_canvas_agg.get_tk_widget().pack()

# 提供数据
data = {'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.random.randn(50)}
data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100

ax1.scatter('a', 'b', c='c', s='d', data=data)


#  图例二
# 获取实例
canvas2_elem = window['canvas2']
canvas2 = canvas2_elem.TKCanvas

# 创建画布
fig2 = Figure(figsize=(5, 3), facecolor="y")   # 可以设置画布尺寸和 比例
ax2 = fig2.add_subplot(111)

# 把绘制的初始图形显示到pysimplegui上
figure_canvas_agg2 = FigureCanvasTkAgg(fig2, canvas2)
figure_canvas_agg2.draw()
figure_canvas_agg2.get_tk_widget().pack()

labels = ['娱乐', '育儿', '饮食', '房贷', '交通', '其他']  #饼图外侧说明文字
sizes = [2, 5, 12, 70, 2, 9]   # 每块占用比例，如果综合超过100，就会归一化
explode = [0, 0, 0, 0, 0, 0]  # 每块离开中心的距离
# autopct 百分比数值设置格式  startangle 其实绘制角度
ax2.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=False, startangle=150)
ax2.set_title('饼图示例-8月份家庭支出')
ax2.axis('equal')  # 使饼图长宽相等
ax2.text(1, -1.2, 'By:Biyoulin')   # 增加文字说明
# loc='upper right'位于右上角  bbox_to_anchor=[]  #外边距 上边 右边  ncol=2 分两列  borderaxespad=0.3 图例内边距
ax2.legend(loc='upper right', fontsize=10, bbox_to_anchor=(1.1, 1.05), ncol=2, borderaxespad=0.3)

while True:
    event, values = window.read()
    if event is None:
        break
window.close()

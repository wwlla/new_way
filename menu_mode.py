import PySimpleGUI as sg


def second_window():
    layout = [[sg.Text('The second form is small \nHere to show that opening a window using a window works')],
              [sg.OK()]]
    window = sg.Window('Second Form', layout)
    event, values = window.read()
    window.close()


def test_menus():
    # 预设
    sg.change_look_and_feel('LightGreen')
    sg.set_options(element_padding=(0, 0))
    # 定义菜单选项
    menu_def = [['&File', ['&Open', '&Save', '&Properties', 'E&xit']],
                ['&Edit', ['&Paste', ['Special', 'Normal', ], 'Undo'], ],
                # '---' 分割菜单栏
                ['&Toolbar', ['---', 'Command &1', 'Command &2', '---', 'Command &3', 'Command &4']],
                ['&Help', '&About...'], ]
    # 定义右键菜单
    right_click_menu = ['Unused', ['Right::_Right_', '!&Click', '&Menu', 'E&xit', 'Properties']]
    # 定义布局
    layout = [[sg.Menu(menu_def, tearoff=False, pad=(20, 1))],
              [sg.Text('Click right on me to see right click menu')],
              [sg.Output(size=(60, 20))],  # print() 的显示结果
              [sg.ButtonMenu('ButtonMenu', key='-BMENU-', menu_def=menu_def[0])], ]
    # 定义 Window
    window = sg.Window("Windows-like program", layout,
                       default_element_size=(12, 1),
                       grab_anywhere=True,  # 非阻塞
                       right_click_menu=right_click_menu,  # 添加右键菜单
                       default_button_element_size=(12, 1)
                       )
    # 事件循环
    while True:
        event, values = window.read()
        print('Event = ', event)
        if event in (None, 'Exit'):
            break
        # ------ Process menu choices ------ #
        elif event == 'About...':
            window.disappear()  # 隐藏窗口
            sg.popup('About this program', 'Version 1.0',
                     'PySimpleGUI rocks...', grab_anywhere=True)
            window.reappear()  # 重现窗口
        elif event == 'Open':
            filename = sg.popup_get_file('file to open', no_window=True)
            print(filename)
        elif event == '-BMENU-':
            print('You selected from the button menu:', values['-BMENU-'])
        elif event == 'Properties':
            second_window()
    window.close()


test_menus()
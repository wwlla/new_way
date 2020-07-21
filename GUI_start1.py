import PySimpleGUI as sg
import requests
import json


def get_weather(city):
    r = requests.get('http://wthrcdn.etouch.cn/weather_mini?city='+city)
    print(r.text, type(r.text))
    result = json.loads(r.text)
    return result["data"]["forecast"][0]["type"]


#让所有文档居中
sg.SetOptions(text_justification='center')
layout = [
    [sg.Text('城市', size=(20, 1)), sg.Combo(('北京', '上海', '莱芜'), size=(20,1), default_value='莱芜', change_submits=True, key='-CITY-')],
    [sg.Text('明日天气', size=(20, 1)), sg.Input(key='-WEATHER-')],
    [sg.Button('查询', key='-SUMBIT-')]
]
window = sg.Window('天气查询', layout)
while True:

    event, values = window.read()
    print(event, values)
    if event is None:
        break
    city = values['-CITY-']
    weather = get_weather(city)
    print(city,'天气：', weather)
    weather_wind = window['-WEATHER-']
    weather_wind.update(weather)

    # window.read()
window.close()

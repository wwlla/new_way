from time import sleep
import snap7
from snap7.snap7exceptions import Snap7Exception
from snap7.util import *
from snap7.snap7types import *


def RM(dev, byte, bit, datatype):
    result = dev.read_area(0x83, 0, byte, datatype)  #datatype 作为 size 参数使用
    if datatype == S7WLBit:
        return get_bool(result, 0, bit)
    elif datatype == S7WLByte or datatype == S7WLWord:
        return  get_int(result, 0)
    elif datatype == S7WLReal:
        return get_real(result,0)
    elif datatype == S7WLDWord:
        return get_dword(result, 0)
    else:
        return None

def WM(dev, byte, bit, datatpye, value):
    result = dev.read_area(0x83, 0, byte, datatpye)
    if datatpye == S7WLBit:
        set_bool(result, 0, bit, value)
    elif datatpye == S7WLByte or datatpye == S7WLWord:
        set_int(result, 0, value)
    elif datatpye == S7WLReal:
        set_real(result, 0, value)
    elif datatpye == S7WLDWord:
        set_dword(result, 0, value)
    dev.write_area(0x83, 0, byte, result)
def connect(dev, ip, rack, slot):
    while True:
        if dev.get_connected():
            break
        try:
            dev.connect(ip, rack, slot)
        except:
            pass
        sleep(2)


def main():
    s7400 = snap7.client.Client()
    connect(s7400, '192.168.0.20', 0, 3)
    while True:
        try:
            print(RM(s7400, 1, 2, S7WLBit))
            sleep(1)
            WM(s7400, 410, 0, S7WLReal, 33.1)
            sleep(1)
            print(RM(s7400, 410, 0, S7WLReal))
            sleep(2)
        except Snap7Exception as e:
            connect(s7400, '192.168.0.20', 0, 3)


if __name__ == '__main__':
    main()


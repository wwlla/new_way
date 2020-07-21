import PySimpleGUI as sg
from time import sleep
import snap7
from snap7.snap7exceptions import Snap7Exception
from snap7.util import *
from snap7.snap7types import *


def Read_M(dev, byte, bit, datatype):
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


def Write_M(dev, byte, bit, datatpye, value):
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


def Read_DB(dev, DB, byte, bit, datatype):
    result = dev.read_area(0x84, DB, byte, datatype)  #datatype 作为 size 参数使用
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


def Write_DB(dev, DB, byte, bit, datatpye, value):
    result = dev.read_area(0x84, DB, byte, datatpye)
    if datatpye == S7WLBit:
        set_bool(result, 0, bit, value)
    elif datatpye == S7WLByte or datatpye == S7WLWord:
        set_int(result, 0, value)
    elif datatpye == S7WLReal:
        set_real(result, 0, value)
    elif datatpye == S7WLDWord:
        set_dword(result, 0, value)
    dev.write_area(0x83, 0, byte, result)

def Read_Q(dev, byte, bit):
    result = dev.read_area(0x82, 0, byte, 1)
    return get_bool(result, 0, bit)


def Write_Q(dev,byte,bit, value):
    result = dev.read_area(0x81, 0, byte, 1)
    set_bool(result, 0, bit, value)
    dev.write_area(0x82, 0, byte, result)

def Read_I(dev, byte, bit):
    result = dev.read_area(0x81, 0, byte, 1)
    return get_bool(result, 0, bit)


def Write_I(dev,byte,bit, value):
    result = dev.read_area(0x82, 0, byte, 1)
    set_bool(result, 0, bit, value)
    dev.write_area(0x82, 0, byte, result)

def connect(device, ip, rack, slot):
    while True:
        if device.get_connected():
            break
        try:
            device.connect(ip, rack, slot)
        except:
            pass
        sleep(5)



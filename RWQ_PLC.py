from time import sleep
import snap7.client as client
import snap7
from snap7.snap7exceptions import Snap7Exception
from snap7.util import *


def conncet(dev, ip, rack, slot):
    while True:
        if dev.get_connected():
            break
        try:
            dev.connect(ip, rack, slot)
        except:
            pass
        sleep(2)

def WQ(dev, bytebit, value):
    byte, bit = bytebit.split('.')
    byte, bit = int(byte), int(bit)
    dataArray = dev.read_area(0x82, 0, byte, 1)
    binary_list = [int(x) for x in bin(dataArray[0])[2:]]
    print(binary_list)
    set_bool(dataArray, 0, bit, value)
    binary_list = [int(x) for x in bin(dataArray[0])[2:]]
    print(binary_list)
    dev.write_area(0x82, 0, byte, dataArray)
def main():
    s7400 = client.Client()
    conncet(s7400, '192.168.0.20', 0, 3)
    while True:
        try:
            # WQ(s7400, '1.3', 1)
            # sleep(2)
            for byte in range(2):
                for bit in range(8):
                    byte_bit = str(byte) + '.' + str(bit)
                    WQ(s7400, byte_bit, 1)
                    sleep(1)
            for byte in range(2):
                for bit in range(8):
                    byte_bit = str(byte)+'.'+str(bit)
                    WQ(s7400, byte_bit, 0)
                    sleep(1)
        except Snap7Exception as e:
            conncet(s7400, '192.168.0.20', 0, 3)

if __name__ == '__main__':
    main()
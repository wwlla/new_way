import snap7
from snap7.snap7exceptions import Snap7Exception
from time import sleep


def connect(device, ip, rack, slot):
    while True:
        if device.get_connected():
            break
        try:
            device.connect(ip, rack, slot)
        except:
            pass
        sleep(5)

def ReadQ(dev):
    data = dev.read_area(0x82, 0, 1, 1)
    print(data)
    binary_list = [int(x) for x in bin(data[0])[2:]]
    print(binary_list)
def main():
    s7400 = snap7.client.Client()
    connect(s7400, '192.168.0.20', 0, 3)
    while True:
        try:
            ReadQ(s7400)
            sleep(2)
        except Snap7Exception as e: # 如果错误类型是 e
            connect(s7400, '192.168.0.20', 0, 3)




if __name__ == '__main__':
    main()
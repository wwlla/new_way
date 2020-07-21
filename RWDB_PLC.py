from time import sleep
import snap7
from snap7.snap7exceptions import Snap7Exception
from snap7.util import *
from snap7.snap7types import *


db = \
'''
DB001 Real 0.0
DB002 Bool 4.0
DB003 Int 6.0
DB004 String 8.0
DB005 Real 264.0
'''


offsets = {'Bool': 2, 'Int': 2, 'Real': 4, 'DInt': 6, 'String':256}

class DBObject(object):
    pass


def connect(dev, ip, rack, slot):
    while True:
        if dev.get_connected():
            break
        try:
            dev.connect(ip, rack, slot)
        except:
            pass

def DBRead(dev, db_num, db_len, db_items):
    data = dev.read_area(0x84, db_num, 0, db_len)
    obj = DBObject()
    for item in db_items:
        value = None\
        offset = int(item['bytebit'].split('.')[0])
        if item['datatype'] == 'Real':
            value = get_real(data, offset)


def main():
    s7400 = snap7.client.Client()
    connect(s7400, '192.168.0.20', 0, 3)
    while True:
        try:
            data = s7400.read_area(0x84, 1, 0, 5)
            print(data)
            value1 = get_real(data, 0)
            value2 = get_bool(data, 4, 0)
            print(value1, value2)
            sleep(2)
        except Snap7Exception as e:
            connect(s7400, '192.168.0.20', 0, 3)

if __name__ == '__main__':
    main()

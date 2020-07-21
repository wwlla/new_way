from time import sleep
import snap7
from snap7.snap7exceptions import Snap7Exception
from snap7.util import *

db = \
"""
DB001 Real 0.0
DB002 Bool 4.0
DB003 Int 6.0
DB004 String 8.0
DB005 Real 264.0
"""

offsets = { "Bool":2,"Int": 2,"Real":4,"DInt":6,"String":256}

class DBObject(object):
    pass


def connect(device, ip, rack, slot):
    while True:
        # check connection
        if device.get_connected():
            break
        try:
            # attempt connection
            device.connect(ip, rack, slot)
        except:
            pass
        sleep(5)


def DBRead(dev,db_num,db_len,db_items):
    data = dev.read_area(0x84,db_num,0,db_len)
    obj = DBObject()
    for item in db_items:
        value = None
        offset = int(item['bytebit'].split('.')[0])

        if item['datatype']=='Real':
            value = get_real(data,offset)

        if item['datatype']=='Bool':
            bit =int(item['bytebit'].split('.')[1])
            value = get_bool(data,offset,bit)

        if item['datatype']=='Int':
            value = get_int(data, offset)

        if item['datatype']=='String':
            value = get_string(data, offset, 256)

        obj.__setattr__(item['name'], value)

    return obj

def get_db_len(db_items,bytebit,datatype):
    offset_int = []
    offset_str,datatype =[(x[bytebit]) for x in db_items],[x[datatype] for x in db_items]
    for x in offset_str:
        offset_int.append(int(x.split('.')[0]))
    idx = offset_int.index(max(offset_int)) #结果=4
    db_len = (max(offset_int)) + int(offsets[datatype[idx]]) #结果=264+4=268
    return db_len

def main():
    s71200 = snap7.client.Client()
    connect(s71200, '192.168.0.20', 0, 3)
    while True:
        try:
            itemlist = filter(lambda a: a != '', db.split('\n'))
            space = ' '
            items = [
                {
                    "name": x.split(space)[0],
                    "datatype": x.split(space)[1],
                    "bytebit": x.split(space)[2]
                } for x in itemlist
            ]
            db_len = get_db_len(items, 'bytebit', 'datatype')
            DB_obj = DBRead(s71200, 1, db_len, items)
            print(DB_obj.DB001, DB_obj.DB002, DB_obj.DB003, DB_obj.DB004, DB_obj.DB005)
            sleep(5)
        except Snap7Exception as e:
            connect(s71200, '192.168.0.20', 0, 3)

if __name__ == '__main__':
    main()
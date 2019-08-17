# coding = utf-8

import socket
from rbkNetProtoEnums_L import *
import time
import json
import struct
import os

# build connection
so= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
so.settimeout(2)
so.connect((Robot_Ip,Api_Port_Status))

# send request

myrequst1 = packMasg(2,robot_status_info_req,{})
# so.send(myrequst)
so.send(myrequst1)


# receive tne information
head_data = so.recv(16)
jsonDataLen = 0
if (len(head_data)<16):
    print('pack head error')
    os.system('pause')
    so.close()
    quit()
else:
    jsonDataLen= unpackHead(head_data)


rec_data2 = so.recv(1024)

d_rec_data1 = rec_data2.decode('utf-8')

print(d_rec_data1)
print(jsonDataLen)



















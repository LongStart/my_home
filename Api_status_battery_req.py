# conding = 'utf-8'

import socket
import time
import json

from rbkNetProtoEnums_L import *

# build the sochet

so = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
so1 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# build the connection
so.connect((Robot_Ip,Api_Port_Status))
so.settimeout(2)

so1.connect((Robot_Ip,Api_Port_Status))
so1.settimeout(2)

# my request
my_request = packMasg(3,robot_status_battery_req,{})
my_request1 = packMasg(3,robot_status_emergency_req,{})

# send my request

so.send(my_request)
so1.send(my_request1)

# recieve the data

msg_head = so.recv(16)
msg_head2 = so1.recv(16)

if len(msg_head) < 16:
    print("pack wrong head message  ")

msg_data1 = so.recv(1024).decode(encoding='utf-8')
msg_data2 = so1.recv(1024).decode(encoding='utf-8')

print(msg_data1)

while True:
    so.send(my_request)
    so.recv(16)
    print(so.recv(1024).decode(encoding='utf-8'))
    so1.send(my_request1)
    so1.recv(16)
    print(so1.recv(1024).decode(encoding='utf-8'))
    time.sleep(3)



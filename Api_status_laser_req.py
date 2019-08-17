
from rbkNetProtoEnums_L import *
import socket
import time
import json
import csv


# build socket

so = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
so.connect((Robot_Ip,Api_Port_Status))

# send request
msg = packMasg(3,robot_status_laser_req)
so.send(msg)


# recv data

data_head = so.recv(16)
len_data_head = len(data_head)
if len_data_head < 16:
    print("wrong pack head")


data_msag1 = so.recv(1024).decode(encoding='utf-8')
data_msag2 = so.recv(1024).decode(encoding='utf-8')
data_msag3 = so.recv(1024).decode(encoding='utf-8')

with open("status_laser_data.log","a",newline="") as f:
    # writer = f.writer(f)
    # writer.writerow(data_msag1)
    # writer.writerow(data_msag2)
    # writer.writerow(data_msag3)
    # f.write(data_msag1)
    f.write(data_msag2)
    f.write(data_msag3)

    f.close()





print(data_msag1)





# output the data







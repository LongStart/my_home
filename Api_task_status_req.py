# coding = 'utf-8'
import socket
import time

from rbkNetProtoEnums_L import *


# build socket connection
# Robot_Ip = '192.168.0.6'
so = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
so.connect((Robot_Ip,Api_Port_Status))
# so.settimeout(5)


# send my request

my_requrest = packMasg(2,robot_status_task_req,{})
so.send(my_requrest)


# receive the message of the robot
raw_msg_head = so.recv(16)
len_msg_head = len(raw_msg_head)
print(len_msg_head)
if (len_msg_head < 16):
    print("wrong pack head message")

else:
    raw_msg = so.recv(2048)
    msg = raw_msg.decode(encoding='utf-8')
    print(msg)

while True:
    so.send(my_requrest)
    time.sleep(10)





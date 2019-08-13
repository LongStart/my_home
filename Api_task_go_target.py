from rbkNetProtoEnums_L import *
import time
import socket
import json

# Robot_Ip = '192.168.98.50'

# build socket connection

so = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
so.connect((Robot_Ip,Api_Port_Navig))
so.settimeout(2)


# send request

my_request_go_1 = packMasg(1,robot_task_go_target_req,{"id":"LM1"})
my_request_go_2 = packMasg(1,robot_task_go_target_req,{"id":"LM2"})


# build the function of req_status_task
def req_status_task(IP=Robot_Ip):
    so1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    so1.connect((IP, Api_Port_Status))
    so1.settimeout(2)
    my_request_task = packMasg(1, robot_status_task_req, {})
    my_task_status = 0

    while my_task_status != 0:
        so1.send(my_request_task)
        so1.recv(16)
        raw_task_status = so1.recv(1024).decode(encoding='utf-8')
        dict_raw_task_status = dict(json.loads(raw_task_status))
        my_task_status = dict_raw_task_status.get("task_status")
        time.sleep(0.1)
        return my_task_status






so.send(my_request_go_1)


#
# while True:
#     so.send(my_request_go_1)
#     if req_status_task() ==4:
#         so.send(my_request_go_2)
#
#



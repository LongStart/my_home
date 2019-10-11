
# 展会用机器人批量回收控制权
# 5A 01 00 01 00 00 00 00 0F A1 00 00 00 00 00 00



import socket
import time
from rbkNetProtoEnums_L import *

Robot1 = '192.168.192.5'
# build the socket

so = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
so.connect((Robot1,Api_Port_Config))
so.settimeout(2)

# message
message = packMasg(1,robot_config_require_req)

# send the message

so.send(message)






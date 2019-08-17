# conding = utf-8

import json
import struct



Api_Port_Status = 19204
Api_Port_Ctrl = 19205
Api_Port_Navig = 19206
Api_Port_Config = 19207
API_PORT_Kernel = 19208
Api_Port_Other = 19210


robot_status_info_req = 1000
robot_status_run_req = 1002
robot_status_loc_req = 1004
robot_status_speed_req = 1005
robot_status_block_req = 1006
robot_status_battery_req = 1007
robot_status_brake_req = 1008
robot_status_laser_req = 1009
robot_status_emergency_req = 1012
robot_status_io_req = 1013
robot_status_task_req = 1020
robot_status_all1_req = 1100
robot_status_all2_req = 1101
robot_status_all3_req = 1102


robot_task_pause_req = 3001
robot_task_resume_req = 3002
robot_task_cancel_req = 3003
robot_task_go_target_req = 3051
robot_task_target_path_req = 3053




# 0x5A + verson(0x01)+ sequence number(0x00 0x01) + length of data +  type of data + reserve data(0x00 0x00 0x00 0x00 0x000x00)
# + data

Pack_Head_Fomt ='>BBHLH6s'
# Pack_Reserve_Data = bytes('\x00\x00\x00\x00\x00\x00',encoding='utf-8')
Pack_Reserve_Data = b'\x00\x00\x00\x00\x00\x00'


def packMasg(reqId, msgType, msg={}):
    msgLen = 0
    jsonStr = json.dumps(msg)
    if (msg != {}):
        msgLen = len(jsonStr)
    rawMsg = struct.pack(Pack_Head_Fomt, 0x5A,1,reqId,msgLen,msgType,Pack_Reserve_Data)

    if (msg != {}):
        rawMsg += bytearray(jsonStr,'ascii')

    return rawMsg



def unpackHead(data):
    result = struct.unpack(Pack_Head_Fomt,data)
    jsonLen = result[3]
    reqNum = result[4]
    # result = data.hex()
    # jsonLen = result[8:15]
    # reqNum = result[4]

    return (jsonLen, reqNum)
    # return (result,jsonLen,reqNum)


# set Robot IP address
Robot_Ip ='192.168.4.212'
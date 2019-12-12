"""
============================
author:wbl
time:2019/12/12
E-mail:540453724@qq.com
============================
"""
import lcm
from lcmtypes import *


#from exlcm import example_t

#if len(sys.argv) < 2:
#    sys.stderr.write("usage: read-log <logfile>\n")
#    sys.exit(1)

log = lcm.EventLog('80.01', "r")

for event in log:
    if event.channel == "ESR_FRONT_DATA":
        msg = lidar_object_t.decode(event.data)

#        print("Message:")
        print('相对距离m')
        m = float(msg.frontObject.objectCenterPosition.y)
        print(str(msg.frontObject.objectCenterPosition.y))
        print('相对速度km/h')
        s = float(msg.frontObject.objectCenterSpeed.y*3.6)
        print(float(msg.frontObject.objectCenterSpeed.y*3.6))
        print('碰撞时间s')
        #print(msg.frontObject.objectCenterPosition.y / msg.frontObject.objectCenterSpeed.y)
        print(m/s)
        print('--------')

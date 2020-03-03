"""
============================
author:wbl
time:2020/3/2
E-mail:540453724@qq.com
读取lcm包
============================
"""

import lcm
from lcmtypes.platoon import platoon_control_debug_t

# 模式 1 - CACC, 2 - ACC
control_mode = []
# 本车车速
speed_ego = []
# 目标车速
speed_target = []
# CACC车间距误差
spacing_error = []
# 时间戳原始
utimes = []
# 时间戳 S
utime = []
# 车间距
member = []
# 本车和前车车距
spacing_current = []
# 当前目标车距
spacing_target = []


class LcmStructure():
    """
    自动驾驶评测系统
    目前拿到的通道：车辆模式、目标速度、实际速度、间距误差
    """

    def _init_(self, name):
        """"数据初始化"""
        self.name = name

    def read(name):
        log = lcm.EventLog(name, "r")
        for event in log:
            if event.channel == "CONTROL_DEBUG":
                msg = platoon_control_debug_t.decode(event.data)
                # 车辆模式
                control_mode.append(msg.control_mode)
                # 本车速度
                speed_ego.append(msg.speed_ego * 3.6)
                # 目标车速
                speed_target.append(msg.speed_target * 3.6)
                # CACC车间距误差
                # spacing_error.append(msg.spacing_current)
                # 本车和前车车距
                spacing_current.append(msg.spacing_current)
                # 当前目标车距
                spacing_target.append(msg.spacing_target)
                spacing_error.append(msg.spacing_current - msg.spacing_target)
                # 时间戳
                utimes.append(msg.utime)

        for a in utimes:
            # 获取正确的时间
            utime.append((a - utimes[0]) / 1000000)

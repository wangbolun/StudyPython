"""
============================
author:wbl
time:2019/12/10
E-mail:540453724@qq.com
============================
"""

import lcm
import matplotlib.pyplot as plt
from lcmtypes import vehicle_status_t
from lcmtypes import speed_cmd_t
import numpy as np


# 实际车速
square = []
# 车速时间戳
time = []
# 目标车速
squares = []
# 目标车速时间戳
times = []


class read_lcmlog():
    """lcm数据读取"""

    def _init_(self, name):
        """"数据初始化"""
        self.name = name

    def speed(name):
        log = lcm.EventLog(name, "r")
        for event in log:
            if event.channel == "VEHICLE_STATUS":
                msg = vehicle_status_t.decode(event.data)
                # "时间戳"
                car_time = event.timestamp
                time.append(car_time)
                # 左轮车速
                L = float(msg.speLeft)
                # 右轮车速
                R = float(msg.speRight)
                # 实际车速
                S = (R + L) / 2
                #                print(S)
                square.append(S)
        average_a = np.mean(square)

        #print('平均车速为：{:.2f} km/h'.format(average_a))

        logs = lcm.EventLog(name, "r")
        for event in logs:
            if event.channel == "SPEED_CMD":
                msgs = speed_cmd_t.decode(event.data)
                car_times = event.timestamp
                times.append(car_times)
                squares.append(float(msgs.aim_spe))

        # 引用数据源

        plt.figure(num=3, figsize=(8, 5))
        # 设置线条粗细
        # plt.plot(squares,linewidth=1)
        # 设置图标标题并给坐标轴加上标签
        plt.title("Speed", fontsize=24)

        # 设置XY轴坐标系
        plt.xlabel("time", fontsize=14)
        plt.ylabel("speed_km/h", fontsize=14)
        # 标记刻度大小
        plt.tick_params(axis='both', labelsize=14)
        plt.figure(num=3, figsize=(8, 5))
        # 实际车速
        plt.plot(time, square, label='Actual_Speed')
        # 目标车速
        # plt.plot(times, squares,label = 'Target_Speed')
        plt.legend()
        # 插入平均值
        plt.text(np.mean(time), np.mean(square), ' Average {:.2f} km/h'.format(average_a), family='fantasy',
                 fontsize=16, style='italic', color='mediumvioletred')
        # 自动存图，以文件名称命名
        plt.savefig('./{}Speed.jpg'.format(name))
        plt.close()
	    #plt.show()


if __name__ == '__main__':
    read_lcmlog.speed(input('请输入数据名称：'))


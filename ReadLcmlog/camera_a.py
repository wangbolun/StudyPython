"""
============================
author:wbl
time:2019/12/10
E-mail:540453724@qq.com
============================
"""

import lcm
import matplotlib.pyplot as plt
import numpy as np
from lcmtypes import *
import math

camera_time = []
camera_a = []
camera_ja = []


class read_lcmlog():
    """lcm数据读取"""

    def _init_(self, name):
        """"数据初始化"""
        self.name = name

    def camera_a(name):
        log = lcm.EventLog(name, "r")
        for event in log:
            if event.channel == "camera":
                msgs = camera_info_t.decode(event.data)
                camera_t = event.timestamp
                camera_time.append(camera_t)
                camera_a.append(float(msgs.center_line.a))
        # 平均横向偏差
        average_a = np.mean(camera_a)
        # 最大横向偏差
        median_a = np.median(camera_a)

        #导入图
        plt.figure(num=3, figsize=(8, 5))
        # 设置线条粗细
        # plt.plot(squares,linewidth=1)
        # 设置图标标题并给坐标轴加上标签
        plt.title("deviation", fontsize=24)

        # 设置XY轴坐标系
        plt.xlabel("time", fontsize=14)
        plt.ylabel("deviation(m)", fontsize=14)
        # 标记刻度大小
        plt.tick_params(axis='both', labelsize=14)
        #        input_values = [1,2,3,4,5]
        #        plt.plot(input_values,squares,linewidth=5)
        plt.figure(num=3, figsize=(8, 5))
        plt.plot(camera_time, camera_a, label='deviation')
        plt.legend()
        
        # 插入平均值
        plt.text(np.mean(camera_time), np.mean(camera_a),
                 ' Average {:.2f} m \nmax{:.2f} m\nmin{:.2f}'.format(average_a, max(camera_a),min(camera_a)), family='fantasy',
                 fontsize=16, style='italic', color='mediumvioletred')
        # 自动保存图片
        plt.savefig('./{}deviation.jpg'.format(name))
        plt.close()
        #plt.show()


if __name__ == '__main__':
    read_lcmlog.camera_a(input('请输入数据名称：'))

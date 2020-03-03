"""
============================
author:wbl
time:2019/12/10
E-mail:540453724@qq.com
============================
"""
"""
项目的启动文件,最后的选择数据逻辑在这里实现，会产生图片保存到logs内。
"""

import matplotlib.pyplot as plt
from commom.read_lcm import *
from commom.constant import *

lcmname = input('请输入data目录下正确的数据名称：')
LcmStructure.read(os.path.join(DATA_DIR, lcmname))

plt.figure(num=3, figsize=(8, 5))
plt.grid()
plt.title(lcmname, fontsize=24)
# 输入想要查看的数据项目
print('0:本车车速,1:当前目标车距')
sitis = (input('请输入查询项：'))
for siti in sitis:
    if siti == '0':
        plt.plot(utime, speed_ego, label='speed_ego')
    elif siti == '1':
        plt.plot(utime, spacing_target, label='spacing_target')
    elif siti == '2':
        plt.plot(utime, spacing_current, label='spacing_current')
    elif siti == '3':
        plt.plot(utime, spacing_error, label='spacing_error')
    elif siti == '4':
        plt.plot(utime, control_mode, label='control_mode')
    elif siti == '5':
        plt.plot(utime, control_mode, label='control_mode')

plt.legend()
plt.savefig(os.path.join(LOG_DIR, lcmname), format="svg")
plt.show()

"""
============================
author:wbl
time:2019/12/12
E-mail:540453724@qq.com
============================
"""

import os
from common.constant import LCM_LOG

w = LCM_LOG
for root,dirs,files in os.walk(LCM_LOG):
        for file in files:
            #获取文件所属目录
            #print(root)
            #获取文件路径
            #print(os.path.join(root,file))
            c = os.path.join(root,file)
            print(c)
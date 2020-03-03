"""
============================
author:wbl
time:2019/12/10
E-mail:540453724@qq.com
============================
"""
import os

"""
常量模块，
获取项目项目目录的路径，保存

项目路径：
配置文件的路径：
用例数据的路径：

"""

# 项目目录路径
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# 日志文件所在的目录路径
LOG_DIR = os.path.join(BASE_DIR, 'logs')

# 配置文件所在的目录
CONF_DIR = os.path.join(BASE_DIR, 'conf')

# lcm数据所在的目录
DATA_DIR = os.path.join(BASE_DIR, 'data')

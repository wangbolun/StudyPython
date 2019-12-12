
import os


# print(__file__)
# 
# res = os.path.dirname(__file__)
# print(os.path.dirname(res))

# 项目目录路径
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# 测试用例所在的目录路径
LCM_LOG = os.path.join(BASE_DIR, 'lcmlog')


# 测试报告所在的目录路径
REPORT_DIR = os.path.join(BASE_DIR, 'reports')

# 日志文件所在的目录路径
LOG_DIR = os.path.join(BASE_DIR, 'logs')

# 配置文件所在的目录
CONF_DIR = os.path.join(BASE_DIR, 'conf')

# 用例数据所在的目录
DATA_DIR = os.path.join(BASE_DIR, 'data')

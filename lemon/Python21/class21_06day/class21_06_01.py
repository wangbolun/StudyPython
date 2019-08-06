"""
============================
author:Administrator
time:2019/8/1
E-mail:540453724@qq.com
============================
"""

"""
函数：
自己定义函数
关键字 def ：用来定义函数
函数作用：用来封装功能，提高代码的复用性

:return 关键字   以来给函数定义给函数定义返回值    只能用在函数
一个函数里面只要执行到return那么这个函数就运行结束

内置函数 type   id   range 

"""


# 函数的定义
def add():
    pass


# 相加

def add():
    #    print("这个是用来计算两个数相加的")
    # 函数的返回值 return
    a = 100
    b = 200
    c = a + b
    d = a - b
    if c == 300:
        return "等于300"
    else:
        return "不等于300"
    return c, d


#    print(a+b)
res1 = add()
# cc, dd  = res1
print(res1)
print(cc, dd)

# add()
#
#
# res = type(100)
# print(res)


#
# res =type("7")
# print(res)

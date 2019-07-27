"""
============================
author:Administrator
time:2019/7/26
E-mail:540453724@qq.com
============================
"""
# 2.编写代码，提示用户输入1-7七个数字，分别代表周一到周日，如果输入的数字是6或7则为周末，打印输出“今天是周几”

tady = int(input("请输入1~7之间数字："))
if tady == 1:
    print("今天是周一")
elif tady == 2:
    print("今天是周二")
elif tady == 3:
    print("今天是周三")
elif tady == 4:
    print("今天是周四")
elif tady == 5:
    print("今天是周五")
elif tady == 6:
    print("今天是周六")
elif tady == 7:
    print("今天是周日")
else:
    print("输入错误，请输入1~7之间数字")

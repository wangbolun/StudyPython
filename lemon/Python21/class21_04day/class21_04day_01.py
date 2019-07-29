"""
============================
author:Administrator
time:2019/7/28
E-mail:540453724@qq.com
============================
"""

"""
元祖

"""

tu1 = (111,2222,333,11111)
print(tu1.count(111))
print(tu1.index(333))

tu2 = ([1,2,3,4],999,10)
print(id(tu2))
tu2[0].append(6)
print(tu2)
print(id(tu2))
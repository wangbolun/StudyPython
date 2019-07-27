"""
============================
author:Administrator
time:2019/7/26
E-mail:540453724@qq.com
============================
"""
#4、切片
# 1、li = [1,2,3,4,5,6,7,8,9] 请通过切片得出结果 [3,6,9]
# 2、s = 'python java php',通过切片获取: ‘java’
# 3 、tu = ['a','b','c','d','e','f','g','h'],通过切片获取 [‘g’,‘b’]

li = [1,2,3,4,5,6,7,8,9]
print(li[2::3])

s = 'python java php'
print(s[7:11])

tu = ['a','b','c','d','e','f','g','h']
tul = tu[-7:-1:5]
tul.reverse()
print(tul)
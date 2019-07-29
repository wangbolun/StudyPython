"""
============================
author:Administrator
time:2019/7/28
E-mail:540453724@qq.com
============================
"""

""""
元祖 列表 字符串通用操作
序列类型 ：有下标索引，可以切片

通用操作：   
1.索引取值和切片
2.len() 获取长度
3.序列类型之间的相互转换
str()   list()    tuple()

"""

str1 = "a,b,c,d,d"
tu1 = (11,22,33,44)
li1 = [444,55,88,66]
print(len(str1))
print(len(tu1))
print(len(li1))

print(list(str1))
print(str(tu1))
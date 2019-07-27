"""
============================
author:Administrator
time:2019/7/26
E-mail:540453724@qq.com
============================
"""
# 3、现在有一个列表 li2=[1，2，3，4，5]，
# 第一步：请通过相关的操作改成li2 = [0，1，2，3，66，4，5，11，22，33]，
# 第二步：对li2进行排序处理
# 第三步：请写出删除列表中元素的方法，并说明每个方法的作用


li2=[1,2,3,4,5]
li2.insert(0,0)
li2.insert(4,66)
li2.insert(7,11)
li2.insert(8,22)
li2.insert(9,33)
print(li2)
print(sorted(li2))
# del 语句删除
del li2[0]
print(li2)
# pop 删除末尾
li2.pop()
print(li2)
#删除下标位置
li2.pop(2)
print(li2)
# remov 删除元素
li2.remove(11)
print(li2)
#del删除
del li2[0]
#清空
li2.clear()
print(li2)
"""
============================
author:Administrator
time:2019/7/23
E-mail:540453724@qq.com
============================
"""


""""
字符串：

字符串定义：单引号  双引号 三引号   、 内置函数str（）  转换为字符串类型

注意点： 空白字符  和空字符

#空字符 None     bool 布尔值查看
str1 = ""
print(bool(str1))



#空白字符
str2 = " "


字符串取值：下标索引取值  和切片
索引取值：从左往右0开始     从右往左-1开始
切片：[start_index:end_index]  终止位置不包含进去（左闭右开）   
字符串拼接+
字符串的转义

"""

name = 'wangbolun'

desc = """
1、aaa
2、vvvv
"""


age = 18


#转化字符串

age = str(age)

print(type(age))

#空字符 None     bool 布尔值查看
str1 = ""
print(bool(str1))



#空白字符
str2 = " "

print(bool(str2))


str3 = 'python'
str4 = 'python '
str3 == str4

str5 = str1+str2+str4
print(str5)
print(str5*5)

#\n换行   \t 制表符 四个空格    特殊语义
#  字符串前边加r  关闭转义



#4.字符串常用方法.join字符串拼接
#find   查找字符串
#count统计数量

a = 'aaa'
#str7 = a.join(['11','22','33'])
str7 = a.join('123')
print(str7)

bb = "python"

print(bb.find('py'))
print(bb.count(o))

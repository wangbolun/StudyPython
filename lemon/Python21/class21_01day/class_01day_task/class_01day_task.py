"""
============================
author:Administrator
time:2019/7/19
E-mail:540453724@qq.com
============================
"""

# 1、下面那些不能作为标识符？
#
# 1、find     2、 _num   3、7val   4、add.    5、def
# 6、pan     7、-print   8、open_file 9、FileName   10、print
# 11、INPUT   12、ls     13、user^name  14、list1   15、str_


# 答案：3、7val(数字不能当标识符)；5、def(python关键词，定义函数用);7、-print（间隔线不可开头）
#10、print（关键词）；13、user^name（^不可当标识符）


name = (input("请输入姓名："))
age = (input("请输入年龄："))
gender = (input("请输入性别："))

print("性别：", name)
print("性别：", age)
print("年龄：", gender)
# print('21期的大佬很厉害')

"""

文档注释
字符串：引号包起来

变量：用来储存数据
python里面的关键字：['False', 'None', 'True', 'and',
'as', 'assert', 'async', 'await', 'break', 'class',
 'continue', 'def', 'del', 'elif', 'else', 'except',
 'finally', 'for', 'from', 'global', 'if', 'import',
 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass',
  'raise', 'return', 'try', 'while', 'with', 'yield']'

多行语句\ 显示

"""
print('21期的大佬'
      '很厉害')  # 自动连接

print("""21期的
大佬
很厉
害""")  # 三引号自动连接 保留格式

x = 10
a = 10
c = 10
y = x * 2

name = "Wangbolun"

aga_max = 24
# 小驼峰
agaMax = 25
# 大驼峰   类使用
AgaMax = 26

gender = "男"

# python 里面关键字不能使用
import keyword

print(keyword.kwlist)

# 一行代码多行显示
desc = "这个是用来测\
试换行拼接\
的"

print(desc)

# ctrl+?  多行注释

name = input("请输入姓名：")
age = input("请输入年龄：")

# Ctrl+Alt+shift+l  调整空格

print("我的名字：", name)
print("我的年龄：", age)

# 整数 int   浮点数 float   布尔值 bool   true false

#type()查看类型

"""
============================
author:MuSen
time:2019/8/3
E-mail:3247119728@qq.com
============================
"""
"""
python中的内置函数

int   float  bool  str  list   tuple  
dict  set   range   len
type  id   print  input

max  min  sum
"""

# li = [11,22,33,44,55]
#
#
# max_value = max(li)
# print(max_value)
# print(min(li))
# print(sum(li))

#  enumerate
li = [11, 22, 33, 4, 55, 'a', 'bb']
#
# for i, j in enumerate(li):
#     print('下标：{}，值：{}'.format(i,j))

# eval:能够识别字符中的python表达式

# exec: 动态执行字符串中的python代码


# str1 = "1+2"
# res = eval(str1)
# print(type(res))
# print(res)

# num = eval(input('请输入:')
# print(type(num),num)

str2 = "print('hello python')"

eval(str2)

str5 = """
def func():
    print(111)
"""

# eval(str5)


# exec(str5)
#
# func()

#  filter:过滤


li2 = [11, 22, 33, 44, 1, 41, 98]


def func(x):
    return x > 40


res = filter(func, li2)

print(list(res))


# map:

def add(a):
    return a[0] + a[1]


list_val = [(11, 22), (33, 44), (55, 66)]
res2 = map(add, list_val)
print(list(res2))

#  zip:打包聚合

title = ['name', 'age', 'gender']

value = ['musen', 18, '男']


# li77 = [11,22,33,44,55]
#
# li88 = [11,22,33,44,55]

res5 = zip(title,value)


for item in res5:
    print(item)

# print(dict(res5))
# print(list(res5))

# isinstance:  判断数据类型

num = 1000
str12 = 'str'

print(isinstance(num,str))





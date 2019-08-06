"""
============================
author:MuSen
time:2019/8/3
E-mail:3247119728@qq.com
============================
"""
"""
函数的不定长参数:可以传值（1个或者多个），也可以不传
*agrs: 用来接收未被接收的位置参数，保存为一个元组
**kwargs: 用来接收未被接收的关键字参数，保存为一个字典


*\**：打包 (不定长参数)

*\**：拆包（函数调用）

"""


def add(a, b, c, *args, **kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)
    print(type(args))


def func(a):
    print(a)

tu = (11, 22, 33, 44, 55)
dic = {"a": 111, "b": 222, "c": 333, "dd": 2222, "ff": 22288}
# add(*tu)
add(**dic)


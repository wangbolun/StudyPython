"""
============================
author:MuSen
time:2019/8/3
E-mail:3247119728@qq.com
============================
"""

"""
函数的作用域：

全局变量：直接定义在模块（py中的变量），在整个文件中任何地方都能够访问

局部变量：定义在函数中的，它的作用范围，仅限于当前的作用域（定义的函数中）



"""

# a = 200
#
#
# def func():
#     b =100
#     print(b)
#     print(a)
#
# # print(a)
#
# func()


#  在函数中声明全局变量

# a = 1
#
#
# def func1():
#     a = 1
#     a = a + 100
#     # c = c+100
#     # print(c)
#
#
# func1()
#
# print(a)

# num = 1000
#
#
# def func1():
#     print('func1----num:',num)
#     def fun3():
#         global num
#         num += 1
#         print('fun3----num:',num)
#
#     fun3()
#
#     print('func1--2----num:',num)
#
#
# func1()
#
#
# print(num)

# num = 10
#
#
# def func1():
#     num = 100
#     def fun3():
#         nonlocal num
#         num = 999
#         print('fun3----num:', num)
#     fun3()
#     print('func1--2----num:', num)
#
#
# func1()

#
# def fun():
#     nonlocal num
#     num=100
#
# print(num)
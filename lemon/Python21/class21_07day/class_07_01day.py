"""
============================
author:Administrator
time:2019/8/5
E-mail:540453724@qq.com
============================
"""

"""
不定长参数：
**agrs  
**kwargs

*打包 （不定长参数）
*拆包(函数调用)

"""

# def add(a,b,*args,**kwargs):
#     print(a)
#     print(b)
#     print(args)
#     print(kwargs)
# # add(11,22,111,4444,5,cc=999,dd=555)
# tu = (11,22,33,44,55)
# add(*tu)



"""
#在函数中声明全局变量

"""

def func1():
    global a   # 声明全局变量
    a = 100
    print(a)
func1()
print(a)


a = [1,2,3,4,5,6,7]
print(len(a))
print(min(a))
print(max(a))
print(sum(a))


str2 = "print('hello world')"
exec(str2)

str5 = """
def func():
    print(1111)


"""
exec(str5)
#

lis1 = [11,22,33,44,55,66]
def func(x):
    return  x>30
res = filter(func,lis1)
print(list(res))

res2 = map(func,lis1)
print(list(res2))


li1=['name',"age","gender"]
li2=["wangbokun",18,"男"]
res5 = zip(li1,li2)
print(dict(res5))


num = 100

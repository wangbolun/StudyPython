"""
============================
author:wbl
time:2019/7/27
E-mail:540453724@qq.com
============================
"""
""""

1.将给定字符串的PHP替换为Python      
  best_language = "PHP is the best programming language in the world! "





2、编写代码，提示用户输入1-7七个数字，分别代表周一到周日，如果输入的数字是6或7则为周末，打印输出“今天是周几” 



3、现在有一个列表 li2=[1，2，3，4，5]，


     第一步：请通过相关的操作改成li2 = [0，1，2，3，66，4，5，11，22，33]，

     第二步：对li2进行排序处理 

    第三步：请写出删除列表中元素的方法，并说明每个方法的作用



 4、切片 

        1、li = [1,2,3,4,5,6,7,8,9] 请通过切片得出结果 [3,6,9] 

        2、s = 'python java php',通过切片获取: ‘java’ 

        3 、tu = ['a','b','c','d','e','f','g','h'],通过切片获取 [‘g’,‘b’] 



5、写出上课讲的 列表的所有方法 ，并说明  每个方法有什么作用

"""


print("*****************第一题*********************")
best_language = "PHP is the best programming language in the world! "
print(best_language.replace("PHP","Python"))


print("*****************第二题*********************")
tady = int(input("请输入1~7之间的数字："))
if tady == 1:
    print("今天是周一")
elif tady == 2:
    print("今天是周二")
elif tady == 3:
    print("今天是周三")
elif tady == 4:
    print("今天是周四")
elif tady == 5:
    print("今天是周五")
elif tady == 6:
    print("今天是周六")
elif tady == 7:
    print("今天是周日")
else:
    print("请输入1~7之间的任意数字")


print("*****************第三题*********************")
li2=[1,2,3,4,5,6]
li2.insert(0,0)
print(li2)
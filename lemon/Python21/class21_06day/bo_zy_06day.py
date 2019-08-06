"""
============================
author:Administrator
time:2019/8/2
E-mail:540453724@qq.com
============================
"""

""""
1、一、输出99乘法表，结果如下：（提示嵌套for循环，格式化输出）
2、有1 2 3 4 这四个数字，设计程序计算能组成多少个互不相同且无重复数字的3位数？分别是什么？
3、通过函数实现一个计算器，运行程序分别提示用户输入数字1，数字2，然后再提示用户选择 ：   加【1】    减【2】    乘【3】      除【4】，
每个方法使用一个函数来实现， 选择后调用对应的函数，然后返回结果。
4、对上次作业的石头剪刀布游戏升级，游戏一轮出拳后进入下一轮，
当选择结束游戏后，打印本次游戏的胜率：    胜利的次数  /玩的总次数-平局数
提示：（想办法记录一下计算胜率需要的数据，然后就可以算出结果）

"""

print("************第一题***********")
for i in range(1,10):
    for j in range(1,10):
        if i < j:
            continue
        print("{}*{}=".format(i,j),i*j,end=" ")
    print(" ")

print("***********第二题*************")
count = 0
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if (i != j) and (i != k) and (j != k):
                count += 1
                print(i,j,k)
print("组成了{}组互不重复的三位数".format(count))

print("***************第三题***********")

def add ():
    print(num1+num2)
def reduce ():
    print(num1-num2)
def multiplication():
    print(num1*num2)
def division():
    print(num1/num2)
num1 = float(input("请示入第一组数字："))
num2 = float(input("请输入第二组数字："))
choice = int(input("请选择 ：加【1】 减【2】 乘【3】 除【4】："))
if choice ==1:
    add()
elif choice ==2:
    reduce()
elif choice == 3:
    multiplication()
elif choice ==4:
    division()
else:
    print("请输入正确的数字:")


print("***************第四题***********")
import random
a = 0
b = 0
c = 0
print("---石头剪刀布游戏开始---\n请按下面提示出拳：\n石头【1】 剪刀【2】 布【3】 退出【4】")
while True:
    c +=1
    num2 = random.randint(1, 3)
    num1 = int(input("请输入你的选项："))
    dic = {1: "石头", 2: "剪刀", 3: "布"}
    #    print("电脑：",num2,"\n本人:",num1)
    if (num1 == 1 and num2 == 2) or (num1 == 2 and num2 == 3) or (num1 == 3 and num2 == 1):
        print("您出拳为：{}，电脑出拳：{}，您胜利了".format(dic[num1], dic[num2]))
        a += 1
    elif num1 == num2:
        print("平局")
        b += 1
    elif num1 == 4:
        print("游戏结束")
        break
    else:
        print("您出拳为：{}，电脑出拳：{}，您失败了".format(dic[num1], dic[num2]))
print("您的胜率{:.2%}".format(a/(c-b)))
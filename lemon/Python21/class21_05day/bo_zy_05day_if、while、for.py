"""
============================
author:Administrator
time:2019/7/31
E-mail:540453724@qq.com
============================
"""
"""
1、一家商场在降价促销。如果购买金额50-100元(包含50元和100元)之间，会给10%的折扣，
如果购买金额大于100元会给20%折扣。编写一程序，询问购买价格，再显示出折扣（%10或
20%）和最终价格。
2、一个 5 位数，判断它是不是回文数。例如： 12321 是回文数，个位与万位相同，十位与千位相
同。 根据判断打印出相关信息。
3、利用random函数生成随机整数，从1-9取出来。然后输入一个数字，来猜，如果大于，则打
印大于随机数。小了，则打印小于随机数。如果相等，则打印等于随机数
4、使用循环和条件语句完成剪刀石头布游戏，提示用户输入要出的拳 ：石头（1）／剪刀（2）／布（3）/退出（4）
电脑随机出拳比较胜负，显示用户胜、负还是平局。运行如下图所示：


"""
print("*************第一题**************")
price = int(input("请输入购买价格："))
if price < 0:
    print("输入的价格有误")
elif price > 100 :
    print(price-price*0.2)
elif price >= 50 :
    print(price-price*0.1)
else:
    print(price)

print("*************第二题**************")
number = input("请输入一个5位数：")
if len(number) < 5 or len(number) > 5:
    print("请输入正确的5位数")
elif number[0] == number[4] or number[1] == number[3]:
    print("您输入的是回文数")
else:
    print("您输入的不是回文数")

print("*************第三题**************")
import random
number1 = random.randint(1,9)
print("随机数：",number1)
number2 = int(input("请输入数字："))
if number2 > number1 :
    print("大于随机数")
elif number2 < number1:
    print("小于随机数")
else:
    print("等于随机数")

print("*************第四题**************")
import random
print("---石头剪刀布游戏开始---\n请按下面提示出拳：\n石头【1】 剪刀【2】 布【3】 退出【4】")
while True:
    num2 = random.randint(1, 3)
    num1 = int(input("请输入你的选项："))
    dic = {1:"石头",2:"剪刀",3:"布"}
#    print("电脑：",num2,"\n本人:",num1)
    if (num1 == 1 and num2 == 2) or (num1 == 2 and num2 == 3) or (num1 == 3 and num2 == 1):
        print("您出拳为：{}，电脑出拳：{}，您胜利了".format(dic[num1],dic[num2]))
    elif num1 == num2 :
        print("平局")
    elif num1 == 4:
        print("游戏结束")
        break
    else:
        print("您出拳为：{}，电脑出拳：{}，您失败了".format(dic[num1],dic[num2]))

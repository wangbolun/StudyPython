"""
============================
author:Administrator
time:2019/7/30
E-mail:540453724@qq.com
============================
"""

"""
while 循环

关键字 ：while

"""

# 打印100 遍


# i = 0
# while i < 100:
#     i += 1
#     print("这个是第{}遍hello python".format(i))


# 死循环

# 使用while 循环 ，一定要加上循环终止的条件

# while True:
#     # break 终止循环，跳出循环体
#     # continue 终止当前循环，进入下一个循环
#     print("111111111222111")
# users = {"user": "python", "pwd": "lemeon"}
# while True:
#     user = input("请用户输入账号")
#     pwd = input("请输入密码")
#     if user == users.get("user") and pwd==users.get("pwd"):
#         print("您输入的账号密码正确，登录成功")
#         break
#     else:
#         print("您输入账号或密码不正确")


# continue 终止当前循环，进入下一个循环
# 关键字   if else elif while pass break contuiue


num = 0

while num < 7:
    num += 1

    if num == 5:
        continue
    print(num)
    # break
else:
    print("while中的else---")


if 3>0:
    print(">")
else:
    print("<")
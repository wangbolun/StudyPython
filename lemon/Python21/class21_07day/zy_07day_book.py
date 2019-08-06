"""
============================
author:Administrator
time:2019/8/5
E-mail:540453724@qq.com
============================
"""


def print_menu():
    print('---------------------------------------')
    print('【1】：添加图书')
    print('【2】：删除图书')
    print('【3】:显示所有图书')
    print('【4】：退出')
boosk = []
def add_book():
    dic = {"id": input("请输入图书编号："), "name": input("请输入图书名称："), "location": input("请输入图书位置：")}
    boosk.append(dic)
    print(boosk)
    print("添加完毕，返回菜单界面")
def del_book():
    bid = input("请输入删除的书名：")
    n = 0
    for i in range(0, len(boosk) - 1):
        l = boosk[i].get("name")
        if l == bid:
            n = n + 1
            print(boosk[i])
            print("找到{}本书籍名为：".format(n), bid)
            del (boosk[i])
    print("找到{}本书籍名为：".format(n), bid)

    print("请选择删除的编号：")
def all_book():
    print("您当前共有{}本书籍，所有图书信息如下：".format(len(boosk)))
    for i in range(len(boosk)):
        l = boosk[i]
        print("编号：{} 书名：{} 位置：{}".format(l.get("id"), l.get("name"), l.get("location")))
    print("查询完毕返回菜单界面")
    return
def main2():
    print("----------欢迎进入图书管理系统-----------")
    while True:
        print_menu()
        num = input('请输入您的选项：')
        if num == '1':
            add_book()
        elif num == '2':
            del_book()
        elif num == '3':
            all_book()
        elif num == '4':
            print('谢谢使用，程序即将关闭')
            break
        else:
            print('您选择的有误，请重新选择')
    return
main2()

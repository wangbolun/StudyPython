"""
============================
author:Administrator
time:2019/8/4
E-mail:540453724@qq.com
============================
"""

"""
1、什么是全局变量？ 什么是局部变量？
2、函数内部如何修改全局变量？
3、将本周学的控制流程和函数整理成思维导图
4、根据下面运行流程图和提示，实现文字版图书管理功能。


"""

print("************第一题**************")
"""
全局变量：直接定义在模块（py中的变量），在整个文件中任何地方都能够访问

局部变量：定义在函数中的，它的作用范围，仅限于当前的作用域（定义的函数中）

"""

print("************第二题**************")

"""
通过global在函数中声明全局变量，如下示例：

"""
a = 100
def sun():
    global a
    a = 10
    print(a)
sun()
print(a)

print("************第四题**************")
def print_menu():
    print('---------------------------------------')
    print('【1】：添加图书')
    print('【2】：删除图书')
    print('【3】:显示所有图书')
    print('【4】：退出')
boosk = []
all_boosk = []
def add_book():
    tic = {"id":input("请输入图书编号："),"name":input("请输入图书名称："),"location":input("请输入图书位置：") }
    boosk.append(tic["id"])
    all_boosk.append(tic)
    print(boosk)
    print(all_boosk)
    print("添加完毕，返回菜单界面")
def del_book():
    name = input("请输入删除的书名")
    n = 0
    for name in all_boosk["name"]:
        n = n+1
        print("找到{}本书籍名为：".format(n),name)
        print()
    dbook = input("请选择删除书籍的编号：")
def all_book():
    print("您当前共有{}本书籍，所有图书信息如下：".format(len(boosk)))
    print(boosk)
    print("查询完毕返回菜单界面")
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
main2()

"""
1、一、输出99乘法表，结果如下：（提示嵌套for循环，格式化输出）

2、有1 2 3 4 这四个数字，设计程序计算能组成多少个互不相同且无重复数字的3位数？分别是什么？

3、通过函数实现一个计算器，运行程序分别提示用户输入数字1，数字2，然后再提示用户选择 ： 
加【1】    减【2】    乘【3】      除【4】，
每个方法使用一个函数来实现， 选择后调用对应的函数，然后返回结果。

4、对上次作业的石头剪刀布游戏升级，游戏一轮出拳后进入下一轮，
当选择结束游戏后，打印本次游戏的胜率：    胜利的次数  /玩的总次数-平局数
提示：（想办法记录一下计算胜率需要的数据，然后就可以算出结果）

"""
# 第一题
print('-----------------1-----------------------')


def mul_table():
    for i in range(1, 10):
        for j in range(1, i + 1):
            print('{} * {} = {:<4d}'.format(j, i, i * j), end='')
        print()

# mul_table()
print('-----------------2-----------------------')


# 第二题

def count_num():
    count = 0
    for a in range(1, 5):
        for b in range(1, 5):
            for c in range(1, 5):
                if a != b and c != b and a != c:
                    print(a, b, c)
                    count += 1
    print('一共有{}个'.format(count))

# count_num()
# 第三题:
print('-----------------3-----------------------')


def compute_number():
    print('欢迎使用计算器')
    a = int(input('请输入数字1:'))
    b = int(input('请输入数字2:'))
    print('功能提示:【1】加 【2】减【3】乘 【4】除')
    num = input('请选择：')
    if num == '1':
        return add(a, b)
    elif num == '2':
        return sub(a, b)
    elif num == '3':
        return mul(a, b)
    elif num == '4':
        return div(a, b)
    else:
        print('没有此选项！')


def add(a, b):
    """加法"""
    return a + b


def sub(a, b):
    """减法"""
    return a - b


def mul(a, b):
    """乘法"""
    return a * b


def div(a, b):
    """除法"""
    return a / b

#
# res = compute_number()
# print(res)

print('-----------------4-----------------------')


# 第四题
def game():
    import random
    li = ['石头', '剪刀', '布']
    print('---石头剪刀布游戏开始----')
    count_win = 0  # 赢的次数
    count_sum = 0  # 游戏的总次数
    count_flat = 0  # 平局次数
    while True:
        print('请按下面提示出拳：')
        print('石头【1】 剪刀【2】 布【3】 结束游戏【4】')
        num_5 = int(input('请输入你的选项：'))
        r_num = random.randint(1, 3)
        if 1 <= num_5 <= 3:
            count_sum += 1
            if r_num == num_5:
                print('您的出拳为:{}，电脑出拳:{}，平局'.format(li[num_5 - 1], li[r_num - 1]))
                count_flat += 1
            elif (num_5 - r_num) == -1 or (num_5 - r_num) == 2:
                count_win += 1
                print('您的出拳为:{}，电脑出拳:{}，您胜利了'.format(li[num_5 - 1], li[r_num - 1]))
            else:
                print('您的出拳为:{}，电脑出拳:{}，您输了'.format(li[num_5 - 1], li[r_num - 1]))
        elif num_5 == 4:
            break
        else:
            print('您出拳有误，请按规矩出拳')

    print('本次游戏您完了{}次，赢了{}次,平局{}次，您的胜率为{:.2%}'.format(
        count_sum, count_win, count_flat, count_win / (count_sum - count_flat)))




# game()
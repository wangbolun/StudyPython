"""
============================
author:Administrator
time:2019/7/25
E-mail:540453724@qq.com
============================
"""
"""
字符串方法
find：查找字符下标位置
count：查找字符串的出现的次数
replace（'a','h'）指定替换字符
split:分割
join： 拼接
upper：将小写转换为大写
lower： 大转小

format 格式化

"""
#
# sttr1 = 'ajhnkahij445'
# # 字符串分割
# res = sttr1.split('a')
# print(res)


# 替换
# res = sttr1.replace('a','h')
# print(res)

# 格式化输入
#format    {}占位符
# str4 = "今收到{}，交来学费{}，日期{}"
# print(str4.format('小明','8000','2019-7-25'))
# # 保留小数{：.2f}
str5 = "今收到{}，交来学费{:.2f}，日期{}"
print(str5.format('小明',8000.03,'2019-7-25'))

#%s 万能占位符   s字符串   d 数值类型    f浮点类型

str6 = "这位同学叫{}，今年：{}岁，银行卡余额：{}"
print(str6.format('小明',18,99.99))
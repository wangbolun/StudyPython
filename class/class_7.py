#字符串内建函数
str_1='hello'
str_2='PYTHON'
#1大小写切换upper() lower()
res=str_1.upper()
print('转换后的结果{}'.format(res))
res=str_2.lower()
print('转换后的结果{}'.format(res))

#2字符串的查找 find()
res = str_1.find('o')
print('转换后的结果{}'.format(res))
#单个字符 如果能够找到就返回单个字符在字符串里面的索引值
#子字符串 如果能够找到就返回子字符在字符串里面的第一个元素在远字符串里面的索引值
#没找到返回-1

#3字符串替换 replace()
res=str_1.replace('l','花花')  #目标字符  转换的内容
print('转换后的结果{}'.format(res))

#4字符串切片 split()
res=str_1.split('o')
print('转换后的结果{}'.format(res))

#5字符串头尾的处理strip()
res=str_1.strip('o')
print('转换后的结果{}'.format(res))

#字典内建函数
#1 :clear()清空字典
#2：items()以列表返回可遍历(键值)元祖数组
#3：keys()以列表返回椅子字典所有的建
#4 values() 以列表返回所有的值
#5 pop(key):删除制定key的字典值，会返回被删除的这个值
#6 del 字典名[key]删除指定key的字典值
#7 popitem():随机删除一组数据
#8 setdeault(key,value) 如果key存在则返回值value值，否则加入key-value
#9 A.uodata(B字典) 把A字典与B字典合并，如果key重复，则选择B中的内容

a = {'name':"博伦",'age':18,'money':99.99,'score':[100,100,80]}
#增删改查
#增加元素
a['class']='柠檬班'
print('修改之后的字典值{}'.format(a))

#修改元素
a['name']='柠檬班王搏伦'
print('修改之后的字典值{}'.format(a))

#查询 字典名[key]
print('字典里面的姓名是：{0}'.format(a['name']))

#删除字典名.pop(key)  依据key去做删除
a.pop('age')
print('删除之后的字典：{0}'.format(a))

#删除

del a['money'] #del 字典名[key]
print(a)
#随机删除
a.popitem()
print(a)
#清空
#a.clear()
#print(a)
#单独取值
print(a.keys())
print(a.values())
print(a.items())
#字典合并  c值更新到a   c里面的key如在a里面存在把C更新到a
a = {'name':"博伦",'age':18,'money':99.99,'score':[100,100,80]}
c = {'name':"柠檬班王搏伦",'age':'未知'}
a.update(c)
print(a)
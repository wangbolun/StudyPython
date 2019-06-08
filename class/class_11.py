#字典
#1：标志{}关键字dict
#2：a={}空字典
#3：字典的数据格式key:value键值
#4 :字典里面value 可以是任何数据
#5：取值方式：根据key取值 字典名[key]
a = {'name':"博伦",'age':18,'score':99.99,'money':[100,100,80]}
print(a)
print(a['age'])

#6新增元素 字典名 [new_key] = value
a["sex"]='girl'

print(a)

#7修改元素的值
a['sex']='boy'
print(a)

#删除操作
a.pop('score') #删除
print(a)
a.clear()#清空
print(a)
#列表内建函数
#列表支持赠删减加
a = [1,0.05,'wang',(1,2,3),[4,5,6]]
#1新增操作 append() 家园素到最后面每次只能加一个
# 、insert到指定位置
a.append('王搏伦')
print(a)
a.insert(0,"博伦")
print(a)

#2修改列表元素值  重新赋值  =赋值运算浮
a[-1]="热爱学习的我"
print(a)

#3删除操作  列表名.pop(index) 删除列表制定位置元素   不赋值删除末尾
a = [1,0.05,'wang',(1,2,3),[4,5,6]]
a.pop(0)
print(a)

#4其他操作   排序
c=[7,5,6,3,1]
#排序.sort
c.sort()
print(c)
#到装reverse
c.reverse()
print(c)

#清空.clear()
c.clear()
print(c)
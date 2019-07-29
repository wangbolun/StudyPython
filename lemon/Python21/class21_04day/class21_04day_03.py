"""
============================
author:Administrator
time:2019/7/28
E-mail:540453724@qq.com
============================
"""

""""
字典：
方式一
字典的定义{key:calue}
key :唯一不重复
calue : python中任何数据
方式二：dict


字典增删查改的方法：
添加和修改：键+值   有责该无则加
查询    通过键查询
get   查找元素    好处，键不存在的时候不会报错



"""

dict1 = {"name": "小明", "age": 18, "moble": 17600108234}
print(dict1)
print(type(dict1))

dict2 = dict(
    name="小明",
    age=18,
    gender="男"
)

dict2["phone"] = "264513"
print(dict2)

print(dict2.get("name"))

# 查找方法  键值对获取
print(list(dict2.items()))
# 获取所有的键
print(list(dict2.keys()))
# 获取所有的值
print(list(dict2.values()))

dict1 = {"name": "小明", "age": 18, "moble": 17600108234}
print(dict1)
# pop  指定键删除
print(dict1.pop("name"))
print(dict1)

# popitem删除最后一个
#print(dict1.popitem())

del dict1["name"]

print(dict1)
# upper 更新到
dict2.update({})

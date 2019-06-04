age=18
name='柠檬班王搏伦'
score=99.9
#print(name+", 今年"+str(age))

#格式化输出%d整数 %f浮点数 %s字符串
print("%s今年%d岁,数学考了%.2f"%(name,age,score)) #按顺序赋值 #%.2小数点后两为
#%d必须放整数 %s可以放任意值

#第二种输出方式format{}
print("{0}今年数学考了{1}".format(name,score))
#{}里面不指定数值 按顺序
#{}里面制定数值 就会按设置的取值
#format里面数据有索引，从0开始标定数据也


""" def func(name,age,*args,**kwargs):
    print(f"我是{name},年龄{age}岁,我的爱好是{args},我的其他信息是{kwargs}")
    
    print()

func("张三",18,"打篮球","唱歌",function="男",high=180,weight=70)



#函数作为 参数传递
def add(x,y):
    return x+y
def sub(add):
    result = add(10,5)
    print(f"计算结果是：{result}")

sub(add) """

def func(com):
    result = com(1,2)
    print(result)

func(lambda x,y:x + y)
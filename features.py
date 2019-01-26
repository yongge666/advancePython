# coding:utf8
# python中的一些特性
def fun1(x,y):
    print(x,y)

def fun2(x=[]):
    x.append(1)
    print(x)

def fun3(x=None):
    if x is None:
        x = []
    x.append(1)
    print(x)

if __name__ == '__main__':

    # 1.函数参数解包
    lis = [1,2]
    fun1(*lis)
    dic = {"x":1,"y":2}
    fun1(**dic)

    # 2.函数默认参数陷阱
    fun2() #[1]
    fun2() #[1, 1]
    fun2() #[1, 1, 1]
    fun3()
    fun3()

    #3.链式比较
    x = 3
    print(1<x<5)

    #4.三元运算符
    y = 5
    small = x if x<y else y
    print(small)

    #5.字典get方法
    print(dic.get("z")) #None
    print(dic.get("z","默认值")) #默认值


    # 6.带关键字的格式化





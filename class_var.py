# coding:utf8
class A:
    b = 1
    def __init__(self, x, y):
        self.x = x
        self.y = y

a = A(2,3)
a.b = 100 #改变的是实例变量
print(a.x,a.y,a.b)
print(A.b) # 类变量可以直接通过类名访问

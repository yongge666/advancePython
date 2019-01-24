# coding:utf8
# 魔法函数
## 非数学运算
### 集合序列相关
#### __len__
#### __getitem__
#### __setitem__
#### __delitem__
#### __contains__

### 迭代相关
####__iter__
####__next__
### 可调用
####__call__

### with上下文管理
#### __enter__
#### __exit__

### 数值转换
#### __abs__
#### __bool__
#### __int__
#### __float__
#### __hash__
#### __index__

### 元类相关
#### __new__
#### __init__

### 属性相关
#### __getattr__,_setattr__
#### __getattribute__,__setattribute__
#### __dir__


### 属性描述符
#### __get__,__set__,__delete__

### 协程
#### __await__,__aiter__,__anext__,__aenter__,__aexit__

## 数学运算
### 一元运算符
#### __neg__（-）、__pos__（+）、__abs__
### 二元运算符
#### __lt__(<)、 __le__ <= 、 __eq__ == 、 __ne__ != 、 __gt__ > 、 __ge__ >=
### 算数运算符
#### __add__ + 、 __sub__ - 、 __mul__ * 、 __truediv__ / 、 __floordiv__ // 、 __mod__ % 、 __divmod__ divmod() 、 __pow__ ** 或 pow() 、 __round__ round()
### 反向算数运算符
#### __radd__ 、 __rsub__ 、 __rmul__ 、 __rtruediv__ 、 __rfloordiv__ 、 __rmod__ 、__rdivmod__ 、 __rpow__
### 增量赋值算术运算符
#### __iadd__ 、 __isub__ 、 __imul__ 、 __itruediv__ 、 __ifloordiv__ 、 __imod__ 、__ipow__
### 位运算符
#### __rlshift__ 、 __rrshift__ 、 __rand__ 、 __rxor__ 、 __ror__
### 反向位运算符
#### __rlshift__ 、 __rrshift__ 、 __rand__ 、 __rxor__ 、 __ror__
### 增量赋值位运算符
#### __ilshift__ 、 __irshift__ 、 __iand__ 、 __ixor__ 、 __ior__

class Employee(object):
    def __init__(self,employee_list):
        self.employee = employee_list
    def __getitem__(self, item):
        return self.employee[item]

# _repr__用于所有其他的环境中：用于交互模式下提示回应以及repr函数，如果没有使用__str__，会使用print和str。它通常应该返回一个编码字符串，可以用来重新创建对象，或者给开发者详细的显示
    
    def __repr__(self):
        return ",".join(self.employee)

    def __str__(self):
        return ",".join(self.employee)

class Vector():
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self, other):
        print("ox:{x},oy:{y}".format(x=other.x,y=other.y))
        return Vector(self.x+other.x,self.y+other.y)

    def __str__(self):
        return "x:{x},y:{y}".format(x=self.x,y=self.y)

if __name__ == "__main__":
    employee = Employee(["n1","n2","n3"])
    for e in employee.employee:
        print(e)

    # __getitem__这个魔法函数使得Employee这个类可以迭代，同样也可以切片
    employee2 = Employee(["n1","n2","n3"])
    for e in employee2:
            print(e)

    employee3 = Employee(["a","b","c"])
    employee4 = employee3[:2]
    print(len(employee4))
    for e in employee4:
        print(e)

    print("=============str===================")
    employee3
    print(employee) # 因为有魔术方法，会调用__str__
    print("=============add===================")
    print(Vector(1,2)+Vector(2,3))
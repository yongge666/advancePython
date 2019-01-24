# coding:utf8
# object type class之前的关系
# type是一个类也是一个对象，他是自身的实例也是object的实例
# type是object的实例，list，str，dict,tupl等都继承object，同事也都是type的实例
# "abc"是str的实例
# 所以说list，str，dict,tupl不仅是一个类还是一个对象，他们都是type的对象
# 类一旦生成对象就很难修改，但是list，str，dict,tupl即是类也是对象就很灵活
if __name__ == "__main__":
    a = 1
    print(type(1))  #class 'int'
    print(type(a))  #class 'int'
    print(type(int)) #class 'type'
    # type->int->1
    # type->class->obj

    class Student:
        pass
    stu = Student()
    print(type(Student)) #<class 'type'>
    print(type(stu)) #<class '__main__.Student'>

    b = [1,2]
    print(type(b)) #<class 'list'>
    print(type(list)) #<class 'type'>

    class Mystudent(Student):
        pass

    # Object是最顶层基类
    print(Student.__bases__) #(<class 'object'>,)
    print(Mystudent.__bases__) #(<class '__main__.Student'>,)
    print(object.__bases__) #()
    # type是一个类，
    print(type.__bases__) #(<class 'object'>,)

    print(type(object)) #<class 'type'>

    # 数据类型及引用
    a = 1
    print(id(a)) #2012992560
    b = a
    print(id(b)) #2012992560
    b = 3
    print(id(a), id(b)) #b的地址变了cow机制

    # None是全局对象，全局只有一个
    a = None
    b = None
    print(id(a) == id(b)) #True

    # 数值类型 int float，complex，bool
    # 迭代类型
    # 序列类型 list，bytes，bytearray，memoryview(二进制序列),range,tuple,str,array
    # 映射 dict
    # 集合 set frozenset
    # 上下文管理类型 with
    # 其他 模块类型，class和实例，函数类型，方法类型，代码类型，object对象，type类型，ellipsis类型，notimplemented类型




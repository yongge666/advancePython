# coding:utf8
# python自省是通过一定的机制查询到对象的内部结构
class Person():
    # 单行注释
    '''
    这是注释1
    '''
    a=1
    # 注释2
    b="s1"
    '''
    这是注释3
    '''

class Student(Person):
    def __init__(self,school_name):
        self.school_name = school_name
        self.__a = "111"

if __name__ == '__main__':
    user = Student("家里蹲大学")
    print(user.__dict__)
    # print(user.__a)
    print(user._Student__a)
    print(user.__dict__["school_name"])
    user.__dict__["school_name"] = "北大"
    user.__dict__["_Student__a"] = "222"
    print(user.__dict__)
    print(Student.__dict__)
    print(Person.__dict__)
    print(Person.__dict__["__doc__"]) #获取第一个多行注释
    print(dir(user)) #获取对象所有属性
    list = [1,2]
    print(dir(list))

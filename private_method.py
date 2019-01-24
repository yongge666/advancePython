# coding:utf8
from class_method import Date
class User:
    def __init__(self,birthday):
        self.__birthday = birthday  # __开头的变量为私有变量

    def get_age(self):
        return 2018 - self.__birthday.x

if __name__ == '__main__':
    user = User(Date(1990,2,1))
    print(user._User__birthday)  # 私有属性的外部访问（只是为了编码规范）
    print(user.get_age())


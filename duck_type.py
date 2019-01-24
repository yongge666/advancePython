# coding:utf8
class Cat(object):
    def say(self):
        print("I am a cat")

class Dog(object):
    def say(self):
        print("I am dog")

if __name__ == "__main__":

    # 不用管animal具体是什么类型，只要有say方法就可以调用
    obj_list = [Cat,Dog]
    for animal in obj_list:
        animal().say()

    a = ["a1","a2"]
    b = ["a3","a4"]
    c = set()
    c.add("a5")
    c.add("a6")
    a.extend(b)
    print(a)
    b.extend(c)
    print(b)



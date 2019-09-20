#python和java中的变量本质不一样，python的变量实质上是一个指针 int str， 便利贴

a = 1
a = "abc"
#1. a贴在1上面
#2. 先生成对象 然后贴便利贴

a = [1,2,3]
b = a
# print (id(a), id(b))  #cow机制，指向同一个地址
# print (a is b)
# b.append(4)
# print (a)
c = 1
d = 1
print("c is d:",c is d)


e = [1,2,3,4]
f = [1,2,3,4]
# print(a == b)
print("e is f:",e is f) #False,可变类型不会指向同一个地址

g = "a"
h = "a"
print("g is h",g is h) #不可变类型，python内部解释器做了优化，只要值相同，声明后指向同一块内存空间

class People:
    pass

person = People()
if type(person) is People:
    print ("yes")


# coding:utf8
'''
           A
     B          C
           D
当继承关系如上时，python如何进行属性查找
'''

# python3所有自定义类默认继承object
class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B,C):
    pass

# print(D.mro())  # [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]



'''
   H             L
   F             G
         E
当继承关系如上时python又该如何查找
'''

class H:
    pass

class L:
    pass

class F(H):
    pass

class G(L):
    pass

class E(F,G):
    pass
if __name__ == '__main__':
    # print(E.mro())  #[<class '__main__.E'>, <class '__main__.F'>, <class '__main__.H'>, <class '__main__.G'>, <class '__main__.L'>, <class 'object'>]
    print(E.__mro__)
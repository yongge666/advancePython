class A:
    pass

class B(A):
    pass

b = B()

print(isinstance(b, B))
print(isinstance(b, A))

print(type(b) is B)
print(id(type(b)),id(B))  #is的本质是比较地址，==是比较值
print(type(b) is A)


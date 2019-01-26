# coding:utf8
# python中的序列
## 容器序列 （可以接受任意类型，可以混合）
### list,tuple,deque
## 扁平序列(只能存放同一种数据类型)
### str,bytes,bytearray,array.array
## 可变序列
### list,deque,bytearray,array(可以增加修改数据)
## 不可变序列
### str,tuple,bytes(不能增加修改)
if __name__ == '__main__':

    a = [1,2]
    a.append(3)
    print(a)
    b= a+[4,5]
    print(b)
    b.extend(range(6,9))
    print(b)
    b.extend((10,11,12))
    print(b)

    # append注意事项,append一个序列时，会把这个序列整个作为一个值，而extend会迭代append进去
    a.append([6,7])
    print(a)


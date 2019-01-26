# coding:utf8

# 列表推导式，用最简洁的方式遍历可迭代对象生成需要的格式
if __name__ == '__main__':
    lis = [1,2,3,4,5]
    list1 = [v*v for v in lis]
    print(list1)
    li = [1,2,-3,4,5]
    # li1 = [v if v<0 abs(v)  for v in li]

    for i, item in enumerate(lis):
        print(i, item)

    # 字典 (python2中range生成数组，xarange是一个生成器，python3已将其合并)
    my_dict = {i: i*i for i in range(10)}
    print("my_dict",my_dict)

    # 集合
    my_set = {i*i for i in range(10)}
    print("my_set:",my_set)

    print(list(enumerate('abc', 2)))  # [(2, 'a'), (3, 'b'), (4, 'c')]


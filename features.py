# coding:utf8
# python中的一些特性
def fun1(x,y):
    print(x,y)

def fun2(x=[]):
    x.append(1)
    print(x)

def fun3(x=None):
    if x is None:
        x = []
    x.append(1)
    print(x)

if __name__ == '__main__':

    # 一.函数
    ## 1.函数参数解包
    lis = [1, 2]
    fun1(*lis)
    dic = {"x": 1, "y": 2}
    fun1(**dic)

    # 2.函数默认参数陷阱
    '''
    如果参数默认值是在函数编译compile阶段就已经被确定。之后所有的函数调用时，如果参数不显示的给予赋值，
    那么所谓的参数默认值不过是一个指向那个在compile阶段就已经存在的对象的指针。如果调用函数时，没有显示指定传入参数值得话。
    那么所有这种情况下的该参数都会作为编译时创建的那个对象的一种别名存在。如果参数的默认值是一个不可变(Imuttable)数值，
    那么在函数体内如果修改了该参数，那么参数就会重新指向另一个新的不可变值。而如果参数默认值是和本文最开始的举例一样，是一个可变对象(Muttable)，那么情况就比较糟糕了。
    所有函数体内对于该参数的修改，实际上都是对compile阶段就已经确定的那个对象的修改。
    '''
    fun2()  # [1]
    fun2()  # [1, 1]
    fun2()  # [1, 1, 1]
    fun3()
    fun3()

    # 二.运算
    ## 1.强制浮点
    #from __future__ import division #只能在文件头部引入
    result = 1 / 2
    # print(result)
    # 0.5

    # 三.运算符
    ## 1.python中的== 和 is
    '''
    python中的对象包含三要素: id, type, value
    id
    用来标识唯一一个对象，type标识对象的类型，value用来设置对象的值。
    is 判断是否是一个对象，使用id来判断的。
    == 是判断a对象的值是否是b对象的值，默认调用它的__eq__方法。
    '''
    ## 2.链式比较
    x = 3
    print(1 < x < 5)

    ## 3.三元运算符
    y = 5
    small = x if x < y else y
    print(small)

    ## 4.单下划线_
    '''
    命令行模式中表示上一条语句的返回值
    果你写了代码 : from <模块/包名> import * ，那么以 _ 开头的名称都不会被导入，除非模块或包中的 __all__ 列表显式地包含了它们
    '''
    print("=========================单下划线_=============================")
    ## 如果不需要执行次数变量，可以这样玩，更高校
    n = 2
    for _ in range(n):
        print("do sth")
    ## 5.isinstance可以接收一个元组
    isinstance(1, (float, int)) #True
    isinstance(1.3, (float, int)) #True
    isinstance("1.3", (float, int)) #False


    # 四 .推导式
    ## 1.嵌套列表推导式(为了编码的清晰易懂，不建议使用复杂的推导式)
    print("=========================嵌套列表推导式=============================")
    set_in_lis = [(i,j) for i in range(3) for j in range(i)]
    print(set_in_lis)

    num = [1, 4, -5, 10, -7, 2, 3, -1]
    filtered_and_squared = map(lambda x: x ** 2, filter(lambda x: x > 0, num))
    print(filtered_and_squared) # [1, 16, 100, 4, 9]

    ## 更简化的一种写法
    num = [1, 4, -5, 10, -7, 2, 3, -1]
    filtered_and_squared = [x ** 2 for x in num if x > 0]
    print(filtered_and_squared)# [1, 16, 100, 4, 9]
    # 生成器表达式同列表推导式有着几乎相同的语法结构，区别在于生成器表达式是被圆括号包围，而不是方括号：
    num = [1, 4, -5, 10, -7, 2, 3, -1]
    filtered_and_squared = (x ** 2 for x in num if x > 0)
    print(filtered_and_squared)

    # <generator object <genexpr> at 0x00583E18>

    for item in filtered_and_squared:
        print(item)

    ## 通过两阶列表推导式遍历目录
    import os

    def tree(top):
        for path, names, fnames in os.walk(top):
            for fname in fnames:
                yield os.path.join(path, fname)


    for name in tree("C:\\Users\\Public\\Libraries"):
        print(name)

    # 五.优化循环（尽量避免在python中使用.操作符）
    lowerlist = ['this', 'is', 'lowercase']
    upper = str.upper
    upperlist = []
    append = upperlist.append
    for word in lowerlist:
        append(upper(word))
        print(upperlist)
        # Output = ['THIS', 'IS', 'LOWERCASE']

    n = 16
    myDict = {}
    for i in range(0, n):
        char = 'abcd'[i % 4]
        if char not in myDict:
            myDict[char] = 0
            myDict[char] += 1
            print(myDict)

    #由于char not in myDict是极少数情况，可以改成如下的写法
    n = 16
    myDict = {}
    for i in range(0, n):
        char = 'abcd'[i % 4]
        try:
            myDict[char] += 1
        except KeyError:
            myDict[char] = 1
        print(myDict)

    # 五.数据类型的特性
    ## 遍历过程中不能删除列表元素
    print("=========================遍历过程中不能删除列表元素=============================")
    def odd(n):
        if n%2 == 0:
            return True
        else:
            return False

    numbers = [n for n in range(10)]
    for i in numbers:
        if i%2==0:
            # del numbers[i]  # BAD: Deleting item from a list while iterating over it
            pass

    numbers[:] = [n for n in numbers if not odd(n)]
    print(numbers)

        ## zip和unzip
    ## 将两个元素相等的列表组装成一个列表元组
    a = [1, 2, 3]
    b = ['a', 'b', 'c']
    z = zip(a, b)
    print(z) #[(1, 'a'), (2, 'b'), (3, 'c')]
    print( zip(*z) )  #[(1, 2, 3), ('a', 'b', 'c')]

    ## 自适应元组列表
    print("=========================自适应元组列表=============================")
    a = [1, 2, 3, 4, 5, 6]
    # Using iterators
    group_adjacent = lambda a, k: zip(*([iter(a)] * k))
    g = group_adjacent(a, 3)
    print(*g)#[(1, 2, 3), (4, 5, 6)]
    print(*group_adjacent(a, 2)) #[(1, 2), (3, 4), (5, 6)]
    print(*group_adjacent(a, 1)) #[(1,), (2,), (3,), (4,), (5,), (6,)]


    ## 字典zip
    print("=========================字典zip=============================")
    m = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    print(m.items()) #[('a', 1), ('c', 3), ('b', 2), ('d', 4)]
    m_zip = zip(m.values(), m.keys())
    print(*m_zip) #[(1, 'a'), (3, 'c'), (2, 'b'), (4, 'd')]
    print(*m_zip) #此处输出空，可见只能迭代一次
    m_zip2 = zip(m.values(), m.keys())
    mi = dict(m_zip2)
    print(mi) #{1: 'a', 2: 'b', 3: 'c', 4: 'd'}
    mi1 = dict(m_zip)
    print(mi1)  # {} *m_zip已经迭代过一次，无法再输出

    ## 解压列表
    print("=========================解压列表=============================")
    ### 方式1
    import itertools
    a = [[1, 2], [3, 4], [5, 6,[7,8]]]
    ali = list(itertools.chain.from_iterable(a)) #[1, 2, 3, 4, 5, 6, [7, 8]] 只会解压一层
    print(ali)

    ### 方式二
    ali2 = sum(a,[])
    print(ali2)

    ### 方式三 使用列表推导式
    # ali3 = [x for lis in a for v in lis for x in v]
    # ali3 = [x for l1 in a for l2 in l1 for x in l2]
    # print(*ali3)

    ## map推导式
    print("=========================map推导式=============================")
    m = {x: x ** 2 for x in range(3)}
    print(m)
    m = {x: 'A' + str(x) for x in range(3)}
    print(m)


    ## 1.字符串转列表
    print("=========================字符串转列表=============================")
    expr = "[1, 2, 3]"
    my_list = eval(expr)
    print(my_list)
    ## 使用下面的方式更高效
    import ast
    my_list = ast.literal_eval(expr) #可以转化任何可迭代对象
    print(my_list)


    ##1.字典get方法
    print("=========================字典get方法=============================")
    print(dic.get("z")) #None
    print(dic.get("z","默认值")) #默认值


    # 六.变量作用域
    # Python的作用域解析是基于LEGB规则，分别是Local、Enclosing、Global、Built-in。
    print("=========================变量作用域=============================")
    x = 10
    # 不可变类型函数体内无法访问
    # def foo():
    #     x += 1
    #     print(x)
    lst = [1,2,3]
    def foo1():
        lst.append(4)
        print(lst)

    foo1()
    print(lst)

    def foo2():
        # lst += [5] //报错。找不到lst
        pass

    '''
    为什么foo2失败而foo1运行正常？ 答案与前面那个例子是一样的，但又有一些微妙之处。foo1没有赋值给lst，而foo2赋值了。
    lst += [5]实际上就是lst = lst + [5]，试图给lst赋值（因此，假设Python是在局部作用域里）。然而，我们正在寻找指定给lst的值是基于lst本身，其实尚未确定
    '''

    # 七.性能优化
    ## 1.while 1 比 while true快很多

    ## 使用 cProfile, cStringIO 和 cPickle等用c实现相同功能（分别对应profile, StringIO, pickle）的包

    ## val, cPickle, json方式三种对相应字符串反序列化的效率，json比cPickle快近3倍，比eval快20多倍。








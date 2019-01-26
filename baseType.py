#!/usr/bin/python
# -*- coding: utf-8 -*-
# 一.列表
number_list = [1,3,5,7,9]
string_list = ['aaa','bbb','cccc',2,3]
list_1 = [1,1,1,1,1]#list元素可以重复 [1, 1, 1, 1, 1]

print(list_1)
print(number_list)
print(string_list)
print(3 in number_list)
## 遍历列表
for ele in string_list:
    print(ele)

## 产生递增列表
list_inc = range(10)
print(list_inc)
print(list_inc[6])#6
l1 = range(1,5)      #即 L=[1,2,3,4],不含最后一个元素
print(l1)
l2 = range(1, 10, 2) #即 L=[1, 3, 5, 7, 9]
print(l2)
## 用某个固定值初始化列表
initial_value = 0
list_length = 5
sample_list = [ initial_value for i in range(10)]
sample_list = [initial_value]*list_length
print(sample_list) # sample_list ==[0,0,0,0,0]
#print(list.count(1))
## 2.访问列表元素：
print(string_list[2])#cccc
print(string_list[-2])#2
print(len(string_list))
print(number_list+string_list)
## 3.追加列表元素
print(string_list)#['aaa', 'bbb', 'cccc', 2, 3]
string_list.append('yongge')   #追加元素到末尾  ['bbb', 'cccc', 'lee', 2, 3, 'yongge']
string_list.insert(2,'lee')#在第二个元素上追加lee，原本的第二个元素变成第三个
string_list.insert(3,'lee')#在第二个元素上追加lee，原本的第二个元素变成第三个
print(string_list)
print('_____________________________________________________________')
print(string_list.count('lee'))#2 该元素在列表中出现的个数
print(string_list.index('lee'))#2 该元素首次出现的位置,无则抛异常
### 3.1 append注意事项,append一个序列时，会把这个序列整个作为一个值，而extend会迭代append进去

## 4.列表不支持赋值修改
print(list_inc)
## 5.删除列表元素
print("===============================list删除===================================")
del string_list[0]
print(string_list);#['bbb', 'lee', 'lee', 'cccc', 2, 3, 'yongge']
string_list.pop()      #返回最后一个元素，并从list中删除之
print(string_list) #['bbb', 'lee', 'lee', 'cccc', 2, 3]
string_list.pop(4)
print(string_list) #['bbb', 'lee', 'lee', 'cccc', 3]
string_list.remove('lee')   #删除第一次出现的该元素
print(string_list)#['bbb', 'lee', 'cccc', 3]

## 6.切片详解
print("===============================list切片===================================")
# [start:end:step]
lis = [0,1,2,3,4,5,6,7,8,9]
str = "abcde"
print(lis[::]) # 返回所有
print(lis[::-1]) #返回所有元素的逆序
#字符串依然可以反转
print(str[::-1])
print(lis[::2]) #获取偶数位置的元素
print(lis[1::2]) #获取奇数位置的元素
print(lis[0:100]) #end超过能给多少给多少
print(lis[100:]) #start超过给空列表
lis[len(lis):] = [10] #尾部插入元素
# print(lis)
lis[:0] = [-2,-1] #头部插入
# print(lis)
lis[3:3] = "a" #指定位置插入
# print(lis)
lis[:3] = ["b","c"] #替换(以少换多)
# print(lis)
lis[:3] = ["d", "e","f","g"]  # 替换(以多换少)
# print(lis)
lis[:4] = [] #删除 等价于 del lis[:4]
# print(lis)
lis[::2] = ["a","b","c","d","e"] #修改偶数位置,元素个数必须相等
print(lis)


# 2.数组
# 数组
import array
#array和list的一个重要区别， array只能存放指定的数据类型
my_array = array.array("i")
my_array.append(1)
# my_array.append("abc") #报错


# 三.tuple元组，比列表效率高，可以相互转化
## 1.元组使用细节
tuple_1 = (2,)#一个tuple要用逗号分隔

## 2.元组的元素可以是任意类型
tuple_mixed = (1,2,string_list);
print(tuple_mixed);#(1, 2, ['bbb', 'cccc', 2, 3])
## 4.访问元组中的列表元素
print(tuple_mixed[2][1])#cccc
## 5.tuple不支持改值，删除和增加,但是可以改列表的元素值
#tuple_mixed[0] = 3;
tuple_mixed[2][1] = 'dddddd';#(1, 2, ['bbb', 'dddddd', 2, 3])
print(tuple_mixed)
## 6.元组中的元素可以重复
tuple_3 = (3,3,1)

print(tuple_3)
tuple_4 = tuple_1 + tuple_mixed
## 7.不去重合并
print(tuple_4);#(2, 1, 2, ['bbb', 'dddddd', 2, 3])

## 8.相互转化
tuple_trans = tuple(string_list)
print(tuple_trans)#(2, 1, 2, ['bbb', 'dddddd', 2, 3])

list_trans = list(tuple_4)
print(list_trans)#[2, 1, 2, ['bbb', 'dddddd', 2, 3]]

## 9.拆包（常用特性，取出元组元素并逐一赋值）
print("===============================tuple拆包===================================")
(x,y,z) = tuple_3;
print(x)
x,*other = tuple_3 #部分拆包
print(x) #3
print(other) #[3, 1]


# 四.dcit(通过c语言实现，非常高效，可hash）
## 统计list中相同元素的个数
print("===============================dict===================================")
users = ["lee1","lee2","lee3","lee1","lee2","lee3","lee4"]
user_dict = {}
for user in users:
    if user_dict.get(user) != None:
        user_dict[user] += 1
    else:
        user_dict[user] = 1
print(user_dict)

## 统计list中相同元素的个数优化1
print("===============================dict===================================")
users = ["lee1","lee2","lee3","lee1","lee2","lee3","lee4"]
user_dict = {}
for user in users:
    user_dict.setdefault(user,0)
    user_dict[user] += 1
print(user_dict)

## 统计list中相同元素的个数优化2
print("===============================dict===================================")
from collections import defaultdict
users = ["lee1","lee2","lee3","lee1","lee2","lee3","lee4"]
user_dict = defaultdict(int)
for user in users:
    user_dict[user] += 1
print(user_dict)


## 统计list中相同元素的个数优化3(统计结果包含指定结构)
print("===============================dict===================================")
from collections import defaultdict
def gen_default():
    return {
        "name":"",
        "nums":0
    }
users = ["lee1","lee2","lee3","lee1","lee2","lee3","lee4"]
user_dict = defaultdict(gen_default)
for user in users:
    user_dict[user]["name"] = user
    user_dict[user]["nums"] += 1
print(user_dict)



# 五. namedtuple
from collections import namedtuple
print("===================================namedtuple==========================")
## 1.创建简单高效的类对象 namedtuple(类名,[属性1,属性2...])
User = namedtuple("User",["name","age","sex"])
user = User(name="lee",age=18,sex="男")
print(user.name,user.age,user.sex)
## 1.1 通过tuple初始化属性
t = ("yonge",24,"男")
user = User(*t)
print(user.name,user.age,user.sex)

## 1.2 通过dict初始化属性
d = {"name":"phper","age":26,"sex":"男"}
user = User(**d)
print(user.name,user.age,user.sex)

## 1.3 通过make初始化属性
user = User._make(t)
print(user.name,user.age,user.sex)
user = User._make(d.values())
print(user.name,user.age,user.sex)


## 1.4 nametuple转dict
d1 = user._asdict()
print(d1)

## 1.4 nametuple拆包
name,*other = user
print(name,other)


# 六.defaultdict
print("===================================defaultdict==========================")
from collections import defaultdict
defult_dict = defaultdict(list)  # int默认0
print(defult_dict["name"]) #[] 不会报错
# 可以使用自定义数据结构
def exec_default():
    return {
        "field1":"",
        "field2":""
    }
print(defaultdict(exec_default))
# 六.defaultdict

print("===================================format==========================")
# format
a=1
b=2
c=3
print("a:{0} b:{1} c:{2}".format(a,b,c))#a:1 b:2 c:3
print("a:{1} b:{0} c:{2}".format(a,b,c))#a:2 b:1 c:3


# 六.deque 双端队列
print("===================================deque==========================")
from collections import deque
queue_demo = deque([1,2,3,4,5])
## 1.从头部删除
queue_demo.popleft()
print(queue_demo)

## 2.从头部插入
queue_demo.appendleft(1)
print(queue_demo)

## 3.浅拷贝不可变类型，深拷贝可变类型
### 3.1当元素是字符串这样的不可变类型时（str，tuple，bytes）
queue_str = deque(["a","b","c"])
queue_str2 = queue_str.copy()
print(id(queue_str),id(queue_str2)) #内存地址不同
queue_str[1] = "bb"
print(queue_str,queue_str2) # 只有queue_str发生了变化

### 3.2当元素包含list,deque,bytearray,array等可变类型时
queue_str = deque(["a",["b1","b2","b3"],"c"])
queue_str2 = queue_str.copy()
print(id(queue_str[1]),id(queue_str2[1])) #地址相同
queue_str[1][0] = ["bbb"]
print(queue_str,queue_str2) #元素中的list都发生了变化
### 3.3 深拷贝
import copy
queue_str = deque(["a",["b1","b2","b3"],"c"])
queue_str2 = copy.deepcopy(queue_str)
print(id(queue_str[1]),id(queue_str2[1])) #地址不相同
queue_str[1][0] = ["bbb"]
print(queue_str,queue_str2) #只有queue_str发生了变化

## 4.extend
queue_str.extend(queue_str2)
print(queue_str)

## 4.deque是线程安全的，list不是线程安全的（GIL全局锁）

# 七.counter
print("===============================Counter===================================")
from collections import Counter
users = ["lee1","lee2","lee3","lee1","lee2","lee3","lee4"]
## 1.统计list
user_dict = Counter(users)
# print(user_dict)
## 2.统计字符串
str_counter = Counter("dsfsgsresdwesdsdwewrffawres")
# print(str_counter)

## 3.合并统计
str_counter.update("gerdas")
print(str_counter)

## 3.1合并操作可以传入任意可迭代对象
str_counter1 = str_counter.update("fwdsd")
str_counter.update(str_counter1)
print(str_counter)


## 4.统计出现最多的前n个元素
print(str_counter.most_common(3))

# 八.OrderedDict
from collections import OrderedDict
## 1.有序性（默认按照添加顺序,注意，python3中的dict也支持）
order_dict = OrderedDict()
order_dict["c"] = "lee3"
order_dict["a"] = "lee1"
order_dict["b"] = "lee2"

print(order_dict)

## pop和popitem
order_dict.pop("a") #删掉指定key的元素
print(order_dict)
order_dict.popitem() #删掉最后一个
print(order_dict)

# ChainMap
from collections import ChainMap
## 1.合并
dict1 = {"a":"lee1","b":"lee2"}
dict2 = {"c":"lee3","d":"lee4"}
# for k,v in dict1.items():
#     print(k,"=>",v)

new_dict = ChainMap(dict1,dict2)
for k,v in new_dict.items():
    print(k,"=>",v)

## 2.动态添加元素
new_dict = new_dict.new_child({"e":"lee5","f":"lee6"})
print(new_dict)
print(new_dict.maps) #引用类型，只是将内存地址copy到迭代器

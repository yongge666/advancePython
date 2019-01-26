# coding:utf8
# [start:end:step]
if __name__ == '__main__':
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
    # print(lis)





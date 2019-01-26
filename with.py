# coding:utf8
def except_try():
    try:
        print("start")
        #raise KeyError
        raise IndexError
        return 1
    except KeyError:
        print("key error 异常时执行")
        return 2
    else:
        print("other error")
        return 3
    finally:
        print("总会执行")
        return 4
# 上下文管理协议
class WithDemo:
    def __enter__(self):
        print("调用with开始时执行")
        # return self
        # 获取资源

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("调用with结束时执行")
        #用于释放资源

    def do_something(self):
        print("do something")

if __name__ == '__main__':

    try:
        print("start")
        raise KeyError
        # raise IndexError
    except KeyError:
        print("key error 异常时执行")
    else:
        print("other error")
    finally:
        print("总会执行")

    # return 压栈
    print(except_try()) #4

    print("====================with====================")

    with WithDemo() as wd:
        wd.do_something()




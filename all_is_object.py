# coding:utf8
# 装饰器实现原理
def ask(name="lee"):
    print(name)

def decorator_func():
    print("decorator_func")
    return ask

askFun = decorator_func()


if __name__ == "__main__":
    askFun("yongge")

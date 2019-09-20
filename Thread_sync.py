# coding:utf8
# 线程同步
# lock在同一个线程(函数)里面只能有一个acquire 和 release
# Rlock在同一个线程(函数)里面要有相同数目的acquire和release
from threading import Thread,Lock,RLock
total = 0
lock = RLock()
def add():
    global total
    global lock
    for i in range(100000):
        lock.acquire()
        total += 1
        lock.release()

def desc():
    global total
    global lock
    for i in range(100000):
        lock.acquire()
        total -= 1
        lock.release()

if __name__ == '__main__':
    t1 = Thread(target=add)
    t2 = Thread(target=desc)
    t1.start()
    t2.start()
    t1.join(True)
    t2.join(True)
    print(total)

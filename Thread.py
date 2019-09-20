# coding:utf8
import threading
import time
def get_html(url):
    print("获取",url,"详情start")
    time.sleep(2)
    print("获取",url,"详情end")

def get_url():
    print("获取url start")
    time.sleep(4)
    print("获取url end")

 #通过继承threading.Thread来实现多线程
class GetUrl(threading.Thread):
    def __init__(self,name):
        super().__init__(name = name)
        self.name = name
    def run(self):
        print(self.name,"获取url start")
        time.sleep(4)
        print("获取url end")


class GetHtml(threading.Thread):
    def __init__(self,name,url):
        super().__init__(name=name)
        self.url = url
    def run(self):
        print(self.name,"获取", self.url, "详情start")
        time.sleep(2)
        print("获取", self.url, "详情end")

if __name__ == '__main__':
    # thread1 = threading.Thread(target=get_html,args=("www.baidu.com",))
    # thread2 = threading.Thread(target=get_url)
    # start_time = time.time()
    # # thread1.setDaemon(True)  #主线程退出则退出，在start之前使用
    # # thread2.setDaemon
    # thread1.start()
    # thread2.start()
    #
    # thread1.join(True)  # 主线程等待此线程结束，在start之后使用
    # thread2.join(True)

    thread1 = GetHtml(name="t1",url="www.baidu.com")
    thread2 = GetUrl(name="t2")
    start_time = time.time()
    # thread1.setDaemon(True)  #主线程退出则退出，在start之前使用
    # thread2.setDaemon
    thread1.start()
    thread2.start()

    thread1.join(True)  # 主线程等待此线程结束，在start之后使用
    thread2.join(True)






    end_time = time.time()
    print(end_time-start_time)

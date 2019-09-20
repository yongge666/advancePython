# coding:utf8
# 线程间通信 （list操作是非线程安全的，所以推荐使用queue来做线程间通信）
from queue import Queue
import threading
import time
def get_url(queue):
    while True:
        print("get html start")
        time.sleep(3)
        for i in range(20):
            queue.put("http://www.baidu.com?id=",i)
def get_html(queue):
    while True:
        print("get html start")
        url = queue.get()
        print("get html started")
        time.sleep(2)
        print("get html end")


if __name__ == '__main__':
    url_quene = Queue(maxsize=10000)
    get_detail_url = threading.Thread(target=get_url,args=(url_quene,))
    get_detail_url.start()
    for i in range(10):
        html = threading.Thread(target=get_html,args=(url_quene,))
        html.start()

    url_quene.task_done()  # 结束队列
    url_quene.join() #阻塞主线程直到queue接收到taskdown
    print("主程序结束")






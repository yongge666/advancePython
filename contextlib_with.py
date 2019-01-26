# coding:utf8
import contextlib

@contextlib.contextmanager
def write_file(file):
    print(file," file open")
    print("文件操作中。。。") # 最先执行
    # raise IOError
    yield {}
    print("file close") #最后执行

if __name__ == '__main__':
    with write_file("/usr/local/data/test") as f:
        print("start...")
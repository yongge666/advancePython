# coding:utf8
class Company():
    def __init__(self,employee_list):
        self.employee = employee_list

    def __len__(self):
        return len(self.employee)

if __name__ == '__main__':
    com = Company(["a1","a2"])
    print(hasattr(com,"__len__"))
    #在某些情况下我们需要判定某个对象的类型
    # from collections.abc import Sized
    print(isinstance(com,Company))

    #需要强制某个子类必须实现某些方法 (推荐使用raise NotImplementedError)
    import abc
    class CacheBase(metaclass=abc.ABCMeta):
        @abc.abstractmethod
        def get(self,key):
            # raise NotImplementedError
            pass
        @abc.abstractmethod
        def set(self,key,value):
            # raise NotImplementedError
            pass
    class RedisCache(CacheBase):
        pass

    redis_cache = RedisCache()
    # redis_cache.set("key","val")




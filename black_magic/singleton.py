"""
python 单例模式

"""

instances = {}


def singleton(cls):
    def get_instance(*args, **kwargs):
        cls_name = cls.__name__
        if cls_name not in instances:
            instances[cls_name] = cls(*args, **kwargs)
        return instances[cls_name]

    return get_instance


@singleton
class User:
    def __init__(self, name):
        self.name = name


import threading


class Singleton(object):
    _instance_lock = threading.Lock()

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if not hasattr(Singleton, "_instance"):
            print("没有实例")
            with Singleton._instance_lock:  # 获取锁
                if not hasattr(Singleton, "_instance"):
                    Singleton._instance = object.__new__(cls)
        return Singleton._instance


# obj1 = Singleton()
# obj2 = Singleton()
# print(obj1, obj2)


def task(arg):
    obj = Singleton()
    print(obj)


for i in range(10):
    t = threading.Thread(target=task, args=[i, ])
    t.start()

if __name__ == '__main__':
    # u1 = User("lll")
    # u1.age = 2
    # print(u1.age)
    ...

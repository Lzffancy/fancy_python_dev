class Logger:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print(f"[Info]: function {self.func.__name__} is running...")

        return self.func(*args, **kwargs)


class Logger1:
    def __init__(self, level="INFO"):
        self.level = level # 装饰器的入参

    def __call__(self, func):
        def wrapper(*args, **kwargs):  # 函数也可入参
            print(f"[{self.level}]:function {func.__name__} is running")
            func(*args, **kwargs)

        return wrapper


@Logger
def foo():
    print("foo!!!!!!!!!!!!!!!")


@Logger1("DEBUG")
def bar():
    print("bar!!!!!!!!!!!!!!!")


if __name__ == '__main__':
    foo()
    bar()

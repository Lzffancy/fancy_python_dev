import be_call_xx

print("to call!!!", be_call_xx.STATIC_NUM)
print("to call!!! 2", be_call_xx.print_something())  # 这种函数执行,不会赋值给print

with open("./be_call_xx.py", "r") as f:
    print(exec(f.read()))


class Logger:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print(f"[Info]: function {self.func.__name__} is running...")

        return self.func(*args, **kwargs)

@Logger
def foo():
    print("foo!!!!!!!!!!!!!!!")


if __name__ == '__main__':
    foo()

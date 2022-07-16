def decorator_func(func):
    def wrapper():
        print("in wrapper")
        return func

    return wrapper


# @decorator_func
def say_hello():
    print("hello")


# =============================


# if __name__ == '__main__':
#     say_hello()

if __name__ == '__main__':
    wrapper = decorator_func(say_hello)
    say_hello = wrapper()()
    print(say_hello.__all__)
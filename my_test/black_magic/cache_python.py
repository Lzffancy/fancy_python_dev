from functools import lru_cache


@lru_cache(None)
def add(x, y):
    print("calculating: %s + %s" % (x, y))
    return x + y


print(add(1, 2))
print(add(1, 2))#直接调用结果
print(add(2, 3))
print(add(1, 2))

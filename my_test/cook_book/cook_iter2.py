from collections.abc import Iterable

"""
含有yield from 的递归生成器
"""
items = [1, 2, [3, 4, [5, 6], 7], 8]


def flatten(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable):
            yield from flatten(x)
        else:
            yield x


# d

CHUNKSIZE = 8192


def reader(s):
    while 1:
        data = s.recv(CHUNKSIZE)
        if data == b"":
            break
        print(data)


def reader2(s):
    for chunk in iter(lambda: s.recv(CHUNKSIZE), b''):
        pass


def opener_iter(dir):
    with open(dir) as f:
        for data in iter(lambda: f.readline(), ""):
            yield data


if __name__ == '__main__':
    print(list(flatten(items)))
    print(list(opener_iter("./test_str.txt")))

    with open("./test_str.txt", 'wt') as f:
        print('Hello World!', file=f) #输出并将其写入 file

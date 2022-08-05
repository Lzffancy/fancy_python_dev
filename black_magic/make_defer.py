import contextlib


def callback():
    # error=1/0
    print('B')


with contextlib.ExitStack() as stack:
    stack.callback(callback)
    print('A')

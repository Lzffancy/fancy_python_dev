"""
只会在Linux下生效
将程序中的标准输出记录为日志
"""

import contextlib
import sys

log_file = "./my_log"


def you_task():
    a = 1 / 0
    print("good")
    pass


@contextlib.contextmanager
def close_stdout():
    raw_stdout = sys.stdout
    f = open(log_file, "a+")  # 调用开始的时候执行
    sys.stdout = f

    yield

    sys.stdout = raw_stdout  # 调用结束后执行
    f.close()


with close_stdout():
    you_task()

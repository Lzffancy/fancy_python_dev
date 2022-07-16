import multiprocessing
import time
from multiprocessing import Process
import os


def info(title):
    print("-" * 50)
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())
    print("-" * 50)


def worker(name):
    info('function worker ......')
    time.sleep(2)
    print('hello', name)


def bad_worker(name):
    info('the bad worker ......')
    time.sleep(100)
    print('bad worker', name)


def multi_process_worker(num):
    process_list = []
    for i in range(0, num):
        if i == 5:
            p = Process(target=bad_worker, args=('fancy',), daemon=True)
            p.start()
        else:
            p = Process(target=worker, args=('fancy',), daemon=True)
            p.start()

        process_list.append(p)

    for i in process_list:
        # print(multiprocessing.active_children())
        i.join()


if __name__ == '__main__':
    info('main line')
    s_time = time.time()
    multi_process_worker(10)

    e_time = time.time()
    print("cost time", e_time - s_time)

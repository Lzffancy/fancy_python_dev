import multiprocessing
import time
from multiprocessing import Process
import os
import signal


# signal.signal(signal.SIGCHLD, signal.SIG_IGN)

def info(title):
    # print("-" * 50)
    print(title)
    # print('module name:', __name__)
    print('parent process:', os.getppid())
    # print('process id:', os.getpid())
    # print("-" * 50)


def worker(name):
    # info('function worker ......')
    print("worker:", os.getpid())
    time.sleep(5)
    # print('hello', name)

    return


def bad_worker(name):
    # info('the bad worker ......')
    print("bad_worker:", os.getpid())
    time.sleep(120)
    print('bad worker', name)

    return


def multi_process_worker(num):
    process_list = []
    for i in range(0, num):
        if i == 0:
            p = Process(target=bad_worker, args=('fancy',),daemon=True)
            p.start()
            process_list.append(p)
        else:
            p1 = Process(target=worker, args=('fancy',),daemon=True)
            p1.start()
            process_list.append(p1)


    print("block------")

    # for i in process_list:
    #     # print(multiprocessing.active_children())
    #     # 是否对进程进行阻塞
    #     i.join()


if __name__ == '__main__':
    # info('main line')
    print("main_parent:", os.getppid())
    print("main:", os.getpid())
    s_time = time.time()
    multi_process_worker(20)
    e_time = time.time()
    print("cost time", e_time - s_time)
    print("main sleep-------")
    # time.sleep(50)
    print("main end-------")
    exit(0)

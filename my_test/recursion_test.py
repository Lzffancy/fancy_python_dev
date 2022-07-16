# 测试递归和循环的内存差异
import dis
import threading

from memory_profiler import profile
# import resource, sys
import sys
# resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))
sys.setrecursionlimit(10**6)

sys.setrecursionlimit(100000000)
my_thread=threading.current_thread( )
threading.stack_size(100000000)

def power_by_loop(x, n):
    result = 1
    for i in range(n):
        result *= x
    return result


def power_by_recursion(x, n):
    if n == 0:
        return 1
    else:
        return x * power_by_recursion(x, n - 1)

@profile(precision=4)
def main():
    power_by_recursion(2, 2000)
    power_by_loop(2, 20000)


if __name__ == '__main__':
    # x = 2
    # n = 50
    # # print(power_by_loop(x, n), 'loop')
    #
    # print(power_by_recursion(x, n), "recursion")
    main()
    dis.dis(main)
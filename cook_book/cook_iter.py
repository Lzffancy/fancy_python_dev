def f_range(start, stop, increment):
    """
    该函数返回生成器
    """
    x = start
    while x < stop:
        yield x  #
        x += increment


for n in f_range(0, 4, 0.5):
    print(n)
print()
gen_obj = f_range(0, 4, 0.5)
print(next(gen_obj))
print(next(gen_obj))

range_obj = range(1, 7, 1)
print(range_obj)  # range返回的是可迭代对象


class Node:

    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)

    def depth_first(self):
        yield self
        for c in self:
            # 迭代中调用生成器 ,yield from 产生结果并且继续调用c.depth_first()
            yield from c.depth_first()  # g = c.depth_first()  res = g.send() yield res
            # g = c.depth_first()
            # res = g.send(None)
            # yield res

    def depth_first2(self):
        return DepthFirstIterator(self)


class DepthFirstIterator(object):
    """
    手写一个迭代器
    """

    def __init__(self, start_node):
        self._node = start_node
        self._children_iter = None
        self._child_iter = None

    def __iter__(self):
        return self

    def __next__(self):
        if self._children_iter is None:
            self._children_iter = iter(self._node)
            return self._node

        elif self._child_iter:
            try:
                nextchild = next(self._child_iter)
                return nextchild
            except StopIteration:
                self._child_iter = None
                return next(self)
        else:
            self._child_iter = next(self._children_iter).depth_first()
            return next(self)


import os
import fnmatch
import gzip
import bz2
import re


def gen_find(filepat, top):
    '''
    Find all filenames in a directory tree that match a shell wildcard pattern
    '''
    for path, dirlist, filelist in os.walk(top):
        for name in fnmatch.filter(filelist, filepat):
            yield os.path.join(path, name)


def gen_opener(filenames):
    '''
    实际的入参是一个生成器
    Open a sequence of filenames one at a time producing a file object.
    The file is closed immediately when proceeding to the next iteration.
    '''
    for filename in filenames:
        if filename.endswith('.gz'):
            f = gzip.open(filename, 'rt')
        elif filename.endswith('.bz2'):
            f = bz2.open(filename, 'rt')
        else:
            f = open(filename, 'rt')
        yield f
    f.close()


def gen_concatenate(iterators):
    '''
    入参是文段的迭代器
    Chain a sequence of iterators together into a single sequence.
    '''

    for it in iterators:
        # 取出每一段，返回出去，并且再次调用it
        yield from it


def gen_grep(pattern, lines):
    '''
    # 入参文段的迭代器，
    Look for a regex pattern in a sequence of lines
    '''

    pat = re.compile(pattern)
    for line in lines:
        if pat.search(line):
            # 满足条件则输出，
            yield line


# Example
if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)

    root.add_child(child1)
    root.add_child(child2)

    child1.add_child(Node(3))
    child1.add_child(Node(4))
    child2.add_child(Node(5))

    for ch in root.depth_first():
        print(ch)

    for ch in root.depth_first2():
        print(ch)
    # lognames = gen_find('access-log*', 'www')
    # files = gen_opener(lognames)
    # lines = gen_concatenate(files)
    # pylines = gen_grep('(?i)python', lines)
    # for line in pylines:
    #     # 全局都是生成器在调用
    #     print(line)

    lis01 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


    def iter_list(lis01):
        for i in lis01:
            yield from i
        return "end"


    iter_obj = iter_list(lis01)
    print(iter_obj)
    # print(next(iter_obj)) #将其变为惰性
    # print(next(iter_obj))  # 将其变为惰性
    # print(next(iter_obj))  # 将其变为惰性
    # print(next(iter_obj))  # 将其变为惰性

    for i in iter_obj:
        print(i)
    # print(list(iter_obj))

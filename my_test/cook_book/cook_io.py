import array

a = array.array("i", [0, 0, 0, 0, 0, 0, 0, 0])

with open("data.bin", "rb") as f:
    f.readinto(a)

import os
import mmap


def memory_map(filename, access=mmap.ACCESS_WRITE):
    size = os.path.getsize(filename)
    fd = os.open(filename, os.O_RDWR)
    return mmap.mmap(fd, size, access=access)


size = 100000000

with open('data', 'wb') as f:
    f.seek(size - 1)
    f.write(b'\x00')  # 文末的占位符号，使得整个文件占用指定的size
m = memory_map("data")
print(m)
print(m[0:10])
m[0:11] = b"hello world"
m.close()

with open("data", "rb") as f:
    print(f.read(11))

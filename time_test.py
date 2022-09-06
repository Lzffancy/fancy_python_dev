# coding:UTF-8
import os
import time
from pathlib import Path

dt = "2016-05-05 00:00:01"
# 字符串-》时间元组
timeArray = time.strptime(dt, "%Y-%m-%d %H:%M:%S")
# 时间元组-》时间戳
timestamp = time.mktime(timeArray)
print(timestamp)
#  字符串--》时间元组
a = "2011-09-28 00:00:00"
print(time.strptime(a, '%Y-%m-%d %H:%M:%S'))
#  字符串--》-时间元组--》时间戳
a = "2011-09-28 10:00:00"
time.mktime(time.strptime(a, "%Y-%m-%d %H:%M:%S"))
#  时间戳--》时间元组--》字符串
print("时间戳--》字符串")
x = time.localtime(1644854100.0)
print(x)
print(time.strftime('%H:%M', x))

# 当前时间
print("当前时间")
print(time.time(), "时间戳")
print(time.strftime("%m-%d"), "时间字符串")

a = time.localtime()
print(a, "时间元组")
print("周几")
print(time.strftime("%A", a))
print(time.strftime("%w", a))

if __name__ == '__main__':
    sdt = "2022-08-08 00:14:00"
    edt = "2022-08-08 00:14:05"

    print(sdt[-5:], "倒序")
    print(time.mktime(time.strptime(sdt, "%Y-%m-%d %H:%M:%S")) * 1000)
    print(time.mktime(time.strptime(edt, "%Y-%m-%d %H:%M:%S")) * 1000)
    BASE_DIR = Path(__file__).resolve().parent.parent  # 拼接路径
    print(os.path.join(BASE_DIR, 'logs'))
    date = "2022-02-15"
    index_name = "smart_log-" + date.replace("-", ".")
    print(index_name)

    print(time.strftime("%Y-%m-%d %H:%M:%S"))
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))


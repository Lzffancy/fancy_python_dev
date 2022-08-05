import time

print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(1652154596)))
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(1653557034)))


print(time.time())
print(time.strftime("%d"))

tuple1 = (b"1",b"2")

now_time_str = time.strftime("%Y-%m-%d")
day = now_time_str[8:10]
now_time_stamp = int(time.mktime(time.strptime(now_time_str, "%Y-%m-%d")))  # 去除时分秒
last_time_stamp = now_time_stamp - 24 * 60 * 60
# print(dict(tuple1))
now_time_key, last_time_key = [], []
for t in range(last_time_stamp, now_time_stamp + 24 * 60 * 60, 5 * 60):
    time_str = time.strftime("%Y-%m-%d %H:%M", time.localtime(t))
    if time_str[8:10] == day:
        now_time_key.append(time_str)
    else:
        last_time_key.append(time_str)



print(now_time_key,last_time_key)
time_str = time.strftime("%d %H:%M", time.localtime())
print(time_str)
print(time_str[0:2])

import this

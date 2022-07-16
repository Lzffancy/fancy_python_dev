# import datetime
import time
import hashlib
t = ((1, 2), (3, 4),)
t1 = (1, 2, 3, 4)
t2 = ("1", "2", "3", "4")
# print(t.join())
print("".join(t2))  # 字符格式方法
print(t2)
l = [1, 2, 3, 4]
print("good".join(t2))  #expected str instance


# t3 = (('fancy', 'your', datetime.datetime(2021, 1, 21, 17, 11, 33)),)
t3=""
for name, word, time in t3:
    print(name)
    print(word)
    print(time)



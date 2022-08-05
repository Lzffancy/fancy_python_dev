import time

now_time_tuple = time.localtime()
print(now_time_tuple)
week_day = time.strftime("%w", now_time_tuple)
now_time_stamp=time.mktime(time.strptime(time.strftime("%Y-%m-%d",now_time_tuple),"%Y-%m-%d"))
print(week_day)
now_time_stamp=(7 - int(week_day)) * 24 * 60 * 60 + now_time_stamp
print(now_time_stamp)
mid_time_stamp=now_time_stamp-7*24*60*60
print(mid_time_stamp)
last_time_stamp = now_time_stamp-2*7*24*60*60
print(last_time_stamp)
data_dic={}
data_dic["last_time"] = []
data_dic["last_data"] = []
data_dic["now_time"] = []
data_dic["now_data"] = []
for t in range(int(last_time_stamp),int(now_time_stamp),60*60):
    time_str = time.strftime("%Y-%m-%d %H:%M", time.localtime(t))
    print(time_str)
    if t >=mid_time_stamp:
        data_dic["now_time"].append(time_str[-5:])
    else:
        data_dic["last_time"].append(time_str[-5:])


print(data_dic)
t="2022-02-13 00:00"
print(t[5:])


dt = "2022-02-21 00:01:00"
print(dt[0:10],"==============================")

# 转换成时间数组
timeArray = time.strptime(dt, "%Y-%m-%d %H:%M:%S")
# 转换成时间戳
timestamp = time.mktime(timeArray)

# print(timestamp)

def make_5mins_interval():
    now_time_stamp = timestamp
    # 间隔五分钟向下取整
    interval = 5 * 60
    result = now_time_stamp % interval
    now_time_stamp -= result
    last_time_stamp = now_time_stamp - interval
    print(last_time_stamp)
    print(now_time_stamp)
    print(time.strftime("%Y-%m-%d %H:%M", time.localtime(last_time_stamp)))
    print(time.strftime("%Y-%m-%d %H:%M", time.localtime(now_time_stamp)))
    return last_time_stamp, now_time_stamp

make_5mins_interval()
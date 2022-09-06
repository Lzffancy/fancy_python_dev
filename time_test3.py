import time

dt = "2022-08-09 17:55:00"

# 转换成时间数组
timeArray = time.strptime(dt, "%Y-%m-%d %H:%M:%S")
# 转换成时间戳
timestamp = time.mktime(timeArray)
print("从当前到过去  即从现在到前 x分钟")

def make_mins_interval(mins):
    now_time_stamp = timestamp
    # 间隔五分钟向下取整
    interval = mins * 60
    result = now_time_stamp % interval
    now_time_stamp -= result
    last_time_stamp = now_time_stamp - interval
    print(last_time_stamp)
    print(timestamp)
    print(time.strftime("%Y-%m-%d %H:%M", time.localtime(now_time_stamp)))
    print(time.strftime("%Y-%m-%d %H:%M", time.localtime(last_time_stamp)))
    return last_time_stamp, now_time_stamp


# start_time, end_time = make_mins_interval(5)
start_time, end_time = make_mins_interval(5)
print(start_time * 1000, end_time * 1000)
# end_time=time.strftime("%Y-%m-%d %H:%M", time.localtime(end_time))
# print(end_time[-5:])
# print(end_time[0:10])
# if end_time[-5:] == "00:00":
#     pass
# es_resp = es_common.es_search(body,other_index = start_time_str[0:9])
print("2022-08-11"[8:])

2

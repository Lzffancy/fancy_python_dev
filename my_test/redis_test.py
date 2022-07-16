import redis   # 导入redis 模块

r = redis.Redis(host='11.177.106.2', port=5001, decode_responses=True,password="KF20150309redisPW")
print(r)
r.set("lizhuofan_test","good_redis",ex=10)
print(r.get("lizhuofan_test"))
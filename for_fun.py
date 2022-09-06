import json

res = 0
a = 0
n = 0

while 1:
    n += 1
    a = (-1) ** (n + 1) * 4 / (2 * n - 1)
    res += a
    if abs(a) < 1e-5:
        print(res)
        break

print(1e-5, type(1e-5))

a_lis = ["1", "2", "3"]

b_lis = a_lis.copy()


target  = "1"
print(isinstance(target,str))
if target != "" and isinstance(target,str) and target in a_lis:
    b_lis=[target]
print(b_lis)

ret = '1661931369:{"name":"lzf|123"}|abcd|0'

ret = ret[11:]
print("ret",ret)


cont_table = ret.split("|")

print("cont_table",cont_table)
# data=cont_table[0]
# json_data = json.loads(data)
# print(json_data)



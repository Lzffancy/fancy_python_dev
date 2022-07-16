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

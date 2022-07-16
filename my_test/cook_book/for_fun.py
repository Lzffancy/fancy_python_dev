import heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums))  # Prints [42, 37, 23]
print(heapq.nsmallest(3, nums))  # Prints [-4, 1, 2] 优先队列算法

from collections import defaultdict

d = defaultdict(list)  # 字典Key的默认值为[]
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)
d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['b'].add(4)

# 字典排序
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,

    'FB1': 10.75,
    'FB': 10.75,

}
# zip返回迭代器
sorted_prize = sorted(zip(prices.values(), prices.keys()))
print(sorted_prize)
sorted_prize2 = sorted(prices.items(), key=lambda a: a[1])

print(sorted_prize2)

min_key = min(prices, key=lambda k: prices[k])  # Returns 'FB'
print(min_key)
max_name = max(zip(prices.values(), prices.keys()))  # 以第zip一个位置的值排序
# max_name = max(zip(prices.keys(),prices.values()))
print(max_name)

#

a = {
    'x': 1,
    'y': 2,
    'z': 3
}
b = {
    'w': 10,
    'x': 11,
    'y': 2
}

c = {key: a[key] for key in a.keys() - {'z', 'w'}}
print(c)

a = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]


def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            print(seen)
            seen.add(val)


print(list(dedupe(a, key=lambda d: (d['x'], d['y']))))

rows = [
    {'address': '5412 N CLARK', 'date': '07/01/2012'},
    {'address': '5148 N CLARK', 'date': '07/04/2012'},
    # {'address': '5800 E 58TH', 'date': '07/02/2012'},
    {'address': '2122 N CLARK', 'date': '07/03/2012'},
    # {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
    # {'address': '1060 W ADDISON', 'date': '07/02/2012'},
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
    {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]

from operator import itemgetter
from itertools import groupby

# Sort by the desired field first
rows.sort(key=itemgetter('date'))
# Iterate in groups
for date, items in groupby(rows, key=itemgetter('date')):
    print(date, items)
    for i in items:
        print(' ', i)

from collections import defaultdict

rows_by_date = defaultdict(list)
# dict like {"value":[]}

for row in rows:
    rows_by_date[row['date']].append(row)
print(rows_by_date)

mylist = [1, 4, -5, 10, -7, 2, 3, -1]
l = [n for n in mylist if n > 0]
g = (n for n in mylist if n > 0)  # 这是生成器

print(l, list(g))

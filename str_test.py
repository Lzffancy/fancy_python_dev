# str01 = "abc"
# str01[1] = "c"
# print(str01[1])


class Cat:
    class_level = '贵族'
    __slots__ = "name"

    def run(self):
        print('%s岁的%s%s正在以%s的速度奔跑' % (self.age, self.type, self.name, self.speed))

    def __getattr__(self, item):
        print('你找的属性不存在')

    def __setattr__(self, key, value):
        print('你在设置属性', key)

    def __delattr__(self, item):
        print('你在删除属性')


cat = Cat()
cat.name = "1"
# cat.x = "2"

Cat.y = "3"
cat2 = Cat()
print(cat2.y)

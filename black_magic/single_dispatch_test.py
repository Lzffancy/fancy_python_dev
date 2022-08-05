from functools import singledispatch


@singledispatch
def age(obj):
    print('请输入合法参数')


@age.register(int)
def _(age):
    print('我已经{}了'.format(age))


@age.register(str)
def _(age):
    print('I am {} years old.'.format(age))


age(23)  # int
age('twenty three')  # str
age(['23'])  # list

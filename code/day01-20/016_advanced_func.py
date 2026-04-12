# 高阶函数
# 由于Python的动态性，我们可以定义一些高阶函数，这些函数可以接受其他函数作为参数，也可以返回函数作为结果。

mydict = {
    'a': 1,
    'b': 2,
    'c': 3,}

print(list(mydict.values()))

#  定义一个函数，用于计算多个参数的和
def calc(*args, **kwargs):
    items = list(args) + list(kwargs.values())
    result = 0
    for item in items:
        if type(item) in (int, float):
            result += item
    return result

print(calc(1, 2, 3, a=4, b=5, c=6))

# 把上面的函数改成一个高阶函数，接受一个操作函数作为参数，这样我们就可以用它来计算多个参数的积、差等。
def calc(init_value, op_func, *args, **kwargs):
    items = list(args) + list(kwargs.values())
    result = init_value
    for item in items:
        if type(item) in (int, float):
            result = op_func(result, item)
    return result

def add1(x, y):
    return x + y

def mul1(x, y):
    return x * y

print(calc(0, add1, 2, 3, a=4, b=5, c=6))
print(calc(1, mul1, 2, 3, a=4, b=5, c=6))

# 我们也可以使用python中定义好的函数

from operator import add, mul
print(calc(0, add, 2, 3, a=4, b=5, c=6))
print(calc(1, mul, 2, 3, a=4, b=5, c=6))


def is_even(num):
    """判断num是不是偶数"""
    return num % 2 == 0


def square(num):
    """求平方"""
    return num ** 2


old_nums = [35, 12, 8, 99, 60, 52]
# filter函数
# filter函数可以用来过滤掉不满足条件的元素，返回一个迭代器
# map函数
# map函数可以用来对每个元素进行操作，返回一个迭代器
new_nums = list(map(square, filter(is_even, old_nums)))
print(new_nums)  # [144, 64, 3600, 2704]


# 排序
# sorted函数可以用来对一个可迭代对象进行排序，返回一个新的列表
old_strings = ['in', 'apple', 'zoo', 'waxberry', 'pear']
new_strings = sorted(old_strings)
print(new_strings)  # ['apple', 'in', 'pear', waxberry', 'zoo']

# key可以设置排序的规则，比如按照字符串的长度进行排序
old_strings = ['in', 'apple', 'zoo', 'waxberry', 'pear']
new_strings = sorted(old_strings, key=len)
print(new_strings)  # ['in', 'zoo', 'pear', 'apple', 'waxberry']

# 匿名函数
# 匿名函数是一种没有名字的函数，通常用来作为参数传递给，
# 需要lambda关键字来定义匿名函数，且只能有一个表达式，不能有多条语句。
# 用一行代码实现计算阶乘的函数
import functools
import operator
# 用一行代码实现判断素数的函数
is_prime = lambda x: all(map(lambda f: x % f, range(2, int(x ** 0.5) + 1)))
print(is_prime(7))  # True

# 偏函数
# 偏函数是一种特殊的函数，它可以在调用时固定住一些参数，返回一个新的函数。
# 使用functools模块的partial函数来创建偏函数
# 例如 int函数
int2 = functools.partial(int, base=2)
int16 = functools.partial(int, base=16)
print(int2('1010'))  # 10
print(int16('1A'))  # 26

def add(x, y):
    return x + y

# add5 = functools.partial(add, y=5)
# print(add5(10))  # 15

# 也可以自己实现一个偏函数，接收所有的参数，然后再调用这个参数，
def my_partial(func, *args, **kwargs):
    def wrapper(*fargs, **fkwargs):
        new_args = args + fargs
        new_kwargs = {**kwargs, **fkwargs}
        return func(*new_args, **new_kwargs)
    return wrapper
add5 = my_partial(add, y=5)
print(add5(10))  # 15
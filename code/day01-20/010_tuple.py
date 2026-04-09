# ()表示空元组，
# 但是如果元组中只有一个元素，需要加上一个逗号，
# 否则()就不是代表元组的字面量语法，而是改变运算优先级的圆括号，
# 所以('hello', )和(100, )才是一元组，而('hello')和(100)只是字符串和整数

a = ()
print(type(a))  # <class 'tuple'>
b = ('hello')
print(type(b))  # <class 'str'>
c = (100)
print(type(c))  # <class 'int'>
d = ('hello', )
print(type(d))  # <class 'tuple'>
e = (100, )
print(type(e))  # <class 'tuple'>


# 元组和列表的不同之处在于，元组是不可变类型，
# 这就意味着元组类型的变量一旦定义，其中的元素不能再添加或删除，而且元素的值也不能修改


# 打包和解包操作
# 打包操作
a = 1, 10, 100
print(type(a))  # <class 'tuple'>
print(a)        # (1, 10, 100)
# 解包操作
i, j, k = a
print(i, j, k)  # 1 10 100


# 通过星号表达式，我们可以让一个变量接收多个值，代码如下所示。需要注意两点：
# 首先，用星号表达式修饰的变量会变成一个列表，列表中有0个或多个元素；其次，在解包语法中，星号表达式只能出现一次。
a = 1, 10, 100, 1000
i, j, *k = a
print(i, j, k)        # 1 10 [100, 1000]

# 解包语法对所有的序列都成立
a, b, *c = range(1, 10)
print(a, b, c)
a, b, c = [1, 10, 100]
print(a, b, c)
a, *b, c = 'hello'
print(a, b, c)

# 三个变量a、b、c的值互换
a, b, c = b, c, a

# 列表和元组互转
infos = ('骆昊', 45, True, '四川成都')
# 将元组转换成列表
print(list(infos))  # ['骆昊', 45, True, '四川成都']

frts = ['apple', 'banana', 'orange']
# 将列表转换成元组
print(tuple(frts))  # ('apple', 'banana', 'orange')

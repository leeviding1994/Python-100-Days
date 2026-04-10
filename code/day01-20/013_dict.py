# 声明
d = {}
person = dict(name='王大锤', age=55, height=168, weight=60, addr='成都市武侯区科华北路62号1栋101')

# 可以通过Python内置函数zip压缩两个序列并创建字典
# 一一对应
items1 = dict(zip('ABCDE', '12345'))
print(items1)  # {'A': '1', 'B': '2', 'C': '3', 'D': '4', 'E': '5'}
items2 = dict(zip('ABCDE', range(1, 10)))
print(items2)  # {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5}

# for只能遍历字典的键，不能遍历字典的值
for key in person:
    print(key)

# 赋值
person['name'] = '李大锤2'

# 取值
print(person['name'])  # 李大锤2
print(person.get('name'))  # 李大锤2
# 跟索引运算不同的是，get方法在字典中没有指定的键时不会产生异常，而是返回None或指定的默认值
print(person.get('sex'))  # None
print(person.get('sex', True))  # 未知

# update
# 当执行x.update(y)操作时，x跟y相同的键对应的值会被y中的值更新，而y中有但x中没有的键值对会直接添加到x中
person1 = {'name': '王大锤', 'age': 55, 'height': 178}
person2 = {'age': 25, 'addr': '成都市武侯区科华北路62号1栋101'}
person1.update(person2)
print(person1)  # {'name': '王大锤', 'age': 25, 'height': 178, 'addr': '成都市武侯区科华北路62号1栋101'


# 删除元素,没有键时会报错
del person1['height']
if 'weight' in person1:
    person1.pop('weight')
print(person1)  # {'name': '王大锤', 'age': 25, 'addr': '成都市武侯区科华北路62号1栋101'}
# 3.7+ 按照后进先出（LIFO）的顺序删除键值对，即删除最后插入的键值对
# 3.6 会随机删除一个键值对，而不是最后插入的键值对
print(person1.popitem())
print(person1)
person1.clear()
print(person1)

# 过滤字典
# 只保留股票价格大于100的股票
stocks = {
    'AAPL': 191.88,
    'GOOG': 1186.96,
    'IBM': 149.24,
    'ORCL': 48.44,
    'ACN': 166.89,
    'FB': 208.09,
    'SYMC': 21.29
}
stocks2 = {key: value for key, value in stocks.items() if value > 100}
print(stocks2)


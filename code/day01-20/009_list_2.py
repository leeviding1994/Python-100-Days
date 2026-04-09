# 添加和插入
languages = ['Python', 'Java', 'C++']
languages.append('JavaScript')
print(languages)
languages.insert(1, 'SQL')
print(languages)


# 删除元素
# 删除的元素并不在列表中，会引发ValueError错误导致程序崩溃
# remove()方法会删除列表中第一个匹配的元素，如果有多个相同的元素，只会删除第一个
# pop()方法会删除列表中最后一个元素，默认删除最后一个元素
# clear()方法会清空列表，删除所有元素，返回空列表
if 'C++' in languages:
    languages.remove('C++')
print(languages)

temp = languages.pop()
temp = languages.pop(1)
print(temp)
print(languages)
languages.clear()


languages2 = ['Python', 'Java', 'C++', 'Python']
languages2.remove('Python')
print(languages2)


# del 语句可以删除列表中的元素
del languages2[1]
print(languages2)

# 查找元素
# index()方法会返回元素的第一个匹配的索引位置
# index('', index)方法会从索引位置index开始查找元素，如果找到则返回索引位置，否则引发ValueError错误
items = ['Python', 'Java', 'Java', 'C++', 'Kotlin', 'Python']
print(items.index('Python'))     # 0
# 从索引位置1开始查找'Python'
print(items.index('Python', 1))  # 5
print(items.count('Python'))     # 2
print(items.count('Kotlin'))     # 1
print(items.count('Swfit'))      # 0
# 从索引位置3开始查找'Java'
# print(items.index('Java', 3))    # ValueError: 'Java' is not in list


# 排序和反序
items = ['Python', 'Java', 'C++', 'Kotlin', 'Swift']
items.sort()
print(items)  # ['C++', 'Java', 'Kotlin', 'Python', 'Swift']
items.reverse()
print(items)  # ['Swift', 'Python', 'Kotlin', 'Java', 'C++']

# 列表生成式
# 使用列表生成式创建列表不仅代码简单优雅，而且性能上也优于使用for-in循环和append方法向空列表中追加元素的方式
squares = [x**2 for x in range(10)]
print(squares) 


nums1 = [35, 12, 97, 64, 55]
nums2 = [num ** 2 for num in nums1]
print(nums2)

# 嵌套列表
nums = [0,1,2,3,4]
matrix1 = [nums for _ in nums]
print(matrix1)
matrix2 = [[num ** 2 for num in nums] for _ in nums]
print(matrix2)


# 彩票
# \033[0m是一个控制码，表示关闭所有属性
# 0可以省略，1表示高亮，5表示闪烁，7表示反显等
# 30代表黑色，31代表红色，32代表绿色，33代表黄色，34代表蓝色
import random

n = int(input('生成几注号码: '))
red_balls = [i for i in range(1, 34)]
blue_balls = [i for i in range(1, 17)]
for _ in range(n):
    # 从红色球列表中随机抽出6个红色球（无放回抽样）
    selected_balls = random.sample(red_balls, 6)
    # 对选中的红色球排序
    selected_balls.sort()
    # 输出选中的红色球
    for ball in selected_balls:
        # \033[031m 是设置红色文本
        # {ball:0>2d} 是格式化球号，确保两位数字，不足前面补0
        # \033[0m 是重置所有文本属性，给后面的空格和蓝色球设置默认颜色
        print(f'\033[5;31m{ball:0>2d}\033[0m', end=' ')
    # 从蓝色球列表中随机抽出1个蓝色球
    blue_ball = random.choice(blue_balls)
    # 输出选中的蓝色球
    print(f'\033[0;34m{blue_ball:0>2d}\033[0m')
    
# rich 库提供了丰富的文本样式和颜色，可以用来美化彩票号码的输出
from rich.console import Console
console = Console()
console.print(f'[red]{[ball for ball in red_balls]}[/red]', end=' ')
console.print(f'[blue]{blue_balls}[/blue]')

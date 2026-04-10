# 多行字符串
s3 = '''hello,
wonderful
world!'''
print(s3)

# 原始字符串
s1 = '\it \is \time \to \read \now'
s2 = r'\it \is \time \to \read \now'
print(s1)
print(s2)


# 字符串的特殊表示
# \可以加 八进制、十六进制 为字符的码点（不仅限于 ASCII 码，只要码点在有效范围内）
# u开头的Unicode 码  为 Unicode 编码
s1 = '\141\142\143\x61\x62\x63\xff\x25'
s2 = '\u9a86\u660a'
print(s1)
print(s2)

# 字符串的方法类似于列表
s1 = 'a whole new world'
s2 = 'a whole old world'
print(f's1 == s2:{s1 == s2}')             # False
print(f's1 < s2:{s1 < s2}')              # True
s3 = '骆昊'
print(ord('骆'))            # 39558
print(ord('昊'))            # 26122
s4 = '王大锤'
print(ord('王'))            # 29579
print(ord('大'))            # 22823
print(ord('锤'))            # 38180
print(s3 >= s4)             # True
print(s3 != s4)             # True

# 成员运算符
print('a' in s1)             # True
print('hello' in s1)         # False
print('Hello' not in s1)     # True

# 获取长度
print(len(s1))              # 13

# 获取切片
# 如果索引越界，会引发IndexError异常，错误提示信息为：string index out of range
print(s1[0::2])             # awoenwwrd

# 字符遍历
s = 'hello'
for i in range(len(s)):
    print(s[i])

for sc in s:
    print(sc)

# 字符串的方法
# 1. 字符串的拼接
s1 = 'hello, world!'
# 字符串首字母大写
print(s1.capitalize())  # Hello, world!
# 字符串每个单词首字母大写
print(s1.title())       # Hello, World!
# 字符串变大写
print(s1.upper())       # HELLO, WORLD!
s2 = 'GOODBYE'
# 字符串变小写
print(s2.lower())       # goodbye
# 检查s1和s2的值
print(s1)               # hello, world
print(s2)               # GOODBYE


# isdigit用来判断字符串是不是完全由数字构成的，
# isalpha用来判断字符串是不是完全由字母构成的，这里的字母指的是 Unicode 字符但不包含 Emoji 字符，
# isalnum用来判断字符串是不是由字母和数字构成的。
s2 = 'abc123456'
print(s2.isdigit())  # False
print(s2.isalpha())  # False
print(s2.isalnum())  # True


# 查找
# find() 找不到返回-1
# rfind() 从后往前找，结果和find()一样，只是从后往前找
# index() 找不到会引发ValueError异常
s = 'hello, world!'
print(s.find('or'))      # 8
print(s.find('or', 9))   # -1
print(s.index('or'))      # 8
# print(s.index('or', 9))  # ValueError: substring not found

# center() 居中对齐
# rjust() 右对齐
# ljust() 左对齐
# zfill() 填充0
s = 'hello, world'
print(s.center(20, '*'))  # ****hello, world****
print(s.rjust(20))        #         hello, world
print(s.ljust(20, '~'))   # hello, world~~~~~~~~
print('33'.zfill(5))      # 00033
print('-33'.zfill(5))     # -0033

# replace() 替换, 可以指定替换次数, 默认替换所有
print(s.replace('o', '@'))     # hell@, g@@d w@rld
print(s.replace('o', '@', 1))  # hell@, good world
print(s)

# 格式化输出
a = 321
b = 123
print('%d * %d = %d' % (a, b, a * b))
print('{0:05d} * {1:03d} = {2}'.format(a, b, a * b))
print(f'{a:05d} * {b:03d} = {a * b}')

# strip() 去掉字符串首尾的空格
s = ' hello, world '
print(s.strip())  # hello, world
s = '~hello, world~'
print(s.strip('~'))  # hello, world
print(s.lstrip('~'))  # hello, world~
print(s.rstrip('~'))  # ~hello, world

# 拆分和合并
s = 'hello, world, good, world'
sList = s.split(',')  # ['hello', ' world', ' good', ' world']
print(sList)
# 可以指定拆分次数, 默认拆分所有
print(s.split(',', 2))  # ['hello', ' world', ' good, world']
print('~'.join(sList))  # hello, world, good, world

# 编码和解码
s = '丁立'
b = s.encode('utf-8')
print(b)  # b'\xe4\xbd\x93\xe4\xba\x8c'
print(b.decode('utf-8'))  # 丁立
print(hex(ord('丁')))
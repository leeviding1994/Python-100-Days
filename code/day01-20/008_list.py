# 列表中可以有不同类型的元素，但是我们通常并不建议将不同类型的元素放在同一个列表中，主要是操作起来极为不便。
items1 = [100, 12.3, 'Python', True]
print(items1)

#
items4 = list(range(1, 10))
items5 = list('hello')
items6 = list(['hello', 'world'])
print(items4)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(items5)  # ['h', 'e', 'l', 'l', 'o']
print(items6)  # ['hello', 'world']

# 我们可以使用*运算符实现列表的重复运算，*运算符会将列表元素重复指定的次数
print(items6 * 3)

# 使用in或not in运算符判断一个元素在不在列表中
print('hello' in items6)  # True


# [0]可以访问列表中的第一个元素
# [-1]可以访问列表中的最后一个元素p
# 如果为负数， 则会从 length + index 位置开始访问
print(items6[0])  # 'hello'
print(items6[-1])  # 'world'
print(items6[-2])  # 'hello'

# [start:end:stride]
# start 开始，包含，默认为0
# end 结束，不包含，默认为列表长度
# stride 步长，默认为1， 负数时表示反向访问
items8 = ['apple', 'waxberry', 'pitaya', 'peach', 'watermelon']
print(items8[1:3:1])
print(items8[0:4:2])
print(items8[-4:-2:1])
print(items8[-2:-6:-1])
# 可以省略
print(items8[1:3])     # ['strawberry', 'durian']
print(items8[:3:1])    # ['apple', 'strawberry', 'durian']
print(items8[::2])     # ['apple', 'durian', 'watermelon']
print(items8[-4:-2])   # ['strawberry', 'durian']
print(items8[-2::-1])

# 可以设置
items8[1:3] = ['x', 'o']

# 比较运算
# 列表的比较操作（如 <、>、<=、>=、==、!=）是按元素顺序逐个比较的
# 依次比较，如果相等则继续比较下一个元素，直到找到不相等的元素或者比较完所有元素为止
nums0 = [0,1]
nums1 = [1, 2, 3, 4]
nums2 = list(range(1, 5))
print(nums2)
nums3 = [3, 0, 1]
print(nums1 == nums2)  # True
print(nums1 != nums2)  # False
print(nums1 <= nums3)  # True
print(nums2 >= nums3)  # False
print(f'nums0{nums0} < nums1{nums1}: {nums0 < nums1}')   # True
print(f'nums0{nums0} < nums3{nums3}: {nums0 < nums3}')   # True

# 判断元素是否在列表中
print(1 in nums0)  # True

# 遍历列表  
for num in nums0:   
    print(num)
for i in range(len(nums0)):
    print(nums0[i])

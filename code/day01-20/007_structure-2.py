import time

#  range(3600)可以构造出一个从0到3599的范围
for i in range(2):
    print('hello, world')
    print(f'{i = }')
    time.sleep(1)

a = f'{i = }'
print(f'{a =}')

#  没有用到的循环变量，通常把循环变量命名为_
for _ in range(5):
    print('hello, world')
    
'''
range(101)：可以用来产生0到100范围的整数，需要注意的是取不到101。
range(1, 101)：可以用来产生1到100范围的整数，相当于是左闭右开的设定，即[1, 101)。
range(1, 101, 2)：可以用来产生1到100的奇数，其中2是步长（跨度），即每次递增的值，101取不到。
range(100, 0, -2)：可以用来产生100到1的偶数，其中-2是步长（跨度），即每次递减的值，0取不到。
'''

total = 0
for a in range(0, 101, 2):
    total += a
print(total)

print('sum = %06x' % sum(range(0, 101, 2)))
print(f'sum = {sum(range(0, 101, 2)):06d}')
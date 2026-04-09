'''
sep: str | None = " ",
end: str | None = "\n",
file: SupportsWrite[str] | None = None,
flush: Literal[False] = False,
'''

for i in range(1, 10):
    for j in range(1, i + 1):
        print(f'{i}×{j}={i * j}', end='\t')
    print()
    
num = int(input('需要判断素数：'))

is_prime = True
for a in range(2, int(num ** 0.5) + 1):
    if num % a == 0:
        is_prime = False
        print(f'{num}被{a}整除')
        break
    else:
        continue
print(f'{num}是素数吗？{is_prime}')


# x = y%x   y = x
x = int(input('x = '))
y = int(input('y = '))
while y % x != 0:
    x, y = y % x, x
print(f'最大公约数: {x}')


import random

answer = random.randrange(1, 101)
print(answer)
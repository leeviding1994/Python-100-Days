import random
import string

ALL_CHARS = string.digits + string.ascii_letters

# 练习：生成一个指定长度的验证码
# sample和choices函数都可以实现随机抽样，
# sample实现无放回抽样，这意味着抽样取出的元素是不重复的；
# choices实现有放回抽样，这意味着可能会重复选中某些元素
def generate_code(code_len=4):
    # return ''.join(random.choice(ALL_CHARS) for _ in range(code_len))
    return  ''.join(random.choices(ALL_CHARS, k=code_len))
    # return ''.join(random.sample(ALL_CHARS, k=code_len))

for _ in range(5):
    print(generate_code(6))

    
# 练习：判断一个数是否是素数
def is_prime(num: int) -> bool:
    if num <= 1:
        return True
    for i in range (2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# 练习：求两个数的最小公倍数
def lcm(x: int, y: int) -> int:
    return  x * y // gcd(x, y)

# 练习：求两个数的最大公约数
def gcd(x: int, y: int) -> int:
    while x % y != 0:
        x, y = y , x % y
    return y

print(gcd(12, 16))
print(lcm(12, 16))

# 
def ptp(data):
    return max(data) - min(data)

def mean(data):
    return sum(data) / len(data)

def median(data):
    """中位数"""
    temp, size = sorted(data), len(data)
    if size % 2 != 0:
        return temp[size // 2]
    else:
        return mean(temp[size // 2 - 1:size // 2 + 1])

def var(data, ddof=1):
    """方差"""
    x_bar = mean(data)
    temp = [(num - x_bar) ** 2 for num in data]
    return sum(temp) / (len(temp) - ddof)

def std(data, ddof=1):
    """标准差"""
    return var(data, ddof) ** 0.5


def cv(data, ddof=1):
    """变异系数"""
    return std(data, ddof) / mean(data)


def describe(data):
    """输出描述性统计信息"""
    print(f'均值: {mean(data)}')
    print(f'中位数: {median(data)}')
    print(f'极差: {ptp(data)}')
    print(f'方差: {var(data)}')
    print(f'标准差: {std(data)}')
    print(f'变异系数: {cv(data)}')

print(describe([1, 2, 3, 4, 5]))


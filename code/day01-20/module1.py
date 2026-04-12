# 计算阶乘
def fac(num): 
    result = 1
    for n in range(2, num + 1):
        result *= n
    return result
print(fac(5))


# 使用类型注解，指定参数和返回值的类型
def fac2(num: int) -> int:
    result = 1
    for n in range(2, num + 1):
        result *= n
    return result
print(fac2(5))


def adj_triangle(a: int, b: int, c: int) -> bool:
    return a + b > c and a + c > b and b + c > a
# 不想按照从左到右的顺序依次给出a、b、c 三个参数的值，也可以使用关键字参数
print(adj_triangle(a = 3, c = 4, b = 5))

def adj_triangle1(a: int, b: int, c: int, /) -> bool:
    return a + b > c and a + c > b and b + c > a
# 强制位置参数，必须按照顺序给出，不能使用关键字参数
print(adj_triangle1(3,4,5))

def adj_triangle1(*, a: int, b: int, c: int) -> bool:
    return a + b > c and a + c > b and b + c > a
# 用*设置命名关键字参数，必须按照关键字给出，不能使用位置参数
print(adj_triangle1(a = 3, c = 4, b = 5))

# 参数可以拥有默认值，但是必须要放在最后面
def adj_triangle2(a: int, b: int, c: int = 1) -> bool:
    return a + b > c and a + c > b and b + c > a
print(adj_triangle2(3,3))

# 可变参数
# 调用函数时传入的参数会保存到一个元组，通过对该元组的遍历，可以获取传入函数的参数
def mymax(i: int, *args: int) -> int:
    max = i
    for arg in args:
        if arg > max:
            max = arg
    return max
print(mymax(1,2,3,4,5))

# * args 可以接收0个或任意多个位置参数
# **kwargs 可以接收0个或任意多个关键字参数
def foo(*args, **kwargs):
    print(args)
    print(kwargs)
foo(3, 2.1, True, name='骆昊', age=43, gpa=4.95)

# 装饰器
# 装饰器是一种特殊的函数，它可以在调用时固定住一些参数，返回一个新的函数。

# def time_record(func):
#     def wrapper(*args, **kwargs):
#         import time
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         end_time = time.time()
#         print(f"{func.__name__}运行时间：{end_time - start_time}秒")
#         return result
#     return wrapper

# def upload_file(file_path):
#     """模拟上传文件的函数"""
#     import time
#     time.sleep(2)  # 模拟上传文件需要的时间
#     print(f"文件{file_path}上传成功！")
    
# # 使用装饰器来记录上传文件的时间
# upload_file = time_record(upload_file)

# upload_file("test.txt")

# # 也可以使用@符号来简化装饰器的使用
# @time_record
# def upload_file2(file_path):
#     """模拟上传文件的函数"""
#     import time
#     time.sleep(2)  # 模拟上传文件需要的时间
#     print(f"文件{file_path}上传成功！")

# upload_file2("test2.txt")

# # functools模块的wraps函数也是一个装饰器
# # 所以定义装饰器时，应该使用functools.wraps来修饰内部函数，这样可以保留原函数的元信息（如函数名、文档字符串等）。
# import functools

# def new_time_record(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         import time
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         end_time = time.time()
#         print(f"{func.__name__}运行时间：{end_time - start_time}秒")
#         return result
#     return wrapper

# @new_time_record
# def upload_file3(file_path):
#     """模拟上传文件的函数"""
#     import time
#     time.sleep(2)  # 模拟上传文件需要的时间
#     print(f"文件{file_path}上传成功！") 
    
# upload_file3("test3.txt")

# # 可以通过被装饰函数的__wrapped__属性获得被装饰之前的函数
# # 但是自己定义的装饰器没有使用functools.wraps修饰内部函数，所以__wrapped__属性不存在
# upload_file3.__wrapped__("test3.txt")

# 递归计算斐波那契数列
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(5))  # 输出55

# 使用递归计算非常的慢，因为它会重复计算很多次相同的值。
# 为什么会计算很多次相同的值？
# 因为递归函数在每次调用时，都会计算一次n-1和n-2的斐波那契数列值。
# 所以，当n很大时，递归函数会重复计算很多次相同的值，导致计算时间非常长。
# 例如计算 fibonacci(5) 时，递归函数会计算以下值：
# fibonacci(5) = fibonacci(4) + fibonacci(3)
# fibonacci(4) = fibonacci(3) + fibonacci(2)
# fibonacci(3) = fibonacci(2) + fibonacci(1)
# fibonacci(2) = fibonacci(1) + fibonacci(0)
# fibonacci(1) = 1
# fibonacci(0) = 0 

# fibonacci(5) = fibonacci(4) + fibonacci(3)
# 计算 fibonacci(4) = fibonacci(3) + fibonacci(2)
# 计算f(4)的中的f(3)
# 计算f(5)的中的f(3)
# 所以会计算非常的多次相同的值。

# python 默认递归层数是1000，如果超过这个层数，就会抛出RecursionError异常。
# 但是我们可以通过sys模块的setrecursionlimit函数来修改递归层，但是不建议修改递归层数，因为可能会导致程序崩溃。

# 可以使用funtools模块的lru_cache装饰器来缓存递归函数的结果，这样就可以避免重复计算相同的值，从而提高计算效率。
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(55))  # 输出55


# 如果递归是一个可以快速计算的函数，那么递归是非常方便的，
# 但是如果递归是一个需要重复计算很多次相同的值的函数，那么递归就不是一个好的选择了。
# 可以使用动态规划来避免重复计算相同的值，从而提高计算效率。
# 动态规划是一种分治思想，它将问题分解成多个子问题，每个子问题只计算一次，从而避免重复计算。
# 例如计算 fibonacci(5) 时，动态规划会计算以下值：
# fibonacci(5) = fibonacci(4) + fibonacci(3)
# fibonacci(4) = fibonacci(3) + fibonacci(2)
# fibonacci(3) = fibonacci(2) + fibonacci(1)
# fibonacci(2) = fibonacci(1) + fibonacci(0)
# fibonacci(1) = 1
# fibonacci(0) = 0 
# 计算 fibonacci(5) 时，动态规划会先计算 fibonacci(0) 和 fibonacci(1)，然后计算 fibonacci(2)，再计算 fibonacci(3)，最后计算 fibonacci(4) 和 fibonacci(5)，这样就避免了重复计算相同的值。
def fibonacci2(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib = [0, 1]
        for i in range(2, n+1):          
            # 这里使用了一个列表来存储已经计算过的斐波那契数列值，这样就避免了重复计算相同的值。
            # 相当于使用空间换时间的方式来提高计算效率。   
            fib.append(fib[i-1] + fib[i-2])
        return fib[n]

print(fibonacci2(55))  # 输出55










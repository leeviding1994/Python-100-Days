# 不同于 C、C++、Java 等编程语言，Python 中没有用花括号来构造代码块而是使用缩进的
# 方式来表示代码的层次结构，如果if条件成立的情况下需要执行多条语句，只要保持多条语句
# 具有相同的缩进就可以了。换句话说，若干行连续的语句如果保持了相同的缩进，那么它们就
# 属于同一个代码块，相当于是一个执行的整体。缩进可以使用任意数量的空格，但通常使用4个
# 空格，强烈建议大家不要使用制表键（Tab键）来缩进代码，如果你已经习惯了这么做，可以设
# 置你的代码编辑器自动将 1 个制表键变成 4 个空格，很多代码编辑器都支持这项功能，
# PyCharm 中默认也是这样设定的。还有一点，在 C、C++、Java 等编程语言中，
# 18.5 <= bmi < 24要写成两个条件bmi >= 18.5和bmi < 24，然后把两个条件用与运算符
# 连接起来，Python 中也可以这么做，例如刚才的if语句也可以写成
# if bmi >= 18.5 and bmi < 24:，但是没有必要，难道if 18.5 <= bmi < 24:这个写法它不香吗

height = float(input('身高(cm)：'))
weight = float(input('体重(kg)：'))
bmi = weight / (height / 100) ** 2
print(f'{bmi = :.1f}')
if 18.5 <= bmi < 24:
    print('你的身材很棒！')
else:
    print('你的身材不是那么棒！')

status_code = int(input('响应状态码: '))
match status_code:
    case 400: description = 'Bad Request'
    case 401: description = 'Unauthorized'
    case 403: description = 'Forbidden'
    case 404: description = 'Not Found'
    case 405: description = 'Method Not Allowed'
    case 418: description = 'I am a teapot'
    case 429: description = 'Too many requests'
    case _: description = 'Unknown Status Code'
print('状态码描述:', description)


"""
计算三角形的周长和面积

Version: 1.0
Author: 骆昊
"""
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
if a + b > c and a + c > b and b + c > a:
    perimeter = a + b + c
    print(f'周长: {perimeter}')
    s = perimeter / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    print(f'面积: {area}')
else:
    print('不能构成三角形')
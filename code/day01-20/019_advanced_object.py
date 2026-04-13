# 可见性使用下划线前缀
# __ 表示私有属性，不能在类外部访问，子类也不能访问私有属性
# _ 表示保护属性，只能在类内部及子类访问, 但是可以在类外部访问（技术上），只是不建议这样做

class Student:

    def __init__(self, name, age):
        #  Python 会将 __attr 自动转换为 _ClassName__attr（例如 _Person__age），从而在外部和子类中无法通过原名称访问
        self.__name = name
        self.__age = age

    def study(self, course_name):
        print(f'{self.__name}正在学习{course_name}.')

stu = Student('张三', 18)
stu.study('Python')

# print(stu.__name) # 报错，不能访问私有属性
print(stu._Student__name) # 可以访问保护属性，Python 会自动转换为 _ClassName__attr

# Python 语言属于动态语言
# 可以动态添加属性
stu.sex = '男'
print(stu.sex)

# 如使用 Python 语言中的__slots__魔法方法，可以限制类的属性，只能包含在__slots__中定义的属性
class Student2:
    __slots__ = ('__name', '__age')
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    def study(self, course_name):
        print(f'{self.__name}正在学习{course_name}.')

stu2 = Student2('李四', 19)
stu2.study('Python')
# stu2.sex = '男' # 报错，不能添加__slots__中定义的属性 

# 使用 @staticmethod 定义静态方法
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

result = MathUtils.add(3, 5)
print(result)

# 使用 @classmethod 定义类方法
class Student3:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # 类方法的第一个参数是 cls，代表类本身
    @classmethod
    def create_student(cls, name, age):
        return cls(name, age)
    def study(self, course_name):
        print(f'{self.name}正在学习{course_name}.')

stu3 = Student3.create_student('王五', 20)
stu3.study('Python')

# property 装饰器可以把函数作为属性来调用
class Student4:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def get_age(self):
        return self.age
    @property
    def age_days(self):
        return self.age * 365

stu4 = Student4('赵六', 21)
print(stu4.age_days)
stu4.age = 22
print(stu4.age_days)

# 继承
# object 是所有类的基类，所有类都继承自 object 类
# 可以多继承

class Person:
    """人"""

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def eat(self):
        print(f'{self.name}正在吃饭.')
    
    def sleep(self):
        print(f'{self.name}正在睡觉.')


class Student(Person):
    """学生"""
    
    def __init__(self, name, age):
        super().__init__(name, age)
    
    def study(self, course_name):
        print(f'{self.name}正在学习{course_name}.')


class Teacher(Person):
    """老师"""

    def __init__(self, name, age, title):
        super().__init__(name, age)
        self.title = title
    
    def teach(self, course_name):
        print(f'{self.name}{self.title}正在讲授{course_name}.')



stu1 = Student('白元芳', 21)
stu2 = Student('狄仁杰', 22)
tea1 = Teacher('武则天', 35, '副教授')
stu1.eat()
stu2.sleep()
tea1.eat()
stu1.study('Python程序设计')
tea1.teach('Python程序设计')
stu2.study('数据科学导论')


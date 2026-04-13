# 类里的方法第一个是self参数，代表当前实例对象
class Student:

    # 构造方法，用于初始化实例对象的属性
    # 除非有默认参数，否则必须在创建实例对象时传递参数值
    def __init__(self, name, age):
        """初始化方法"""
        self.name = name
        self.age = age

    def study(self, course_name):
        print(f'{self.name}学生正在学习{course_name}.')

    def play(self, game_name):
        print(f'{self.name}学生正在玩{game_name}.')

student1 = Student('张三', 18)
student2 = Student('李四', 19)
print(student1)
print(student2)
student1.study('Python')
student2.play('篮球')



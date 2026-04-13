# 计算员工工资
from abc import ABCMeta, abstractmethod

# 定义一个抽象类，表示员工
# 使用ABCMeta元类和abstractmethod装饰器来定义抽象方法
class Employee(metaclass=ABCMeta):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_salary(self):
        pass
    
class Manager(Employee):
    def get_salary(self):
        return 15000.0
    
class Programmer(Employee):
    def __init__(self, name, working_hour=0):
        super().__init__(name)
        self.working_hour = working_hour

    def get_salary(self):
        return 200 * self.working_hour

class Salesman(Employee):
    def __init__(self, name, sales=0):
        super().__init__(name)
        self.sales = sales

    def get_salary(self):
        return 1800 + self.sales * 0.05
    
emps = [Manager('刘备'), Programmer('诸葛亮'), Manager('曹操'), Programmer('荀彧'), Salesman('张辽')]
for emp in emps:
    # 两种方式判断对象类型，第一种是使用isinstance()函数，第二种是直接比较类型
    # if isinstance(emp, Programmer):
    if type(emp) == Programmer:
        emp.working_hour = int(input(f'请输入{emp.name}本月工作时间: '))
    elif isinstance(emp, Salesman):
        emp.sales = float(input(f'请输入{emp.name}本月销售额: '))
    print(f'{emp.name}本月工资为: ￥{emp.get_salary():.2f}元')
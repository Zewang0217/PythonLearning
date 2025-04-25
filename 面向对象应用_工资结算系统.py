from abc import ABCMeta, abstractmethod

class Employee(metaclass=ABCMeta):
  """员工"""

  def __init__(self, name):
    self.name = name

  @abstractmethod
  def get_salary(self):
    """结算月薪"""
    pass

class Manager(Employee):
  """部门经理"""

  def get_salary(self):
    return 15000.0

class Programmer(Employee):
  """程序员"""

  def __init__(self, name, working_hour=0):
    super().__init__(name)
    self.working_hour = working_hour

  def get_salary(self):
    return 200 * self.working_hour

class Salesman(Employee):
  """销售"""

  def __init__(self, name, sales=0):
    super().__init__(name)
    self.sales = sales

  def get_salary(self):
    return 1800.0 + self.sales * 0.05

emps = [Manager('刘备'), Programmer('张飞'), Salesman('关羽')]
for emp in emps:
  if isinstance(emp, Programmer):
    emp.working_hour = int(input('请输入%s的作息时间' % emp.name))
  elif isinstance(emp, Salesman):
    emp.sales = float(input('请输入%s的销售额' % emp.name))
  print(f'{emp.name}的工资是{emp.get_salary()}')
class Student:
  """学生"""
  def __init__(self, name, age):
    """初始化方法"""
    self.name = name
    self.age = age

  def study(self, course_name):
    print(f'{self.name}正在学习{course_name}.')

  def play(self):
    print(f'{self.name}正在打游戏.')

# stu1 = Student("Zewang", 19)
#
# print(stu1)
# print(hex(id(stu1)))
#
#
# stu1.study('C++')

class Point:
  """平面上的点"""

  def __init__(self, x=0, y=0):
    """
    初始化方法
    :param x: 横坐标
    :param y: 纵坐标
    """
    self.x, self.y = x, y

  def distance_to(self, other):
    """计算与另一个点的距离
    :param other:另一个点
    """
    dx = self.x - other.x
    dy = self.y - other.y
    return (dx ** 2 + dy ** 2) ** 0.5

  def __str__(self):
    """返回可打印的字符串表示"""
    return f'({self.x}, {self.y})'

# p1 = Point(1, 2)
# p2 = Point(3, 4)
# print(p1)
# print(p2.distance_to(p1))

import time

class Clock:
  """数字时钟"""

  def __init__(self, hour=0, minute=0, sec=0):
    """

    :param hour: 小时
    :param minute: 分钟
    :param sec: 秒
    """
    self.hour = hour
    self.minute = minute
    self.sec = sec

  def run(self):
    """走字"""
    self.sec += 1
    if self.sec == 60:
      self.sec = 0
      self.minute += 1
      if self.minute == 60:
        self.minute = 0
        self.hour += 1
        if self.hour == 24:
          self.hour = 0

  def show(self):
    """显示时间"""
    return f'{self.hour:02d}:{self.minute:02d}:{self.sec:02d}'

clock = Clock(23, 59, 59)
while True:
  print(clock.show())
  time.sleep(1)
  clock.run()
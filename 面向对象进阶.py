class Student:
  def __init__(self, name, age):
    self.__name = name
    self.__age = age
  def study(self, course_name):
    print(f'{self.__name}正在学习{course_name}')

# stu = Student('Zewang', 19)
# print(stu._Student__name)
# stu.sex = '男'

class Triagle(object):
  """三角形"""

  def __init__(self, a, b, c):
    self.a = a
    self.b = b
    self.c = c

  @staticmethod
  def is_valid(a, b, c):
    return a + b > c and b + c > a and a + c > b

  @property
  def perimeter(self):
    return self.a + self.b + self.c

  # @property
  def area(self):
    p = self.perimeter / 2
    return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5

# t = Triagle(3, 4, 5)
# print(f'周长：{t.perimeter}')
# print(f'面积：{t.area()}')

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def eat(self):
    print(f'{self.name}正在吃饭')

  def sleep(self):
    print(f'{self.name}正在睡觉')

class Student1(Person):

  def __init__(self, name, age):
    super().__init__(name, age)

  def study(self,course_name):
    print(f'{self.name}正在学习{course_name}')

class Teacher(Person):

  def __init__(self, name, age, title):
    super().__init__(name, age)
    self.title = title

  def teach(self, course_name):
    print(f'{self.name}正在 teach {course_name}')

p = Person('白元芳', 25)
p.eat()

stu1 = Student1('白元芳', 21)
stu2 = Student1('狄仁杰', 22)
tea1 = Teacher('武则天', 35, '副教授')
stu1.eat()
stu2.sleep()
tea1.eat()
stu1.study('Python程序设计')
tea1.teach('Python程序设计')
stu2.study('数据科学导论')
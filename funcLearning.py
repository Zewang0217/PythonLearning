"""
计算C(m, n)
"""


# m = int(input('m = '))
# n = int(input('n = '))
#
# fm = 1
# for num in range(1, m + 1):
#   fm *= num
# fn = 1
# for num in range(1, n + 1):
#   fn *= num
# fk = 1
# for num in range(1, m - n + 1):
#   fk *= num
#
# print(fm // fn // fk)

"""
使用函数
"""

# from math import factorial as f
#
# def fac(num):
#   result = 1
#   for n in range(2, num + 1):
#     result *= n
#   return result
#
# m = int(input('m = '))
# n = int(input('n = '))
# print(fac(m) // fac(n) // fac(m - n))
# print(f(m) // f(n) // f(m - n))

"""
参数
"""
# def judgement(a, b, c):
#   return a + b > c and b + c > a and c + a > b
#
# print(judgement(3, 4, 5))
# print(judgement(b=2, c=3, a=1))

"""
赌博
"""
# from random import randrange
#
#
# def roll_dice(n=2):
#   total = 0
#   for _ in range(n):
#     total += randrange(1, 7)
#   return total
#
# print(roll_dice())
# print(roll_dice(3))

# def add(a=0, b=1, c=2):
#   return a + b + c
# print(add())
# print(add(1, 3))
# print(add(b=3, c=4))

def add(*args):
  result = 0
  for arg in args:
    if type(arg) in (int, float):
      result += arg
  return result

# print(add(1, 3, 5))
# print(add())
# print(add(1, 's', 3))

# def foo(*args, **kwargs):
#   print(args)
#   print(kwargs)
#
# foo(2, 5.3, True, name='Zewang', age=19)
def foo():
  print('hello')

def foo():
  print(2)

foo()
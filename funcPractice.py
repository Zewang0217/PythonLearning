import random
import string

ALL_CHARS = string.digits + string.ascii_letters
"""
说明1：string模块的digits代表0到9的数字构成的字符串'0123456789'，
string模块的ascii_letters代表大小写英文字母构成的字符串'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'。

说明2：random模块的sample和choices函数都可以实现随机抽样，
sample实现无放回抽样，这意味着抽样取出的元素是不重复的；
choices实现有放回抽样，这意味着可能会重复选中某些元素。
这两个函数的第一个参数代表抽样的总体，而参数k代表样本容量，
需要说明的是choices函数的参数k是一个命名关键字参数，
在传参时必须指定参数名。
"""

def generate_code(*, code_len=4):
  """
      生成指定长度的验证码
      :param code_len: 验证码的长度(默认4个字符)
      :return: 由大小写英文字母和数字构成的随机验证码字符串
      """
  return ''.join(random.choices(ALL_CHARS, k=code_len))

# for _ in range(5):
#   print(generate_code())
#   print(generate_code(code_len=7))


"""
判断素数
"""

def is_prime(n: int) -> bool:
  """
  判断素数的函数
  :param n: 需要判断的整数
  :return: True表示n是素数，False表示n不是素数
  """
  for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
      return False
    return True

# n = int(input('n= '))
# print(is_prime(n))

"""
例三
最大公约数和最小公倍数
"""
def lcm(x: int, y: int) -> int:
  """
  求两个数的最小公倍数
  :param x: 第一个整数
  :param y: 第二个整数
  :return: 最小公倍数
  """
  return x * y // gcd(x, y)

def gcd(x: int, y: int) -> int:
  """
  求两个数的最大公约数
  :param x: 第一个整数
  :param y: 第二个整数
  :return: 最大公约数
  """
  while y % x != 0:
    x, y = y % x, x # 辗转相除
  return x

# x = int(input('x= '))
# y = int(input('y= '))
# print(f'{x}和{y}的最大公约数是{gcd(x, y)}')
# print(f'{x}和{y}的最小公倍数是{lcm(x, y)}')

"""
例四
数据统计（列表）
"""
def ptp(data):
  """ 极差 """
  return max(data) - min(data)

def mean(data):
  """ 算数平均 """
  return sum(data) / len(data)

def median(data):
  """ 中位数 """
  temp, size = sorted(data), len(data)
  if size % 2 != 0:
    return temp[size // 2]
  else:
    return mean(temp[size // 2 - 1: size // 2 + 1])

"""
ddof 代表了可以调整的自由度，默认值为 1。
在计算样本方差和样本标准差时，需要进行自由度校正；
如果要计算总体方差和总体标准差，可以将ddof参数赋值为 0，
即不需要进行自由度校正
"""
def var(data, ddof=1):
  """ 方差 """
  x_bar =  mean(data)
  temp = [(num - x_bar) ** 2 for num in data]
  return sum(temp) / (len(temp) - ddof)

def std(data, ddof=1):
  """ 标准差 """
  return var(data, ddof) ** 0.5

def cv(data, ddof=1):
  """ 变异系数 """
  return std(data, ddof) / mean(data)

def describe(data):
  """ 数据统计 """
  return {
    'ptp': ptp(data),
    'mean': mean(data),
    'median': median(data),
    'var': var(data),
    'std': std(data),
    'cv': cv(data)
  }

# print(describe([1, 2, 3, 4, 5]))

"""
双色球
"""
import random
RED_BALLS = [i for i in range(1, 34)]
BLUE_BALLS = [i for i in range(1, 17)]

def choose():
  """
  生成一组随机号码
  :return:保存随机号码的列表
  """
  selected_balls = random.sample(RED_BALLS, 6)
  selected_balls.sort()
  selected_balls.append(random.choice(BLUE_BALLS))
  return selected_balls

def display(balls):
  """
  打印出双色球号码
  :param balls: 随机号码列表
  """
  for ball in balls[:-1]:
    print(f'\033[031m{ball:0>2d}\033[0m', end=' ')
  print(f'\033[034m{balls[-1]:0>2d}\033[0m')

# n = int(input('生成几注号码: '))
# for _ in range(n):
#     display(choose())

"""
高阶函数
"""

def calc(*args, **kwargs):
  items = list(args) + list(kwargs.values())
  result = 0
  for item in items:
    if type(item) in (int, float):
      result += item
  return result

# print(calc(1, 2, 4, 5, a=3, b=5))

def calc2(init_value, op_func, *args, **kwargs):
  items = list(args) + list(kwargs.values())
  result = init_value
  for item in items:
    if type(item) in (int, float):
      result = op_func(result, item)
  return result

def add(x, y):
  return x + y
def sub(x, y):
  return x - y
def mul(x, y):
  return x * y

# print(calc2(0, add, 1, 3, 4))
# print(calc2(3, mul, 2, a=3))

# old_nums = [32, 12, 8, 99, 53]
# new_nums = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, old_nums)))
# print(new_nums)

import functools
import operator

fac2 = lambda n: functools.reduce(operator.mul, range(2, n + 1), 1)

is_prime2 = lambda x: all(map(lambda f: x % f != 0, range(2, int(x ** 0.5) + 1)))

# print(fac2(4))
# print(is_prime2(5))

int2 = functools.partial(int, base=2)
int8 = functools.partial(int, base=8)
int16 = functools.partial(int, base=16)

# print(int('1001'))
#
# print(int2('1001'))
# print(int8('1001'))
# print(int16('1001'))

import time

# start = time.time()
# download('python入门到如土')
# end = time.time()
# print(f'download time: {end - start:.2f}seconds')
# start = time.time()
# upload('python直接入土')
# end = time.time()
# print(f'upload time: {end - start:.2f}seconds')

def record_time(func):
  def wrapper(*args, **kwargs):
    start = time.time()
    result = func(*args, **kwargs)
    end = time.time()
    print(f'{func.__name__}time: {end - start:.2f}')
    return result
  return wrapper

@record_time
def download(filename):
  print(f'downloading{filename}')
  time.sleep(random.random() * 6)
  print(f'{filename}download')

@record_time
def upload(filename):
  print(f'uploading{filename}')
  time.sleep(random.random() * 8)
  print(f'{filename}upload')

# download = record_time(download)
# upload = record_time(upload)
# download('python入门到入土')
# upload('python直接入土')

@functools.lru_cache()
def fac(num):
  if num in (0, 1):
    return 1
  return num * fac(num - 1)

print(fac(10))
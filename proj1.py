print("Hello, py")
import math
# 单行注释

# 变量类型：int, float, str, bool

# 变量命名，大小写敏感
# 惯例1：变量名通常使用小写英文字母，多个单词用下划线进行连接。
# 惯例2：受保护的变量用单个下划线开头。
# 惯例3：私有的变量用两个下划线开头。

"""
使用变量保存数据并进行加减乘除运算

Version: 1.0
Author: Zewang
"""
# a = 45        # 定义变量a，赋值45
# b = 12        # 定义变量b，赋值12
# print(a, b)   # 45 12
# print(a + b)  # 57
# print(a - b)  # 33
# print(a * b)  # 540
# print(a / b)  # 3.75

# 可以使用type函数对变量的类型进行检查

# a = 100
# b = '123.43'
# c = "Hello, Python"
# d = True
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))

# 也可以改变变量类型
'''
int()：将一个数值或字符串转换成整数，可以指定进制。
float()：将一个字符串（在可能的情况下）转换成浮点数。
str()：将指定的对象转换成字符串形式，可以指定编码方式。
chr()：将整数（字符编码）转换成对应的（一个字符的）字符串。
ord()：将（一个字符的）字符串转换成对应的整数（字符编码）。
'''
# a = 100
# b = 123.45
# c = '123'
# d = '100'
# e = '123.45'
# f = 'hello, world'
# g = True
# print(float(a))         # int类型的100转成float，输出100.0
# print(int(b))           # float类型的123.45转成int，输出123
# print(int(c))           # str类型的'123'转成int，输出123
# print(int(c, base = 16))  # str类型的'123'按十六进制转成int，输出291
# print(int(d, base = 2))   # str类型的'100'按二进制转成int，输出4
# print(float(e))         # str类型的'123.45'转成float，输出123.45
# print(bool(f))          # str类型的'hello, world'转成bool，输出True
# print(int(g))           # bool类型的True转成int，输出1
# print(chr(a))           # int类型的100转成str，输出'd'
# print(ord('d'))         # str类型的'd'转成int，输出100
'''
说明：
str类型转int类型时可以通过base参数来指定进制，可以将字符串视为对应进制的整数进行转换。
str类型转成bool类型时，只要字符串有内容，不是''或""，对应的布尔值都是True。
bool类型转int类型时，True会变成1，False会变成0。
在 ASCII 字符集和 Unicode 字符集中， 字符'd'对应的编码都是100。
'''

# 运算符

# print(321 + 12)     # 加法运算，输出333
# print(321 - 12)     # 减法运算，输出309
# print(321 * 12)     # 乘法运算，输出3852
# print(321 / 12)     # 除法运算，输出26.75
# print(321 // 12)    # 整除运算，输出26
# print(321 % 12)     # 求模运算，输出9
# print(321 ** 12)    # 求幂运算，输出1196906950228928915420617322241
# print(2 + 3 * 5)           # 17
# print((2 + 3) * 5)         # 25
# print((2 + 3) * 5 ** 2)    # 125
# print(((2 + 3) * 5) ** 2)  # 625

# a = 10
# b = 3
# a += b        # 相当于：a = a + b
# a *= a + 2    # 相当于：a = a * (a + 2)
# print(a)      # 大家算一下这里会输出什么
# print((a := 10))  # 10
# print(a)          # 10

# 运算符和表达式应用
# f = float(input('请输入一个华氏温度：'))
# c = (f - 32) / 1.8
# # print('%.1f华氏温度 = %.1f摄氏度' %(f, c))
# print(f'{f:.1f}华氏度 = {c:.1f}摄氏度')

# eg2
# radius = float(input('请输入圆的半径: '))
# perimeter = 2 * 3.1416 * radius
# area = math.pi * radius * radius
# # print(f'周长: {perimeter:.2f}')
# # print(f'面积: {area:.2f}')
# print(f'{perimeter = :.2f}') # 输出：perimeter = 18.85
# print(f'{area = :.2f}') # 输出：area = 28.27

# eg3
year = int(input('请输入年份: '))
is_leap = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
print(f'{is_leap = }')
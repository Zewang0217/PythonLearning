# items1 = [1, 2, 3, 4, 5]
# items2 = ['python', 'java', 'c++']
# print(items1 + items2) #[1, 2, 3, 4, 5, 'python', 'java', 'c++']
# print(items1) #[1, 2, 3, 4, 5]
# print(items2) #['python', 'java', 'c++']
# print(items1 * 3) #[1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
# print('c++' not in items2)
# print(1 in items1)
#
# languages = ['Python', 'Java', 'C++', 'Kotlin']
# for index in range(len(languages)):
#     print(languages[index])

# languages = ['Python', 'Java', 'C++', 'Kotlin']
# for language in languages:
#     print(language)

# 模拟色子概率
# import random
#
# counters = [0] * 6
# for _ in range(6000):
#   up = random.randrange(1, 7)
#   counters[up - 1] += 1
# for up in range(1, 7):
#   print(f'{up}点出现了{counters[up - 1]}次')

# language = ['Python', 'Java', 'C++', 'Kotlin', 'Python', 'Python']
# language.remove('Python')
# print(language)

# 生成式
# items = []
# for i in range(1, 100):
#   if i % 3 == 0:
#     items.append(i)
# print(items)

# items = [i for i in range(1, 100) if i % 3 == 0]
# print(items)

# nums1 = [1, 2, 3, 4, 5]
# nums2 = []
# for num in nums1:
#   nums2.append(num ** 2)
# print(nums2)

# nums1 = [1, 2, 3, 4, 5]
# nums2 = [num ** 2 for num in nums1]
# print(nums2)

# scores = [[95, 83, 92], [80, 75, 82], [92, 97, 90], [80, 78, 69], [65, 66, 89]]
# print(scores[0])
# print(scores[1][2])

# scores = []
# for _ in range(5):
#   temp = []
#   for _ in range(3):
#     temp.append(int(input('请输入： ')))
#   scores.append(temp)
# print(scores)

# import random
# scores = [[random.randrange(60, 101) for _ in range(3)] for _ in range(5)]
# print(scores)

"""
双色球模拟
"""
# import random
#
# red_balls = list(range(1, 34))
# selected_balls = []
#
# for _ in range(6):
#   # 生成随机整数代表选中的红色球索引位置
#   index = random.randrange(len(red_balls))
#   # 添加选中的球
#   selected_balls.append(red_balls.pop(index))
# selected_balls.sort()
# for ball in selected_balls:
#   print(f'\033[031m{ball:0>2d}\033[0m', end=' ')
# blue_ball = random.randrange(1, 17)
# print(f'\033[034m{blue_ball:0>2d}\033[0m')

# import random
#
# n = int(input('生成几注号码: '))
# red_balls = [i for i in range(1, 34)]
# blue_balls = [i for i in range(1, 17)]
# for _ in range(n):
#     # 从红色球列表中随机抽出6个红色球（无放回抽样）
#     selected_balls = random.sample(red_balls, 6)
#     # 对选中的红色球排序
#     selected_balls.sort()
#     # 输出选中的红色球
#     for ball in selected_balls:
#         print(f'\033[031m{ball:0>2d}\033[0m', end=' ')
#     # 从蓝色球列表中随机抽出1个蓝色球
#     blue_ball = random.choice(blue_balls)
#     # 输出选中的蓝色球
#     print(f'\033[034m{blue_ball:0>2d}\033[0m')

import random

from rich.console import Console
from rich.table import Table

# 创建控制台
console = Console()

n = int(input('生成几注号码： '))
red_balls = [i for i in range(1, 34)]
blue_balls = [i for i in range(1, 17)]

# 创建表格并添加表头
table = Table(show_header=True)
for col_name in ('序号', '红球', '蓝球'):
    table.add_column(col_name, justify='center')

for i in range(n):
    selected_balls = random.sample(red_balls, 6)
    selected_balls.sort()
    blue_ball = random.choice(blue_balls)

    # 向表格中添加行
    table.add_row(
        str(i + 1),
        f'[red]{" ".join([f"{ball:0>2d}" for ball in selected_balls])}[/red]',
        f'[blue]{blue_ball:0>2d}[/blue]'
    )

console.print(table)
i
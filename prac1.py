'''
输出100以内的素数
'''
# for num in range(2, 100):
#   is_prime = True
#   for i in range(2, int(num ** 0.5) + 1):
#     if num % i == 0:
#       is_prime = False
#       break
#
#   if is_prime:
#     print(num)

'''
fibonacci sequence 前二十个
'''
# a, b = 0, 1
# for _ in range(20):
#   a, b = b, a + b
#   print(a)

'''
100到900以内的水仙花数
'''
# for num in range(100, 1000):
#   low = num % 10
#   mid = num // 10 % 10
#   high = num // 100
#   if num == low ** 3 + mid ** 3 + high ** 3:
#     print(num)

'''
反转正整数
'''
# num = int(input('num = '))
# reversed_num = 0
# while num > 0:
#   reversed_num = reversed_num * 10 + num % 10
#   num //= 10
# print(reversed_num)


'''
百钱百鸡
'''
# for x in range(0, 21): # x = 公鸡
#   for y in range(0, 34): # y = 母鸡
#     for z in range(0, 100, 3):
#       if x + y + z == 100 and x * 5 + y * 3 + z // 3 == 100:
#         print(f'公鸡: {x}只, 母鸡: {y}只, 小鸡: {z}只')

'''
CRAPS赌博游戏
'''
import random

money = 1000
while money > 0:
  print(f'你的总资产为：{money}元')
  # 下注金额必须大于0且小于等于玩家总资产
  while True:
    debt = int(input('请下注：'))
    if 0 < debt <= money:
      break
    # 用两个1到6均匀分布的随机数相加模拟摇两颗色子得到的点数
  first_point = random.randrange(1, 7) + random.randrange(1, 7)
  if first_point == 7 or first_point == 11:
    print('玩家胜\n')
    money += debt
  elif first_point == 2 or first_point == 3 or first_point == 12:
    print('庄家胜\n')
    money -= debt
  else:
    # 如果第一次没分出胜负，再来一次
    while True:
      current_point = random.randrange(1, 7) + random.randrange(1, 7)
      if current_point == 7:
        print('庄家胜\n')
        money -= debt
        break
      elif current_point == first_point:
        print('玩家胜\n')
        money += debt
        break
print('你破产了，游戏结束')

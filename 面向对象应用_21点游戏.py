from enum import Enum

class Suite(Enum):
  """花色（枚举）"""
  SPADE, HEART, CLUB, DIAMOND = range(4)

# for suite in Suite:
#   print(f'{suite}: {suite.value}')

class Card:
  """牌"""

  def __init__(self, suite, face):
    self.suite = suite
    self.face = face

  def __repr__(self):
    suites = '♠ ♡ ♣ ♢'.split()
    faces = [' ', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    return f'{suites[self.suite.value]}{faces[self.face]}'

  def __lt__(self, other):
    if self.suite == other.suite:
      return self.face < other.face
    return self.suite.value < other.suite.value

  @property
  def value(self):
    """获取牌的点数"""
    if 1 < self.face < 10: # 2 ~ 9
      return self.face
    elif self.face >= 10: # 10, J, Q, K
      return 10
    else: # A
      return 11

# card1 = Card(Suite.SPADE, 5)
# card2 = Card(Suite.HEART, 13)
# print(card1)
# print(card2)

import random

class Poker:
  """扑克"""
  def __init__(self):
    self.current = 0
    self.cards = [Card(suite, face)
                  for suite in Suite
                  for face in range(1, 14)] # 52张牌构成的列表

  def shuffle(self):
    """洗牌"""
    self.current = 0
    random.shuffle(self.cards)  # 通过random模块的shuffle函数实现随机乱序

  def deal(self):
    """发牌"""
    if self.current == 52:
      print('牌已发完，重新洗牌，继续游戏')
      self.current = 0
      self.shuffle()

    card = self.cards[self.current]
    self.current += 1

    return card

  @property
  def has_next(self):
    return self.current < len(self.cards)

# poker = Poker()
# print(poker.cards)
# poker.shuffle()
# print(poker.cards)
# print(poker.has_next)

class Player:
  """玩家"""
  def __init__(self, name):
    self.name = name
    self.cards = []
    self.score = 0

  def get_one(self, card):
    self.cards.append(card)
    self.calculate_score()
    print(f'{self.name}收到一张牌：{card}')

  def calculate_score(self):
    score = sum(card.value for card in self.cards)
    aces = sum(1 for card in self.cards if card.face == 1)
    while score > 21 and aces:
      score -= 10
      aces -= 1
    self.score = score

  def arrange(self):
    """整理手牌"""
    self.cards.sort()

  def show_cards(self, show_all=True):
    """明牌"""
    print(f'{self.name}的手牌：{self.cards} 当前点数：{self.score if show_all else "?"}')

  def clear_cards(self):
    """清空手牌"""
    self.cards = []
    self.score = 0

class BlackjackGame:
  """21点游戏"""
  def __init__(self):
    self.player_win = 0
    self.dealer_win = 0
    self.poker = Poker()
    self.player = Player('玩家')
    self.dealer = Player('庄家')

  def initial_deal(self):
    """初始发牌"""
    self.poker.shuffle()
    self.player.clear_cards()
    self.dealer.clear_cards()

    for _ in range(2):
      self.player.get_one(self.poker.deal())
      self.dealer.get_one(self.poker.deal())

  def player_turn(self):
    """玩家回合"""
    while True:
      self.player.show_cards()
      self.dealer.show_cards(show_all=False)

      if self.player.score >= 21:
        break

      action = input('要牌（h）还是停牌（s）？').lower()
      if action == 'h':
        self.player.get_one(self.poker.deal())
      elif action == 's':
        break
      else:
        print("无效输入，请输入'h' 或 'r' ")

  def dealer_turn(self):
    """庄家回合"""
    if self.player.score <= 21:
      while self.dealer.score < 17:
        self.dealer.get_one(self.poker.deal())

  def determine_winner(self):
    """判断胜负"""
    print('\n===最终结果===')
    self.player.show_cards()
    self.dealer.show_cards()

    if self.player.score > 21:
      self.dealer_win += 1
      print('玩家 bust，庄家胜')
    elif self.dealer.score > 21:
      self.player_win += 1
      print('庄家 bust，玩家胜')
    elif self.player.score > self.dealer.score:
      self.player_win += 1
      print('玩家胜')
    elif self.player.score < self.dealer.score:
      self.dealer_win += 1
      print('庄家胜')
    else:
      print('平局')

  def play_round(self):
    """进行一局游戏"""
    self.initial_deal()
    self.player_turn()
    self.dealer_turn()
    self.determine_winner()

  def play(self):
    """游戏主循环"""
    print("===21点游戏===")
    while True:
      self.play_round()

      if len(self.poker.cards) < 10:
        print('\n牌不够了，重新洗牌')
        self.poker = Poker()

      choice = input('再玩一次（y/n）？\n').lower()
      if choice == 'n':
        print('\n===总成绩===') # 显示最终成绩
        print(f'玩家胜：{self.player_win} 庄家胜：{self.dealer_win}')
        if self.player_win > self.dealer_win:
          print('恭喜玩家获胜！')
        elif self.player_win < self.dealer_win:
          print('庄家获胜！')
        else:
          print('平局！')
        print('游戏结束')
        break

# 开始游戏
# if __name__ == "__main__":
#   game = BlackjackGame()
#   game.play()

"""验证玩家，扑克，牌是否可用"""
# poker = Poker()
# poker.shuffle()
# players = [Player('东邪'), Player('西毒'), Player('南帝'), Player('北丐')]
# for _ in range(3):
#   for player in players:
#     player.get_one(poker.deal())
# # 玩家洗牌
# for player in players:
#   score = 0
#   for card in player.cards:
#     score += card.face
#
#   player.arrange()
#   print(f'{player.name}的牌：', end='')
#   print(player.cards)
#



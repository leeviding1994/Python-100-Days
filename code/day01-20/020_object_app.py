# 枚举
from enum import Enum

class Suite(Enum):
    """花色(枚举)"""
    SPADE, HEART, CLUB, DIAMOND = range(4)


# print(Suite.SPADE)

class Card:
    def __init__(self, suite, face):
        self.suite = suite
        self.face = face

    def view(self):
        faces = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        return self.suite, faces[self.face-1]

card = Card(Suite.HEART, 1)
card.view()

import random
class Poker:
    """扑克"""

    def __init__(self):
        self.cards = [Card(suite, face) 
                      for suite in Suite
                      for face in range(1, 14)]  # 52张牌构成的列表
        self.current = 0  # 记录发牌位置的属性

    def shuffle(self):
        """洗牌"""
        self.current = 0
        random.shuffle(self.cards)  # 通过random模块的shuffle函数实现随机乱序

    def deal(self):
        """发牌"""
        card = self.cards[self.current]
        self.current += 1
        return card

    @property
    def has_next(self):
        """还有没有牌可以发"""
        return self.current < len(self.cards)
    
poker = Poker()
print("\n".join(list(card.view() for card in poker.cards)))  # 洗牌前的牌
poker.shuffle()
print("\n".join(list(card.view() for card in poker.cards)))  # 洗牌后的牌

class Player:
    """玩家"""

    def __init__(self, name):
        self.name = name
        self.cards = []  # 玩家手上的牌

    def get_one(self, card):
        """摸牌"""
        self.cards.append(card)

    def arrange(self):
        """整理手上的牌"""
        self.cards.sort()
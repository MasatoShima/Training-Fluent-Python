# %%
"""
Name: Masato Shima
Description: Pythonic trump
Created by: Masato Shima
Created on: 2019/08/12
"""

# **************************************************
# ----- Import Library
# **************************************************
import collections
from typing import *
from random import choice


# **************************************************
# ----- Variables
# **************************************************
Card = collections.namedtuple("Card", ["rank", "suit"])

TypeCard = NamedTuple("Card", [("rank", int), ("suit", str)])


# **************************************************
# ----- Class
# **************************************************
class FrenchDeck:
	ranks = [str(n) for n in range(2, 11)] + list("JQKA")
	suits = "spades diamonds clubs hearts".split()

	def __init__(self):
		self.cards = [
			Card(rank=rank, suit=suit)
			for rank in self.ranks
			for suit in self.suits
		]

	def __len__(self):
		return len(self.cards)

	def __getitem__(self, position: int):
		return self.cards[position]


# %%
beer_card = Card(8, "spades")

print(beer_card)
print(beer_card.rank)
print(beer_card.suit)


# %%
deck = FrenchDeck()

# __len__ により要素の数を取得可能に
print(deck)
print(len(deck))

# __getitem__ により FrenchDeck Class は Iterable なデータ型として扱える
# Slicing
print(deck[0])
print(deck[-1])

# random ライブラリよりランダムな要素の取得
print(choice(deck))

# loop による要素の取得
for card in deck:
	print(card)

# 要素順の反転
for card in reversed(deck):
	print(card)

# in 演算子による要素の存在確認
print(Card(rank="Q", suit="hearts") in deck)
print(Card(rank="X", suit="hearts") in deck)

# カードの強さで sort
suit_values = {
	"spades": 3,
	"hearts": 2,
	"diamonds": 1,
	"clubs": 0
}


def spades_high(card):
	rank_value = FrenchDeck.ranks.index(card.rank)
	suit_value = suit_values[card.suit]
	value = rank_value * len(suit_values) + suit_value
	return value


for card in sorted(deck, key=spades_high):
	print(card)


# %%
# **************************************************
# ----- End
# **************************************************

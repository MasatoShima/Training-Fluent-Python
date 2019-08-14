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
from random import choice


# **************************************************
# ----- Variables
# **************************************************
Card = collections.namedtuple("Card", ["rank", "suit"])


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

# random ライブラリよりランダムな要素の取得も行える
print(choice(deck))

# loop による要素の取得も可能に
for card in deck:
	print(card)

# 要素の順の反転も可能
for card in reversed(deck):
	print(card)


# %%
# **************************************************
# ----- End
# **************************************************

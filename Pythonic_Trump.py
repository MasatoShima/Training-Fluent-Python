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


# **************************************************
# ----- Function Main
# **************************************************


# **************************************************
# ----- Process Main
# **************************************************
if __name__ == '__main__':
	pass


# **************************************************
# ----- End
# **************************************************

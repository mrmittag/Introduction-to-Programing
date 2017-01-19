from random import shuffle

suits = ['Clubs','Diamonds','Spades','Hearts']
ranks = ['A','K','Q','J','10','9','8','7','6','5','4','3','2']


deck = []

for suit in suits:
	for rank in ranks:
		deck.append(rank + ' ' +suit)

shuffle(deck)
print(deck)

hand1 = deck.pop() + ' ' + deck.pop()
hand2 = deck.pop() + ' ' + deck.pop()
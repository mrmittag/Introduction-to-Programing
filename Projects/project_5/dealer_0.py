from random import shuffle

suits = ['Clubs','Diamonds','Spades','Hearts']
ranks = ['A','K','Q','J','10','9','8','7','6','5','4','3','2']


deck = []

for suit in suits:
	for rank in ranks:
		deck.append(rank + ' ' +suit)

shuffle(deck)
print(deck)

def count_pairs(hand):
	count=[]
	for card in set(hand):
		count.append(hand.count(card))
	return count	

def pairs(hand):
	set_hand = set(hand)
	number_unique_cards = len(set_hand)
	pairs = count_pairs(hand)

	if number_unique_cards == 2:
		if 4 in pairs:
			return "four of a kind" # four of a kind needs another check
		elif 3 and 2 in pairs: 
			return "full house"

	elif number_unique_cards == 3:
		if 3 in pairs:
			return "trips"
		else:
			return "two pair"
	elif number_unique_cards == 4:
		return "pair"
	else:
		return "no pair"		


hand1 = deck.pop() + ' ' + deck.pop() + ' ' + deck.pop() + ' ' + deck.pop()+ ' ' + deck.pop()

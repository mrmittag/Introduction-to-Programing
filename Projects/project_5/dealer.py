from random import shuffle

#suit = '♥ ♦ ♣ ♠'.split()

def deal(deck,number_in_hand=5):
	hand=""
	for card in range(number_in_hand):
		hand = hand  + deck.pop() + ' '
	return hand 

def count_pairs(hand):
	count=[]
	for card in set(hand)
		count.append(hand.count(card))
	return count	

def pairs(hand):
	set_hand = set(hand)
	number_unique_cards = len(set_hand)
	pairs = count_pairs(hand)

	if number_unique_cards == 2
		if 4 in pairs:
			return "four of a kind" # four of a kind needs another check
		else: 
			return "full house"

	elif number_unique_cards == 3
		if 3 in pairs:
			return "trips" # or trips
		else:
			return "two pair"
	elif number_unique_cards == 4
		return "pair"
	else:
		return "no pair"		





def create_deck():
	deck = []
	suits = ['Clubs','Diamonds','Spades','Hearts']
	ranks = ['A','K','Q','J','10','9','8','7','6','5','4','3','2']
	for suit in suits:
		for rank in ranks:
			deck.append(rank + ' ' +suit)
	shuffle(deck)
	return deck





play=True
new_deck = create_deck()

while play ==True:
	number=input("How many cards would you like? --->")
	if number.isdigit():
		number = int(number)
		if len(new_deck) >=number:
			if number >0:
				print(deal(new_deck,number))
			else:
				print ("good bye!")
				play=False
		else:
			print("sorry outa cards!")
			replay=input("Would you like a new deck of cards? Type 'y' or 'n'")
			if replay =='y':
				new_deck = create_deck()
			else:
				print("bye!")
				play=False
	else:
		print("please enter a positive non decimal number!")
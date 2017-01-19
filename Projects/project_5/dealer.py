from random import shuffle


def deal(deck,number_in_hand=5):
	hand=""
	for card in range(number_in_hand):
		hand = hand  + deck.pop() + ' '
	return hand 


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
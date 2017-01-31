from random import randint
play=True
moves = ["rock","paper","scissors"]

while play ==True:
	user_choice = input("What is your choice: rock, paper or scissor")
	random_number = randint(0,2)
	computer_choice = moves[random_number]
	print(computer_choice)
	print(user_choice)

	if user_choice == "rock":
		if computer_choice == "rock":
			win = False
			tie = True
		elif computer_choice =="scissors":
			win = True
			tie = False
		elif computer_choice =="paper":
			win = False
			tie = False

	elif user_choice == "paper":
		if computer_choice == "paper":
			win = False
			tie = True
		elif computer_choice =="rock":
			win = True
			tie = False
		elif computer_choice =="scissors":
			win = False
			tie = False

	elif user_choice == "scissors":
		if computer_choice == "scissors":
			win = False
			tie = True
		elif computer_choice =="paper":
			win = True
			tie = False
		elif computer_choice =="rock":
			win = False
			tie = False

	print("I chose ",computer_choice)
	print("You chose ", user_choice )


	if win == True:
		print("You won!")

	elif win ==False:
		print("You lost!")

	elif tie ==True:
		print("We tied!")
import random

print("\n\n\n\n\n...Rock...\n\n...Paper...\n\n...Scissors...\n\n")
#		To get user input to be case insensitive...
#		.lower()
#		 what it does is that it converts all upper cases to lower cases.
player = None
while player != "exit":
	player = input("Player choose from rock, paper, or scissors: ").lower()

	#		This is to convert random number from 0 to 2 to convert to a game value of rock, paper, scissors.
	rand_num = random.randint(0,2)
	if rand_num == 0:
		computer = "rock"
	elif rand_num == 1:
		computer = "paper"
	else:
		computer = "scissors"
	#		Line below is to print sensible line while in the game, and f{} is used to as f string to build a sentence with correct data types.
	print(f"Computer plays {computer}")

	if player == computer:
		print("\nIt's a Tie!\n\n\n")
	elif player == "rock":
		if computer == "scissors":
			print("\n You Win!\n\n\n")
		elif computer == "paper":
			print("\nYou Lost!\n\n\n")
	elif player == "paper":
		if computer == "rock":
			print("\nYou Win!\n\n\n")
		elif computer == "scissors":
			print("\nYou Lost!\n\n\n")
	elif player == "scissors":
		if computer == "paper":
			print("\nYou Win!\n\n\n")
		elif computer == "rock":
			print("\nYou Lost!\n\n\n")
	else:
		print("\nSomething went wrong!\n\n\n")
print("Game is finished")
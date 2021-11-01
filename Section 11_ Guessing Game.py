


#	================================================================================================
#	================================================================================================
#	================================================================================================



#	Section 11: Guessing Game


#	93. Guessing Game Mini Project
#	94. Guessing Game Solution
#	95. Improving Rock, Paper, Scissors
#	96. SIDE NOTE: Python Style and PEP8



#	================================================================================================
#	================================================================================================
#	================================================================================================



#	94. Guessing Game Solution



from random import randint
rand_num = randint(1, 10)

while True:
	user = input("Guess the number fron 1 to 10: ")
	user = int(user)
	if user > rand_num:
		print("To high")
	elif user < rand_num:
		print("To low")
	else:
		print("You won")
		user = input("Do you want to play again? (y/n) ")
		if user == "y":
			rand_num = randint(1, 10)
			user = None
		else:
			print("Thank you for playing")
			break



#	================================================================================================
#	================================================================================================
#	================================================================================================



#	95. Improving Rock Paper Scissors



import random
player_wins = 0
computer_wins = 0
winning_score = 3

print("\n\n\n\n\n...Rock...\n\n...Paper...\n\n...Scissors...\n\n")
#		To get user input to be case insensitive...
#		.lower()
#		 what it does is that it converts all upper cases to lower cases.
player = None
while player_wins < winning_score and computer_wins < winning_score:
	player = input("Player choose from rock, paper, or scissors: ").lower()
	if player == "quit" or player == "q":
		break

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
		print(f"\nIt's a Tie! {player_wins}:{computer_wins}\n\n\n")
	elif player == "rock":
		if computer == "scissors":
			player_wins += 1
			print(f"\n You Win! {player_wins}:{computer_wins}\n\n\n")
		elif computer == "paper":
			computer_wins += 1
			print(f"\nYou Lost! {player_wins}:{computer_wins}\n\n\n")
	elif player == "paper":
		if computer == "rock":
			player_wins += 1
			print(f"\nYou Win! {player_wins}:{computer_wins}\n\n\n")
		elif computer == "scissors":
			computer_wins +=1
			print(f"\nYou Lost! {player_wins}:{computer_wins}\n\n\n")
	elif player == "scissors":
		if computer == "paper":
			player_wins += 1
			print(f"\nYou Win! {player_wins}:{computer_wins}\n\n\n")
		elif computer == "rock":
			computer_wins += 1
			print(f"\nYou Lost! {player_wins}:{computer_wins}\n\n\n")
	else:
		print("\nSomething went wrong!\n\n\n")
print("Game is finished")


if player_wins > computer_wins:
	print("You Won the Game!")
elif player_wins == computer_wins:
	print("It's a Tie!")
else:
	print("You Lost the Game!")



#	================================================================================================
#	================================================================================================
#	================================================================================================




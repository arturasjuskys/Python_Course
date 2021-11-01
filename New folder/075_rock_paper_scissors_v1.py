

# Alternative Code

print("\n\n\n\n\n...rock...\n\n...paper...\n\n...scissors...\n\n")
player1 = input("(enter Player 1's choice): ")
print("... No Cheating!!!...\n\n\n" *40)
# *40 --- is to multiply string x40.
player2 = input("(enter Player 2's choice): ")

if player1 == player2:
	print("\nIt's a tie!\n\n\n")
elif player1 == "rock":
	if player2 == "scissors":
		print("\nPlayer 1 Wins!\n\n\n")
	elif player2 == "paper":
		print("\nPlayer 2 Wins!\n\n\n")
elif player1 == "paper":
	if player2 == "rock":
		print("\nPlayer 1 Wins!\n\n\n")
	elif player2 == "scissors":
		print("\nPlayer 2 Wins!\n\n\n")
elif player1 == "scissors":
	if player2 == "paper":
		print("\nPlayer 1 Wins!\n\n\n")
	elif player2 == "rock":
		print("\nPlayer 2 Wins!\n\n\n")
else:
	print("\nSomething went wrong!\n\n\n")



# Alternative Clean Solution

#p1 = input("Player 1: rock, paper, or scissors ")
#p2 = input("Player 2: rock, paper, or scissors ")

#if p1 == p2:
#	print("Draw")
#elif p1 == "rock"and p2 == "scissors":
#	print("p1 wins")
#elif p1 == "paper" and p2 == "rock":
#	print("p1 wins")
#elif p1 == "scissors" and p2 == "paper":
#	print("p1 wins")
#else:
#	print("p2 win")




# Redundant Code



#print("\n\n\n\n\n...rock...\n\n...paper...\n\n...scissors...\n\n")
#player1 = input("(enter Player 1's choice): ")
#player2 = input("(enter Player 2's choice): ")

#if player1 == "rock" and player2 == "scissors":
#	print("Player 1 Wins!")
#elif player1 == "rock" and player2 == "paper":
#	print("Player 2 Wins!")
#elif player1 == "paper" and player2 == "scissors":
#	print("Player 2 Wins!")
#elif player1 == "paper" and payer2 == "rock":
#	print("Player 1 Wins!")
#elif player1 == "scissors" and player2 == "paper":
#	print("Player 1 Wins!")
#elif player1 == "scissors" and Player2 == "rock":
#	print("Player 2 Wins!")
#elif player1 == player2:
#	print("Its a tie!")
#else:
#	print("Something went wrong!")
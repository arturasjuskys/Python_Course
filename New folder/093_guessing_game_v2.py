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
	
	
	
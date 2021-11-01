user = input("Gues the number form 1 to 10\n")
user = int(user)

import random
rand_num = random.randint(1, 10)
computer = rand_num
print(f"computer's guess was {computer}")

if rand_num == user:
	print("You guestted it RIGHT!!!")
elif user > 10:
	print("Your guess is outside of game parameters!!!")
elif user != computer:
	print("Your guess is WRONG!!!")
else:
	print("Something went WRONG!!!")
# With user input

user = input("enter the number from [ 10 - 20] ")
user = int(user)

for number in range(user):
	if number == 4 or number == 13:
		print(f"{number} is unlucky")
	elif number % 2 == 0:
		print(f"{number} is even")
	else:
		print(f"{number} is odd")


# Basic cose

for number in range(1,21):
	if number == 4 or number == 13:
		print(f"{number} + is unlucky")
	elif number % 2 == 0:
		print(f"{number} + is even")
	else:
		print(f"{number} + is odd")
		

# Alternative Code

for number in range(1,21):
	if number == 4 or number == 13:
		state = "unlucky"
	elif number % 2 == 0:
		state = "even"
	else:
		state = "odd"
	print(f"{number} is {state}")
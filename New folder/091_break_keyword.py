# while True:
# 	user = input("Type 'exit' to exit: ")
# 	if (user == "exit"):
		# break

user = input("How many times do I have to tell you? ")
user = int(user)
for user in range(1, user + 1):
# range(1, user + 1) - is needed to start the range from 1 ont 0, and the range to be accurate add 1 to input.
	print("CLEAN UP YOUR ROOM!!!")
	if user >= 4:
		print("do you even listen anymore?")
		break
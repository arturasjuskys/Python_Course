


#	================================================================================================
#	================================================================================================
#	================================================================================================



#	Section 10: Looping in Python


#	81: Section Introduction
#	83. The Basics of For Loops
#	84. Exploring Ranges in Depth
#	86. Exercise: Screaming Repeating
#	87: Exercise: Unlucky Numbers
#	88. Introducing While Loops
#	89. Exercise: Emoji Art
#	90. Exercise: Stop Copying Me
#	91. The Break Keyword



#	Coding Exercise 13: For Loop and Range exercise
#	Coding Exercise 14: While Loop Exercise



#	================================================================================================
#	================================================================================================
#	================================================================================================



#	83. The Basics of For Loop



#	for loops


#for item in iterable_object:
#	do something with item


for number in range(1, 8):
	print(number)
	print(number * 8)



#	================================================================================================
#	================================================================================================
#	================================================================================================



#	84. Exploring Ranges in Depth



r = range(0, 20, 2)
print(list(r))
t = range(20, 0, -2)
print(list(t))



for num in range(0, 20, 2):
	print(num)



#	range(7)	# 0, 1, 2, 3, 4, 5, 6
#	range(1, 8)	# 1, 2, 3, 4, 5, 6, 7
#	range(1, 10, 2)	# 1, 3, 5, 7, 9
#	range(7, 0, -1)	# 7, 6, 5, 4, 3, 2, 1



#	================================================================================================
#	================================================================================================
#	================================================================================================



#	86. Exercise: Screaming Repeating



user = input("How namy times I need tell you? ")
user = int(user)
for user in range(user):
	print(f"TIME {user + 1}: To clean your room!!!")



#	================================================================================================
#	================================================================================================
#	================================================================================================



#	87. Exercise: Unlucky Numbers



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



#	================================================================================================
#	================================================================================================
#	================================================================================================



#	88. Introducing While Loop



user = None
while user != "please":
	user = input("Ah ah ah, you didn't say the magic word: ")



msg = input("whats the secret password? ")
while msg != "bananas":
	print("WRONG!")
	msg = input("whats the secret password? ")
print("CORRECT!")



# For Loop convertion to While Loop



for num in range(1, 11):
	print(num)

#num = 1    #    wariable needs to be set before while loop
#while num < 11:
#	print(num)    #    this will cause infinite loop, because num never changes

num = 1
while num < 11:
	num +=1    #    this is to update num value, and to excape infinite loop (num = num + 1)
	print(num)



#	break



while True:
	command = input("Type 'exit' to exit:")
	if (command == "exit"):
		break



times = int(input("How many times do I have to tell you? "))
for time in range(1, times):
	print("CLEAN UP YOUR ROOM!")
	if time >= 4:
		print("do you even listening me?")
		break



#	================================================================================================
#	================================================================================================
#	================================================================================================



#	90. Emoji Art



# for loop
for num in range(1, 10):
	print(num * "\U0001f600")



# while loop
num = 1
while num < 11:
	print(num * "\U0001f600")
	num += 1



# without string multiplication, replacement for ("\U0001f600" * num)
for num in range(1, 11):
	count = 1
	smileys = ""
	while count < num:
		smileys += "\U0001f600"
		count += 1
	print(smileys)



#	================================================================================================
#	================================================================================================
#	================================================================================================



#	90. Exercise: Stop Copying Me


user = input("Hey how its going? ")
while user != "stop copying me":
	print(user)
	user = input()
print("You win!!!!")

# Alternative code

#user = input("Hey how its going")
#while user != "stop copying me":
#	user = input(f"{user}\n")
#print("You Win!!!")

# Alternative Code

# user = input("How are you? ")
# while user != "stop copying me":
# 	user = input(f"{user}\n")
# print("You win I'll stop now")



#	================================================================================================
#	================================================================================================
#	================================================================================================



#	# while True:
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



#	================================================================================================
#	================================================================================================
#	================================================================================================




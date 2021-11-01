


#	================================================================================================
#	================================================================================================
#	================================================================================================



#	Section 8: Boolean and Conditional Logic



#	60. Section Introduction and Objectives
#	61. Getting User Input
#	62. Intro to Conditionals
#	65. Multiple Elifs
#	66. A Word on Truthiness + A Quick Example
#	67. The Joy of Comparison Operators.
#	68. Logical AND & OR
#	70. LOGICAL NOT
#	71. A Note on Is Vs. ==
#	72. Bouncer Code-Along and Nested Conditionals



#	Coding Exercise 9: Number is Odd
#	Coding Exercise 10: Food Classifying Exercise
#	Coding Exercise 11: Positive or Negative Checking
#	Coding Exercise 12: Calling in Sick



#	================================================================================================
#	================================================================================================
#	================================================================================================



#	61. Getting User Input


name = input("Enter your name here: ")
print("Your name is " + name)



print("Enter your name here:")
name = input()
print("Your name is " + name)



#	================================================================================================
#	================================================================================================
#	================================================================================================



#	62. Intro to Conditionals


user = input("Arya Sark, Valar Morgulis, John Snow, other: ")
if name == "Arya Stark":
	print("Valar Morghulis")
elif name == "John Snow":
	print("You know nothing")
else:
	print("Carry on")



#	================================================================================================
#	================================================================================================
#	================================================================================================



#	Coding Exercise 8: Lucky Number 7



from random import randint
choice = randint(1,10)
if choice == 7:
    print("lucky")
else:
    print("unlucky")



#	================================================================================================
#	================================================================================================
#	================================================================================================



#	Coding Exercise 9: Number is Odd



from random import randint
num = randint(1, 1000)
if num % 2 == 0:
    print("even")
else:
    print("odd")



#	================================================================================================
#	================================================================================================
#	================================================================================================



#	66. A Wrod on Truthiness + A quick Example


x = 1
x is 1	# True
x is 0	# False



#	Naturaly False things:
#	Empty Objects
#	Empty Strings
#	None
#	Zero



if 0:
	print("Yay!")
#				<<<===	nothing prints because if statment is false
if 1:
	print("Yay?")
# Yay?	<<<===	if statment is True and thats why it prints this time



animal = input("enter your favorite animal ")
if animal:
	print(animal + " is my favorite too!")
else:	#	<<<===	this else statment executes if no input is provided, because if statment above checks if anything is passed in
	print("You didnt say anything!")
	


#	================================================================================================
#	================================================================================================
#	================================================================================================



#	67. The Joy of Comparison Operators



#	a = 1, b = 1
#	==	 a == b	# True,	Truthy if a has the same value as b
#	!=	  a != b	# False,	Truthy is a does NOT have the same value as a
#	>	   a > b	# False,	Truthy if a is greater than a
#	<	   a < b	# False,	Truthy if a is less than b
#	>= 	a >= b	# True,	Truthy if a is greater than or equal to b
#	<=	 a <= b	# True,	Truthy if a is less than or equal to b



#	================================================================================================
#	================================================================================================
#	================================================================================================



#	68. Logical AND & OR



#if a and b:
#	print(c)
#	Truthy if both a AND b are true (logical conjunction)

#if am_tired or is_bedtime:
#	print("go to sleep")
#	Truthy if either a OR b are true (logical disjunction)

#if not is_weekend:
#	print("go to work")
#	Truthy if the opposite of a is true (logical negative)



#	================================================================================================
#	================================================================================================
#	================================================================================================



#	71. A Note on is Vs. ==


a = 1
a == 1
a == 1	# True
a is 1	# True



a = [1, 2, 3]	# a list of numbers
b = [1, 2, 3]
a == b	# True
a is b	# False
c = b
b is c	# True, because c is set to be the same as b, meaning refering to the same data in comupter memory
#	is	checking computer memory, if both values are refering to the same data on the memory
#	==	checking values, if they are the same, it dont care for memory equality



#	================================================================================================
#	================================================================================================
#	================================================================================================



#	72. Bouncer Code-Along and Nested Conditionals



# ask of age
age = input("How old are you: ")
# this line checkes for empty values, not to return error
if age != "":
	if int(age) >= 18 and int(age) < 21: # int() is required to convert data type to integer form string.
		# 18-21 wristband
		print("You can enter but you need a wristnand!")
	elif int(age) >= 21:
		# 21+ drink, normal entry
		print("You are good to enter and you can drink!")
	else:
		# too young, sorry
		print("You can't come in, little one! :(")
else:
	print("Please enter you age")




# Alternative code

age = input("How old are you: ")
if age:
	age = int(age)
	if age >=18 and age < 21:
		print("You can enter, but need a wristband!")
	elif age >= 21:
		print("You are good to enter and can drink!")
	else:
		print("You can't come in, little one! :(")
else:
	print("Please enter an age!")




# Alternative code

age = input("How old are your: ")
if age:
	age = int(age)
	if age >= 21:
		print("You are good to neter and can drink!")
	elif age >=18:
		print("You can enter, but need a wristband!")
	else:
		print("You can't come in, little one! :(")
else:
	print("Please enter an age!")



#	================================================================================================
#	================================================================================================
#	================================================================================================



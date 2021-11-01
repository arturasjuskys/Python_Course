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

#age = input("How old are you: ")
#if age:
# 	age = int(age)
# 	if age >=18 and age < 21:
# 		print("You can enter, but need a wristband!")
#	elif age >= 21:
#		print("You are good to enter and can drink!")
#	else:
#		print("You can't come in, little one! :(")
#else:
#	print("Please enter an age!")




# Alternative code

#age = input("How old are your: ")
#if age:
#	age - int(age)
#	if age >= 21:
#		print("You are good to neter and can drink!")
#	elif age >=18:
#		print("You can enter, but need a wristband!")
#	else:
#		print("You can't come in, little one! :(")
#else:
#	print("Please enter an age!")
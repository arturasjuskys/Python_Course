


#	================================================================================================
#	================================================================================================
#	================================================================================================



#				Section 7: Variables and Strings



#	41. Variables and Data Types
#	42. Introduction to Variables
#	44. Variable Naming Restrictions and Conventions
#	45. Data Types Overview
#	46. What The Heck is Dynamic Typing
#	47. The Special Value NONE
#	48. Double vs Single Quotes
#	50. String Escape Sequence
#	52. String Concatenation
#	54. String Formating
#	55. IMPORTANT: Interpolation w/ Udemy Exercises
#	57. Strings and Indexes (Indicies?)
#	58. Converting Data Types
#	59. Building a Mileage Converter with User Input



#	Coding Exercise 3: Bank Robbery Money
#	Coding Exercise 4: Make Some Variables
#	Coding Exercise 5: Escape Sequence Practice
#	Coding Exercise 6: String Concatenation Exercise
#	Coding Exercise 7: Formatting Strings



#	================================================================================================
#	================================================================================================
#	================================================================================================



#	42. Introduction to Variables



x = 100
khaleesi_mother_of_dragons = 1
print(khaleesi_mother_of_dragons + x)
#	101



all, at, once = 5, 10, 15
print(all, at, once)



#	================================================================================================
#	================================================================================================
#	================================================================================================



#	45. Data Types Overview


#	bool    True or False values
#	int     an integer (1, 2, 3)
#	str     (string) a sequance of Unicode characters, e.g. "Colt" or "f89sdgf8sd9f"
#	list    an ordered sequence of values of other data types, e.g. [1, 2 ,3] or ['a', 'b', 'c']
#	dict    a collection of key: values, e.g. {'first_name': 'Colt', 'last_name': 'Steele'}

#	Among other...



#	================================================================================================
#	================================================================================================
#	================================================================================================



#	46. What The Heck is Dynamic Typing



awesomeness = True
print(awesomeness)
# True

awesomeness = "a dog"
print(awesomeness)
# a dog

awesomeness = 22 / 7
print(awesomeness)
# 3.142857142857143



#	================================================================================================
#	================================================================================================
#	================================================================================================



#	48. Double vs Single Quotes



#	msg = "he said " "hello!""	#	SyntaxError: invalid syntax

msg1 = "he said 'hello!'"
msg2 = 'I am "funny"'



#	================================================================================================
#	================================================================================================
#	================================================================================================



#	50. String Escape Sequences



#	\n    new line
#	\\    backslash (\)
#	\'    Single qoute (')
#	\"    Double qoute (")



new_line = "hello \n world"
print(new_line)
# hello
#  world



#	================================================================================================
#	================================================================================================
#	================================================================================================



#	String Concatination



#	Concatination is combining multiple strings together.



str_one = "your"
str_two = "face"
str_three = str_one + " " + str_two
print(str_three)
# your face



str_one = "ice"
str_one += " cream"    #    <<<===    += works as an update operator, and helps to avoid longer syntax above
print(str_one)
# ice cream



#	================================================================================================
#	================================================================================================
#	================================================================================================



#	54. String Formating



#	F-Strings
x = 10
formatted1 = f"I've told you {x} times already!"
print(formatted1)



#	.format method
x = 10
formatted2 = "I've told you {} times already!".format(10)
print(formatted2)



first = "a"
last = "j"
formatted = "First Name: {}, Last Name: {}".format(first, last)



#	================================================================================================
#	================================================================================================
#	================================================================================================



#	57. Strings and Indexes (indecies?)



name = "Chuck"
name[0]    # 'C'
name[1]    # 'h'
name[-1]   # 'k'
name[-2]   # 'c'
#name[5]    # IndexError: string index out of range



#	================================================================================================
#	================================================================================================
#	================================================================================================



#	58. Converting Data Types



decimal = 12.56345634534
integer = int(decimal)
print(integer)
# 12



my_list = [1, 2, 3]
my_list_as_a_string = str(my_list)
print(my_list_as_a_string)
# "[1, 2, 3]"



#	================================================================================================
#	================================================================================================
#	================================================================================================



#	59. Mileage Converter With User Input



print("How many kilometers did you cycle today?")
km = input()
miles = float(km)/1.60934
miles = round(miles, 2)
print(f"Your {km}km ride was {miles}mi")



print("How many kilometers did you cycle today?")
km = input()
miles = float(km)/1.60934
print(f"Your {km}km ride was {round(miles, 2)}mi")



print("How many kilometers did you cycle today?")
km = input()
miles = round(float(km)/1.60934, 2)
print(f"Your {km}km ride was {round(miles, 2)}mi")







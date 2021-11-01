


#	================================================================================================
#	================================================================================================
#	================================================================================================



#	Section 21: Debugging and Error Handling



#	207. Section Introduction
#	208. Common Types of Errors in Python
#	209. Raising Our Own Errors
#	210. Try and Except Blocks
#	211. Try, Except, Else, and Finally!
#	212. Debugging With PDB



#	Coding Exercise 72: Debugging and Error Handling Exercises



#	================================================================================================
#	================================================================================================
#	================================================================================================



#	208. Common Types of Errors in Python



#	SyntaxError
		#	typos
#	NameError
		#	when variables are not defined
#	TypeError
		#	miss mach of data typres
#	IndexError
		#	out of range
#	ValueError
		#	int("foo")
		#	ValueError: invalid literal for int() with base 10: 'foo'
#	KeyError
		#	d = {}
		#	d['foo']
		#	KeyError: 'foo'
#	AttributeError
		#	This occurs when a variable does not have an attreibute:
			#	"awesome".foo
			#	AttributeError: 'str' object has no attribute 'foo'
#	And More ...



#	================================================================================================
#	================================================================================================
#	================================================================================================



#	209. Raising Our Own Errors



#	In python we can also throw errors using the raise keyword. This is helpful when creating your own kindss of exceptions and error messages.



#	raise ValueError("invalid value")



#def colorize(text, color):
#	colors = ("cyan", "yellow", "blue", "green", "magenta")
#	if type(color) is not str:
#		raise TypeError("color must be instance of str")
#	if type(text) is not str:
#		raise TypeError("text must be instance of str")
#	if color not in colors:
#		raise ValueError("color is invalid color")
#	print(f"Printed {text} in {color}")
#
#colorize("hello", "red")
#colorize(34, "red")



#	================================================================================================
#	================================================================================================
#	================================================================================================



#	210. Try and Except Blocks



#	In Python, it is STRONGLY enauraged to use try/except blocks, to catch exceptions when we can do something about them.



try:
	foobar
except NameError as err:
	print("PROBLEM!")
print("after the try")



#	What we are doing is catching EVERY error, which means we are not albe to correcly identify "what" went wrong. It is highly discouraged to do this.



try:
	colt
except:
	print("You tried to use a variable that was never declared!")



try:
	colt
except NameError:    #    <<<===    this defines what type of error to chatch
	print("You tried to use a variable that was never declared!")



def get(d, key):
	try:
		return d[key]
	except KeyError:
		return None
d = {"name": "Ricky"}
print(get(d, "name"))
print(get(d, "city"))    #    <<<===    'city' does not exist in given dictionary, and thus we overiden original Error Message with our 'None'



#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n___   ___   ___   211. Try, Except, Else, and Finally!   ___   ___   ___\n")



#	211. Try, Except, Else, and Finally!



try:
	num = int(input("please enter a number: "))
except:    #    <<<===    this will run if there is a problem
	print("That's not a number!")
else:    #    <<<===    this will run if there is no problem
	print("I'm in the else")
finally:    #    <<<===    this will run no matter what
	print("Runs no matter what")


while True:
	try:
		num = int(input("please enter a number: "))
	except ValueError:    #    <<<===    this will run if there is a problem
		print("That's not a number!")
	else:    #    <<<===    this will run if there is no problem
		print("Good job, you entered a number!")
		break
	finally:    #    <<<===    this will run no matter what
		print("Runs no matter what")



def divide(a, b):
	try:
		result = a / b
	except ZeroDivisionError:
		print("don't divide by zero please!")
	except TypeError as err:
		print("a and b must be  ints or floats")
		print(err)
	else:
		print(f"{a} divided by {b} is {result}")
divide(1, 2)
# 1 divided by 2 is 0.5
divide(1, 0)
# don't divide by zero
divide("a", 2)
# a and b must be ints or floats
# unsupported operand type(s) for /: 'str' and 'int'
divide("b", 0)
# a and b must be ints or floats
# unsupported operand type(s) for /: 'str' and 'int'



def divide2(a, b):
	try:
		result = a / b
	except (ZeroDivisionError, TypeError) as err:
		print("Something went wrong!")
		print(err)
	else:
		print(f"{a} devided by {b} is {result}")



#	================================================================================================
#	================================================================================================
#	================================================================================================



#	212. Debugging With PDB



#	import pdb; pdb.set__trace()



import pdb

first = "First"
second = "Second"
pdb.set_trace()
result = first + second
third = "Third"
result += third
print(result)



#		import pdb
#		pdb.set_trace()

#		Also commonly on one line:
#		import pdb; pdb.set_trace()

#		Common PDB Commands:
#		l    (list)
#		n   (next line)
#		p   (print)
#		c   (continue - finishes debugging)



def add_numbers(a, b, c, d):
	import pdb; pdb.set_trace()
	print( a + b + c + d)
	add_numbers(3, 2, 1, 0)



#	================================================================================================
#	================================================================================================
#	================================================================================================



#	Coding Exercise 72: Debugging and Error Handling Exercises



    
# divide(4,2)  2
# divide([],"1")  "Please provide two integers or floats"
# divide(1,0)  "Please do not divide by zero"

def divide(num1, num2):
	try:
		answer = num1 // num2
	except TypeError:
		return "Please provide two integers or floats"
	except ZeroDivisionError:
		return "Please do not divide by zero"
	else:
		return answer







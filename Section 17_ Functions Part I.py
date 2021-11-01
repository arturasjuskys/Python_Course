


#	================================================================================================
#	================================================================================================
#	================================================================================================



#	145. Introduction to Defining Functions
#	146. Defining Functions
#	148. The Magical Return Keyword
#	149. Writing a coin_flip Function Using Random
#	152. Parameters
#	154. Common Mistakes When Returning
#	156. Default parameters
#	158. Keyword Arguments
#	160. Docstrings and Functions Recap - WE DID IT!



#	Coding Exercise 37: Your First Function
#	Coding Exercise 38: Super Quick Return Exercise
#	Coding Exercise 39: Generating Evens Exercise
#	Coding Exercise 40: Yell Function Exercise
#	Coding Exercise 41: Fix This Function!
#	Coding Exercise 42: Default Parameter Exercise - Talking Animals



#	================================================================================================
#	================================================================================================
#	================================================================================================



#	145. Introduction to Defining Functions



#    A process of executing a task
#    it can accept input and return an output
#    Useful for executing similar procedures over and over

#        .clear()
#        .copy()
#        print()
#        ...
#        these are just couple of examples of functions



#    Function Struction

# def name_of_function ():
	# block of runnable code



#	================================================================================================
#	================================================================================================
#	================================================================================================



#	146. Defining Functions



def say_hi():
	print("Hi!")
say_hi()
# Hi!



def sing_happy_birthday():
	print("Happy Birthday To You")
	print("Happy Birthday To You")
	print("Happy Birthday Dear You")
	print("Happy Birthday To You")
sing_happy_birthday()



#	================================================================================================
#	================================================================================================
#	================================================================================================



#	148. Magical Return Keyword



def square_of_7():
	print("I AM BEFORE RETURN")
	return 7 ** 2
	print("I AM AFTER RETURN")
result = square_of_7()
print(result)
# I AM BEFORE RETURN
# 49



#	================================================================================================
#	================================================================================================
#	================================================================================================



#	149. Writing a coin_flip Function Using Random



def flip_coin():
	from random import random
	r = random()
	print(r)
	if r > 0.5:
		return "Heads"
	else:
		return "Tails"
print(flip_coin())



def flip_coin():
	from random import random
	if random() > 0.5:
		return "Heads"
	else:
		return "Tails"
print(flip_coin())



#	================================================================================================
#	================================================================================================
#	================================================================================================



#	152. Parameters



def square(number):
	return number * number
print(square(4))
# 16
print(square(8))
# 64



def sing_happy_birthday(name):
	print("Happy Birthday To You")
	print("Happy Birthday To You")
	print(f"Happy Birthday Dear {name}")
	print("Happy Birthday To You")
sing_happy_birthday("Colt")



def add(a, b):
	return a + b
	


def multiply(first, second):
	return first * second
print(multiply(4, 8))
# 32



def print_full_name(first_name, last_name):
	return(f"Your full name is {first_name} {last_name}")
print(print_full_name("A", "J"))
# Your full name is A J



#    Parameters vs Arguments

#    A PARAMETER is a variable in a method definition.
#    When a method is called, the ARGUMENTS are the dasta you pass into the method's PARAMETERS.
#    PARAMETER is variable in the declaration of function.
#    ARGUMENT is the actual value of this variable that gets passed to function.



#	================================================================================================
#	================================================================================================
#	================================================================================================



#	154. Common Mistakes When Returning



def sum_odd_numbers(numbers):
	total = 0
	for num in numbers:
		if num % 2 != 0:
			total += num
		return total    #    indentation in this line is in the wrong place, in this instance return breaks the loop before secong atempt is initiated causing to return answer of 1 not if 16.
print(sum_odd_numbers([1, 2, 3, 4, 5, 6, 7]))
# 1 + 3 + 5 + 7 = 16    this is sort of answer we are expecting out of this function
def sum_odd_numbers(numbers):
	total = 0
	for num in numbers:
		if num % 2 != 0:
			total += num
	return total
print(sum_odd_numbers([1, 2, 3, 4, 5, 6, 7]))
# 16		



#    This function is correct but just contains one unnecessary line of code    else:
def is_odd_number(number):
	if number % 2 != 0:
		return True
	else:
		return False
print(is_odd_number(4))
# False
print(is_odd_number(9))
# True
#    This time the code stays almost the same, just else: statment is removed because the code will still return the same values
def is_odd_number(number):
	if number % 2 != 0:
		return True
	return False
print(is_odd_number(4))
# False
print(is_odd_number(9))
# True



#	================================================================================================
#	================================================================================================
#	================================================================================================



#	156. Default Parameters



#    Allows you to be more defensive
#    Avoids erros with incorrect parameters
#    More readable examples!
#    Anything can be a default parameter. Functions, list, dictionaries, strings, booleans - all of the above!



#    in the 1st line in the brackets we have 2nd parameter set  to power = 2, this means if there is no parameter given this will be a default value , in case a value is given it will override default value.
def exponent(num, power = 2):
	return num ** power
print(exponent(2, 3))
# 8
print(exponent(5))
# 25
print(exponent(4))
# 16



def add(a, b):
	return a + b
print(add(1, 3))
# 4

def add(a = 10, b = 20):
	return a + b
print(add())
# 30
print(add(1, 10))
# 11



def show_information(first_name = "Colt", is_instructor = False):
	if first_name == "Colt" and is_instructor:
		return "Welcome back instructor COlt"
	elif first_name == "Colt":
		return "I really thought you were an instructor..."
	return f"Hello {first_name}!"
show_information()    # "I really thought you were an instructor..."
show_information(is_instructor = True)    # "Welcome back instructor Colt!"
show_information('Molly')    # Hello Molly!



def add(a, b):
	return a + b
	
def math(a, b, fn = add):    #    <==    default function.    fn    means function and it equals to add function defined above. Best practice is to add default function at the back so it woulnt mess up the function, or set all possible input parameters to default values, in this case you will avoid errors.
	return fn(a, b)

def subtract(a, b):
	return a - b

print(math(2, 4))    # 6    defaults to    fn = add
print(math(2, 2, subtract))    # 0



#	================================================================================================
#	================================================================================================
#	================================================================================================



#	Coding Exercise 42: Default Parameter Exercise - Talking Animals



def speak(animal="dog"):
    if animal == "pig":
        return "oink"
    elif animal == "duck":
         return "quack"
    elif animal == "cat":
        return "meow"
    elif animal == "dog":
        return "woof"
    else:
        return "?"



#	Alternative solution with dictionary



def speak(animal="dog"):
    noises = {
    "dog": "woof",
    "pig": "oink",
    "duck": "quack",
    "cat": "meow"
    }
    noise = noises.get(animal)
    if noise:
        return noise
    return "?"



def speak(animal='dog'):
    noises = {
    'pig':'oink',
    'duck':'quack',
    'cat':'meow',
    'dog':'woof'
    }
    return noises.get(animal, '?')



#	================================================================================================
#	================================================================================================
#	================================================================================================



#	158. Keyword Argument



#	Makes code more readable and flexible

def full_name(first, last):
	return f"Your name is {first} {last}"
print(full_name(first = 'Colt', last = 'Steele'))	# Your name is Colt Steele
print(full_name(last = 'Steele', first = 'Colt'))	# Your name is Colt Steele



def full_name(first = 'Colt', last = 'Steele'):
	return f"Your name is {first} {last}"
print(full_name())                                         # Your name is Colt Steele
print(full_name(last = 'Enthusiast', first = 'Python'))    # Your name is Python Enthusiast



#	================================================================================================
#	================================================================================================
#	================================================================================================



#	159. Scope



#    Where our variables can be accessed!
#    Variables created in functions are scoped in that function!



#    in this example {instructor} is defined in global scope, because it's outside this function'
instructor = 'Colt'
def say_hello():
	return f"Hello {instructor}"
print(say_hello())
# Hello Colt



# in this example {instructor} is defined in functions scope, because it's nested inside say_hello()
def say_hello():
	instructor = 'Colt'
	return f"Hello {instructor}"
print(say_hello())
# Hello Colt
print(instructor)    # NameError



#    global and nonlocal



#     in this axample total is defined in global scope and it doesnt work in this code example, because function is tying to use local variable which doesnt exist in this example.
#	This is to manipulate variables, but if you are just trying to access them you don't need to user that global scope.
#total = 0
def increment():
	total = 0
	total += 1
	return total
print(increment())	# UnboundLocalError: local variablde 'total' referenced before assignment



#    this is how you reference global variable
total = 0
def increment():
	global total	#	<<<<====
	total += 1
	return total
print(increment())



#    Lets us modify a perent's variable in a child (aka nested) function

def outer():
	count = 0
	def inner():
		nonlocal count	#	<<<<====
		count += 1
		return count
	return inner()
print(outer())
# 1



#	================================================================================================
#	================================================================================================
#	================================================================================================



#	160. Docstrings and Function Recap - WE DID IT!



#    Documenting functions
#    Use """ """	triple double quotes
#    .__doc__	works with a lot of functions such ass:
#		.pop()
#		.randint
#		and more...



def say_hello():
	"""A simple function that returns the string hello"""
	return "Hello!"
say_hello.__doc__	# 'A simple function that returns the string hello'	<<<<====	to access it you need to use .__doc__	dot and double underscores.
print(say_hello.__doc__)



#	================================================================================================
#	================================================================================================
#	================================================================================================



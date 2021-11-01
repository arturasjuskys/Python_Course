

#---------------------------------------------------------------------
#---------------------------------------------------------------------
#---------------------------------------------------------------------









#    Section 17: Functions, Part 1









#    What is a Function?



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



def say_hi():
	print("Hi!")
print(say_hi())
# Hi!



def square_of_7():
	print("I AM BEFORE RETURN")
	return 7 ** 2
	print("I AM AFTER RETURN")
result = square_of_7()
print(result)
# I AM BEFORE RETURN
# 49



def add(a, b):
	return a + b
	


def multiply(first, second):
	return first * second
print(multiply(4, 8))
# 32



def square(number):
	return number * number
print(square(4))
# 16
print(square(8))
# 64



def print_full_name(first_name, last_name):
	return(f"Your full name is {first_name} {last_name}")
print(print_full_name("A", "J"))
# Your full name is A J










#    Parameters vs Arguments




#    A PARAMETER is a variable in a method definition.
#    When a method is called, the ARGUMENTS are the dasta you pass into the method's PARAMETERS.
#    PARAMETER is variable in the declaration of function.
#    ARGUMENT is the actual value of this variable that gets passed to function.



#    Common Return Mistakes



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

print(is_odd_number(9))










#    Default Parameters



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
#    does not work

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










#    Keyword Arguments










#    Makes code more readable and flexible



def full_name(first, last):
	return f"Your name is {first} {last}"
print(full_name(first = 'Colt', last = 'Steele'))
# Your name is Colt Steele
print(full_name(last = 'Steele', first = 'Colt'))
# Your name is Colt Steele



def full_name(first = 'Colt', last = 'Steele'):
	return f"Your name is {first} {last}"
print(full_name())
# Your name is Colt Steele
print(full_name(last = 'Enthusiast', first = 'Python'))
# Your name is Python Enthusiast










#    Scope










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



#---------------------------------------------------------------------
#---------------------------------------------------------------------
#---------------------------------------------------------------------










#	Functions Part II










#	*args



#	* this special argument gathers remaining arguments and puts them in tuple







def sum_of_all_numbers(*args):	#	<<<===	this *args is a convention, this could be anything after *...	such as *numbers, *nums, *vals...
	print(args)
	total = 0
	for val in args:
		total += val
	return total

print(sum_of_all_numbers(1, 2, 3))



def ensure_correct_info(*args):
	if "Colt" in args and "Steele" in args:
		return "Welcome back Colt!"
	return "Not sure who you are..."
	
print(ensure_correct_info())
# Not sure who you are...
print(ensure_correct_info(1, True, "Steele", "Colt"))
# Welcome back Colt!










#	**kwargs				keyword args



#	gathers remaining keyword arguments and puts them in dictionary
#	**kwargs	is a convention, you can call it whatever you want, **extras, **...







def fav_colors(**kwargs):
	print(kwargs)
	for person, color in kwargs.items():
		print(f"{person}'s favorite color is {color}")
fav_colors(colt = "purple", ruby = "red", ethal = "teal")



def special_greeting(**kwargs):
	if "David" in kwargs and kwargs["David"] == "special":
		return "You get a spacial greeting David!"
	elif "David" in kwargs:
		return f"{kwargs ['David']} David!"
	return "Not sure who this is..."

print(special_greeting(David = 'Hello'))
# Hello David!
print(special_greeting(Bob = 'hello'))
# Not sure who this is...
print(special_greeting(David = 'special'))
# You get a special greeting David!



def combine_words(word, **kwargs):
	"""
	combine_words("child")  #'child'
	combine_words("child", prefix="man")  #'manchild'
	combine_words("child", suffix="ish")  #'childish'
	combine_words("work", suffix="er")  #'worker'
	combine_words("work", prefix="home")  #'homework'
	"""
	if "prefix" in kwargs:
		return kwargs["prefix"] + word
	elif "suffix" in kwargs:
		return word + kwargs["suffix"]
	else:
		return word

print(combine_words("child"))
print(combine_words("child", prefix = "man"))
print(combine_words("child", suffix = "ish"))
print(combine_words("work", suffix = "er"))
print(combine_words("work", prefix = "home"))










#	Parameter Ordering



#	1. parameters
#	2. *args
#	3. default parameters
#	4. **kwargs



def display_info(a, b, *args, instructor = "Colt", **kwargs):
	return [a, b, args, instructor, kwargs]
print(display_info(1, 2, 3, last_name = "Steele", job = "Instructor"))
# a - 1
# b - 2
# args - 3	<<<===	tuple	(3,)	<<<=== comma is there to distingish this form parentases.
# instructor - "Colt"
# kwargs - {'last_name': "Steele", "job": "Instructor"}	<<<===	dictionaries

# [1, 2, (3,), 'Colt', {'last_name': 'Steele', 'job': 'Instructor'}]










#	Tumple and lists unpacking










def sum_all_values(*args):
	print(args)
	# ([1, 2, 3, 4, 5, 6],)	#	<<<===
	total = 0
	for num in args:
		total += num
	print(total)
nums = [1, 2, 3, 4, 5, 6]
sum_all_values(nums)	#	<<<===	nums as a list passed to args becomes as a tuple with one value, example above
# ([1, 2, 3, 4, 5, 6],)

#	To medeate this problem we need to use *

def sum_all_values(*args):
	print(args)
	# (1, 2 ,3 ,4 ,5 ,6)
	total = 0
	for num in args:
		total += num
	print(total)
nums1= (1, 2, 3, 4, 5, 6)
nums2 = [1, 2, 3, 4, 5, 6]
sum_all_values(*nums1)	#	<<<===	this is how you resolve this with *...
sum_all_values(*nums2)
# (1, 2, 3, 4, 5, 6)
# 21
# (1, 2, 3, 4, 5, 6)
# 21



def count_sevens(*args):
	"""
	This function is to ilustrate how *args unpacks a predefined list
	"""
    return args.count(7)
 
nums = [90,1,35,67,89,20,3,1,2,3,4,5,6,9,34,46,57,68,79,12,23,34,55,1,90,54,34,76,8,23,34,45,56,67,78,12,23,34,45,56,67,768,23,4,5,6,7,8,9,12,34,14,15,16,17,11,7,11,8,4,6,2,5,8,7,10,12,13,14,15,7,8,7,7,345,23,34,45,56,67,1,7,3,6,7,2,3,4,5,6,7,8,9,8,7,6,5,4,2,1,2,3,4,5,6,7,8,9,0,9,8,7,8,7,6,5,4,3,2,1,7]

result1 = count_sevens(1, 4, 7)    #    <<<===    in this example it counts just one instance of 7 given in parameters
print(result1)
# 1
result2 = count_sevens(*nums)    #    <<<===    here *args unpackes predefined list and finds 14 instances of 7
print(result2)
# 14










#	Unpacking Dictionaries










def display_names(first, second):
	return f"{first} says hello to {second}"
names = {"first": "Colt", "second": "Rusty"}
print(display_names(**names))
#	Colt says hello to Rusty



def add_and_multiply_numbers(a, b, c):
	print(a + b * c)
data = dict(a = 1, b = 2, c = 3)
add_and_multiply_numbers(**data)
#	2 * 3 = 6 + 1 = 7
# 7
add_and_multiply_numbers(4, 5, 6)
#	5 * 6 = 30 + 4 = 34
# 34



def add_and_multiply_numbers(a, b, c, **kwargs):
	print(a + b * c)
	print("Other Stuff...")
	print(kwargs)
data = dict(a = 1, b = 2, c = 3, d = 55, name = "Tony")
add_and_multiply_numbers(**data)
# 7
# Other Stuff...
# {'d': 55, 'name': 'Tony'}



def add_and_multiply_numbers(a, b, c, **kwargs):
	print(a + b * c)
	print("Other Stuff...")
	print(kwargs)
data = dict(a = 1, b = 2, c = 3, d = 55, name = "Tony")
add_and_multiply_numbers(**data, cat = "blue")
# 7
# Other Stuff...
# {'d': 55, 'name': 'Tony', 'cat': 'blue'}
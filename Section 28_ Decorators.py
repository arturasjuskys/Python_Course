


#	================================================================================================
#	================================================================================================
#	================================================================================================



#	Section 28: Decotators



#	279. Higher Order Functions
#	280. Introduction to Decorators
#	281. Decorators With Different Signatures
#	282. Using Wraps To Preserve Metadata
#	283. Building A Speed-Test Decorator
#	285. Another Example: Ensuring Args With A Decorator
#	290. Writing an ensure_first_arg_is Decorator
#	291. Enforcing Argument Types With A Decorator



#	Coding Exercise 89: show_args
#	Coding Exercise 90: double_return
#	Coding Exercise 91: ensure_fewer_than_three_args
#	Coding Exercise 92: only_ints
#	Coding Exercise 93: ensure_authorized
#	Coding Exercise 94: delay



#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n___   ___   ___   279. Higher Order Functions   ___   ___   ___\n")



#	279. Higher Order Functions



#	We can pass functions as args to other functions
def sum2(num, fn):
	total = 0
	for num in range(1, num + 1):
		total += fn(num)
	return total
def square(x):
	return x * x
def cube(x):
	return  x**3
print(sum2(3, square))
# 14
print(sum2(3, cube))
# 36



#	We can nest functions inside one another
from random import choice
def greet(person):
	def get_mood():
		msg = choice(('Hello there ', 'Go away ', 'I love you '))
		return msg
	result = get_mood() + person
	return result
print(greet("Toby"))



#	We can creatre a function that returns function
def make_laugh_fn():
	def get_laugh():
		l = choice(('HAHAHAH', 'lol', 'tehehe'))
		return l
	return get_laugh
laugh = make_laugh_fn()
print(laugh())



#	Inner function takes parameter from outer function {person}
def make_laugh_at_fn(person):
	def get_laugh():
		laugh = choice(('HAHAHAH', 'lol', 'tehehe'))
		return f"{laugh} {person}"
	return get_laugh
laugh_at = make_laugh_at_fn("Linda")
print(laugh_at())
print(laugh_at())
print(laugh_at())
print(laugh_at())



#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n___   ___   ___   280. Introduction to Decorators   ___   ___   ___\n")



#	280. Introduction to Decorators



#	Decorators are functions
#	Decorators wrap other functions and enhance their behavior
#	Decorators are examples of higher order funstions
#	Decorators have their own syntax, using "@" (syntactic sugar)



#	Decorators as Functions
#	This example wrapps greet() around with by_polite() and then stores all that to variable 'greet'
def be_polite(fn):
	def wrapper():
		print("What a pleasure to meat you!")
		fn()
		print("Have a great day!")
	return wrapper
def greet():
	print("My name is Colt.")
greet = be_polite(greet)
greet()
# What a pleasure to meat you!
# My name is Colt!
# Have a great day!



#	Decorator Syntax
def be_polite(fn):
	def wrapper():
		print("What a pleasure to meet you!")
		fn()
		print("Have a great day!")
	return wrapper
@be_polite
def greet():
	print("My name is Matt.")
greet()
# What a pleasure to meat you!
# My name is Colt!
# Have a great day!



#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n___   ___   ___   281. Decorators With Different Signatures   ___   ___   ___\n")



#	281. Decorators With Different Signatures



#	Functions with Different Signiture
def shout(fn):
	def wrapper(*args, **kwargs):    #    <<<===    +    <<<===    wrapper is a convension just because it wrapps around another function
		return fn(*args, **kwargs).upper()    #    <<<===
	return wrapper
@shout
def greet(name):
	return f"Hi, I'm {name}."
@shout
def order(main, side):
	return f"Hi, I'd like the {main}, with a side of {side}, please."
@shout
def lol():
	return "lol"
print(greet("todd"))
# HI, I'M TODD'
print(order("burger", "chips"))    #    <<<===    for this to work we need to set shout(fn) wrapper() to take multiple arguments
# HI, L'D LIKE THE BURGER, WITH SIDE OF CHIPS, PLEASE.'
print(lol())
# LOL


#	Decorator Pattern
def my_decorator(fn):
	def wrapper(*args, **kwargs):
		# do some stuff with fn(*args, **kwargs)
		pass
	return wrapper



#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n___   ___   ___   282. Using Wraps To Preserve Metadata   ___   ___   ___\n")



#	282. Using Wraps To Preserve Metadata



#	Preserving Metadata
def log_function_data(fn):
	def wrapper(*args, **kwargs):
		"""I am wrapper function"""
		print(f"you are about to call {fn.__name__}")
		print(f"Here's the documentation: {fn.__doc__}")
		return fn(*args, **kwargs)
	return wrapper
@log_function_data
def add(x, y):
	"""Adds two numbers together"""
	return x + y

print(add(10, 30))
# you are about to call add
# Here's the documentation: Adds two numbers together
# 40

		#	If youll try to print add() docs you will get wrapper() docs instead
print(add.__doc__)
print(add.__name__)
help(add)
# I am wrapper function
# wrapper



#	This is to prevent from loosing metadata such as documentation from example above
from functools import wraps
#	wraps preserves a functions metadata when it is decorated
def my_decorator(fn):
	@wraps(fn)
	def wrapper(*args, **kwargs):
		#	do some stuff with fn(*args, **kwargs)
		pass
	return wrapper







#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n___   ___   ___   283. Building A Speed-Test Decorator   ___   ___   ___\n")



#	283. Building A Speed-Test Decorator



#from functools import wraps
from time import time

def speed_test(fn):
	@wraps(fn)
	def wrapper(*args, **kwargs):
		start_time = time()
		result = fn(*args, **kwargs)
		end_time = time()
		print(f"Executing {fn.__name__}")
		print(f"Time Elapsed: {end_time - start_time}")
		return result
	return wrapper

@speed_test
def sum_nums_gen():
	return sum(num for num in range(900000))
@speed_test
def sum_nums_list():
	return sum([num for num in range(900000)])

print(sum_nums_gen())
print(sum_nums_list())



#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n___   ___   ___   Coding Exercise 89: show_args   ___   ___   ___\n")



#	Coding Exercise 89: show_args



from functools import wraps

def show_args(fn):
	"""

	@show_args
	def do_nothing(*args, **kwargs):
    pass
	do_nothing(1, 2, 3,a="hi",b="bye")

	# Should print (on two lines):
	# Here are the args: (1, 2, 3)
	# Here are the kwargs: {"a": "hi", "b": "bye"}
	"""
	def wrapper(*args, **kwargs):
		#results = fn(*args, **kwargs)
		print(f"Here are the args: {args}")
		print(f"Here are the kwargs: {kwargs}")
	#	return results
	return wrapper

@show_args
def do_nothing(*args, **kwargs):
	pass

do_nothing(1, 2, 3,a="hi",b="bye")
# Here are the args: (1, 2, 3)
# Here are the kwargs: {'a': 'hi', 'b': 'bye'}



#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n___   ___   ___   ___   ___   ___   285. Another Example: Ensuring Args With A Decorator\n")



#	285. Another Example: Ensuring Args With A Decorator



#	This is to write a wrapper that checks for not allowed arguments such as kwargs in this example
from functools import wraps
def ensure_no_kwargs(fn):
	@wraps(fn)
	def wrapper(*args, **kwargs):
		if kwargs:
			raise ValueError("No kwargs allowed! Sorry :(")
		return fn(*args, **kwargs)
	return wrapper

@ensure_no_kwargs
def greet(name):
	print(f"Hi there {name}")

greet("Tony")
# Hi there Tony

#greet(name = "Tony")    <<<===    this will raise ValueError



#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n___   ___   ___   ___   ___   ___   Coding Exercise 90: double_return\n")



#	Coding Exercise 90: double_return



def double_return(fn):
	"""
	@double_return 
	def add(x, y):
		return x + y

	add(1, 2) # [3, 3]

	@double_return
	def greet(name):
		return "Hi, I'm " + name

	greet("Colt") # ["Hi, I'm Colt", "Hi, I'm Colt"]
	"""
	@wraps(fn)
	def wrapper(*args):
		return [fn(*args), fn(*args)]
	return wrapper

@double_return
def add(x, y):
	return x + y

@double_return
def greet(name):
	return "Hi, I'm " + name

print(add(1, 2))
print(greet("Colt"))
# [3, 3]
# ["Hi, I'm Colt", "Hi, I'm Colt"]



#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n___   ___   ___   ___   ___   ___   Coding Exercise 91: ensure_fewer_than_three_args\n")



#	Coding Exercise 91: ensure_fewer_than_three_args



from functools import wraps

def ensure_fewer_than_three_args(fn):
	"""
	@ensure_fewer_than_three_args
	def add_all(*nums):
		return sum(nums)

	add_all() # 0
	add_all(1) # 1
	add_all(1,2) # 3
	add_all(1,2,3) # "Too many arguments!"
	add_all(1,2,3,4,5,6) # "Too many arguments!"
	"""
	@wraps(fn)
	def wrapper(*args):
		if len(args) < 3:
			return fn(*args)
		else:
			print("Too many arguments!")
	return wrapper

@ensure_fewer_than_three_args
def add(*args):
	nums = args
	result = 0
	for num in nums:
		result += num
	print(result)

add()
add(1)
add(1, 2)
add(1, 2, 3)
add(1, 2, 3, 4, 5, 6)
# 0
# 1
# 3
# Too many arguments!
# Too many arguments!



#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - Coding Exercise 92: only_ints\n")



#	Coding Exercise 92: only_ints



from functools import wraps

def only_ints(fn):
	"""
	@only_ints 
	def add(x, y):
		return x + y
    
	add(1, 2) # 3
	add("1", "2") # "Please only invoke with integers."
	"""
	@wraps(fn)
	def wrapper(*args):
		if any([arg for arg in args if type(arg) != int]):
			return "Please only invoke with intergers."
		return fn(*args)
	return wrapper

@only_ints
def add(x, y):
	return x + y

print(add(1, 2))
print(add(1, "2"))
# 3
# Please only invoke with integers 



#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - Coding Exercise 93: ensure_authorized\n")



#	Coding Exercise 93: ensure_authorized



from functools import wraps

def ensure_authorized(fn):
	"""
	@ensure_authorized
	def show_secrets(*args, **kwargs):
		return "Shh! Don't tell anybody!"

	show_secrets(role="admin") # "Shh! Don't tell anybody!"
	show_secrets(role="nobody") # "Unauthorized"
	show_secrets(a="b") # "Unauthorized"
	"""
	@wraps(fn)
	def wrapper(*args, **kwargs):
		if kwargs.get("role") == "admin":
			return fn(*args, **kwargs)
		return "Unauthorized"
	return wrapper

@ensure_authorized
def show_secrets(*args, **kwargs):
	return "Shh! Don't tell anybody"	

print(show_secrets(role = "admin"))
print(show_secrets("admin"))
# Shh! Don't tell anybody
# Unauthorized



#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 290. Writing an ensure_first_arg_is Decorator \n")



#	290. Writing an ensure_first_arg_is Decorator



#	To define a decorator with argument, it required aditional layer inner()
from functools import wraps
def ensure_first_arg_is(val):
	def inner(fn):
		@wraps(fn)
		def wrapper(*args, **kwargs):
			if args and args[0] != val:    #    <<<===    checks if there is any args and then if the 1st one is val
				return f"First arg needs to be {val}"
			return fn(*args, **kwargs)
		return wrapper
	return inner

@ensure_first_arg_is("burrito")
def fav_foods(*foods):
	print(foods)

print(fav_foods("burrito", "ice cream"))
print(fav_foods("ice cream", "burrito"))
# ('burrito', 'ice cream')
# First arg needs to be burrito



#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 291. Enforcing Argument Types With A Decorator \n")



#	291. Enforcing Argument Types With A Decorator



#	This example will require specific types of data and it will try to convert them
def enforce(*types):
	def decorator(f):
		def new_func(*args, **kwargs):
			# convert args into something mutable
			newargs = []
			for (a, t) in zip(args, types):
				newargs.append( t(a))
			return f(*newargs, **kwargs)
		return new_func
	return decorator

@enforce(str, int)    #    <<<===    this can be whatever type and how many types you want it will still work, like in function below
def repeat_msg(msg, times):
	for time in range(times):
		print(msg)

@enforce(float, float)    #    <<<===    another combination
def divide(a, b):
	print(a/b)

repeat_msg("hello", "3")
divide("3", 1)
# hello
# hello
# hello
# 3.0



#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - Coding Exercise 94: delay \n")



#	Coding Exercise 94: delay



from functools import wraps
from time import sleep

def delay(time):
	"""
	@delay(3)
	def say_hi():
		return "hi"

	say_hi()
	# should print the message "Waiting 3s before running say_hi" to the console
	# should then wait 3 seconds
	# finally, should invoke say_hi and return "hi"
	"""
	def inner(fn):
		@wraps(fn)
		def wrapper(*args, **kwargs):
			print("Waiting 3s before running say_hi")
			sleep(time)
			return fn(*args, **kwargs)
		return wrapper
	return inner

@delay(3)
def say_hi():
	return "hi"

print(say_hi())



#	================================================================================================
#	================================================================================================
#	================================================================================================



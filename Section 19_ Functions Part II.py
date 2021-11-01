


#	================================================================================================
#	================================================================================================
#	================================================================================================



#	Section 19: Functions Part II



#	175. Intruduction  and *args
#	177. **kwargs
#	179. Ordering Parameters
#	180. Tuple unpacking
#	182. Dictionary unpacking


#	Coding Exercise 57: *args
#	Coding Exercise 58: **kwargs
#	Coding Exercise 59: Unpacking
#	Coding Exercise 60: Calculate



#	================================================================================================
#	================================================================================================
#	================================================================================================



#	175. Introduction and *args



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



#	================================================================================================
#	================================================================================================
#	================================================================================================



#	177. **kwargs



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



#	================================================================================================
#	================================================================================================
#	================================================================================================



#	Coding Exercise 58: **kwargs Exercise



#	combine_words

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



#	================================================================================================
#	================================================================================================
#	================================================================================================



#	179. Parameter Ordering



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
# default parameter - instructor - "Colt"
# kwargs - {'last_name': "Steele", "job": "Instructor"}	<<<===	dictionaries
# [1, 2, (3,), 'Colt', {'last_name': 'Steele', 'job': 'Instructor'}]



#	================================================================================================
#	================================================================================================
#	================================================================================================



#	180. Tumple unpacking



def sum_all_values(*args):
	print(args)
	# ([1, 2, 3, 4, 5, 6],)	#	<<<===
	total = 0
	for num in args:
		total += num
	print(total)
nums = [1, 2, 3, 4, 5, 6]
sum_all_values(*nums)	#	<<<===	nums as a list passed to args becomes as a tuple with one value, example above
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



#	================================================================================================
#	================================================================================================
#	================================================================================================



#	Coding Exercise 59: Unpacking Exercise



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



#	================================================================================================
#	================================================================================================
#	================================================================================================



#	128. Dictionary Unpacking



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



#	================================================================================================
#	================================================================================================
#	================================================================================================



#	Coding Exercise 60: Calculate


#	calculate

def calculate(**kwargs):
	"""
	calculate(make_float=False, operation='add', message='You just added', first=2, second=4) # "You just added 6"
	calculate(make_float=True, operation='divide', first=3.5, second=5) # "The result is 0.7"
	"""
	operation_lookup = {
		'add': kwargs.get('first', 0) + kwargs.get('second', 0),
		'subtract': kwargs.get('first', 0) - kwargs.get('second', 0),
		'divide': kwargs.get('first', 0) / kwargs.get('second', 0),
		'multiply': kwargs.get('first', 0) * kwargs.get('second', 0)
	}
	is_float = kwargs.get('make_float', False)
	operation_value = operation_lookup[kwargs.get('operation', '')]
	if is_float:
#		final = "{} {}".format(kwargs.get('message', 'The result is'), float(operation_value))
		final = f"{kwargs.get('message', 'The result is')} {float(operation_value)}"
	else:
#		final = "{} {}".format(kwargs.get('message', 'The result is'), int(operation_value))
		final = f"{kwargs.get('message', 'The result is')} {int(operation_value)}"
	print(final)

calculate(make_float=False, operation='add', message='You just added', first=2, second=4)
calculate(make_float=True, operation='divide', first=3.5, second=5)



#	================================================================================================
#	================================================================================================
#	================================================================================================






#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------



#	Coding Exercise 43: Product
#	Coding Exercise 44: return_day
#	Coding Exercise 45: last_element
#	Coding Exercise 46: number_compare
#	Coding Exercise 47: single_letter_count
#	Coding Exercise 48: multiple_letter_count
#	Coding Exercise 49: list_manipulation
#	Coding Exercise 50: is_palindrome
#	Coding Exercise 51: frequency
#	Coding Exercise 52: multiply_even_numbers
#	Coding Exercise 53: capitalize
#	Coding Exercise 54: compact
#	Coding Exercise 55: intersection
#	Coding Exercise 56: partition



#	================================================================================================
#	================================================================================================
#	================================================================================================




#	Coding Exercise 44: return_day



#	return_day

def return_day(number):
	"""
	************************************************************************************************
	return_day(1)	# "Sunday"
	return_day(2)	# "Monday"
	return_day(3)	# "Tuesday"
	return_day(4)	# "Wednesday"
	return_day(5)	# "Thursday"
	return_day(6)	# "Friday"
	return_day(7)	# "Saturday"
	return_day(41)  # None
	"""
	week_days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
	if number > 0 and number < 8:
		return week_days[number -1]
	else:
		None

print(return_day.__doc__)
print(f"\n\n        return_day(2):\n")
print(f"        {return_day(2)}\n\n\n")



#	Alternative code


def return_day(num):
    week_days = {
        1: "Sunday",
        2: "Monday",
        3: "Tuesday",
        4: "Wednesday",
        5: "Thursday",
        6: "Friday",
        7: "Saturday"
    }
    if num > 0 and num <8:
        return week_days.get(num)
    else:
        return None



#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------



#	Coding Exercise 45: last_element



#	last_element

def last_element(collection):
	"""
	************************************************************************************************
	last_element([1, 2, 3])	# 3
	last_element([])        # None
	"""
	if collection:
		return collection[-1]
	else:
		None

print(last_element.__doc__)
print(f"\n\n        last_element([1, 2, 3]):\n")
print(f"        {last_element([1, 2, 3])}\n\n\n")



#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------



#	Coding Exercise 46: number_compare



#	number_compare

def number_compare(number1, number2):
	"""
	************************************************************************************************
	number_compare(1, 1) # "Numbers are equal"
	number_compare(1, 0) # "First is greater"
	number_compare(2, 4) # "Second is greater"
	"""
	if number1 > number2:
		return "First is greater"
	elif number1 < number2:
		return "Second is greater"
	else:
		return "Numbers are equal"

print(number_compare.__doc__)
print(f"\n\n        number_compare(2, 3):\n")
print(f"        {number_compare(2, 3)}\n\n\n")



#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------



#	Coding Exercise 47: single_letter_count



#	single_letter_count

def single_letter_count(word, letter):
	"""
	************************************************************************************************
	single_letter_count("Hello World", "h") # 1
	single_letter_count("Hello World", "z") # 0
	single_letter_count("HelLo World", "l") # 3
	"""
	return word.lower().count(letter.lower())

print(single_letter_count.__doc__)
print(f"\n\n        single_letter_count('Hello World', 'l'):\n")
print(f"        {single_letter_count('Hello World', 'l')}\n\n\n")



#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------



#	Coding Exercise 48: multiple_letter_count



#	multiple_letter_count

def multiple_letter_count(word):
	"""
	************************************************************************************************
	multiple_letter_count("awesome") # {'a': 1, 'e': 2, 'm': 1, 'o': 1, 's': 1, 'w': 1}
	"""
	return {letter:word.count(letter) for letter in word}

print(multiple_letter_count.__doc__)
print(f"\n\n        multiple_letter_count('awesome'):\n")
print(f"        {multiple_letter_count('aweaome')}\n\n\n")



#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------



#	Coding Exercise 49: list_manipulation



#	list_manipulation

def list_manipulation(collection, command, location, value = None):
	"""
	************************************************************************************************
	list_manipulation([1, 2, 3], "remove", "end")        # 3
	list_manipulation([1, 2 ,3], "remove", "beginning")  # 1
	list_manipulation([1, 2, 3], "add", "beginning", 20) # [20, 1, 2, 3]
	list_manipulation([1, 2, 3], "add", "end", 30)       # [1, 2, 3, 30]
	"""
	if command == "remove" and location == "end":
		return collection.pop()
	elif command == "remove" and location == "beginning":
		return collection.pop(0)
	elif command == "add" and location == "beginning":
		collection.insert(0, value)
		return collection
	elif command == "add" and location == "end":
		collection.append(value)
		return collection

print(list_manipulation.__doc__)
print(f"\n\n        list_manipulation([1, 2, 3], 'remove', 'end'):\n")
print(f"        {list_manipulation([1, 2, 3], 'remove', 'end')}\n\n\n")



#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------



#	Coding Exercise 50: is_palindrome



#	is_palindrome

def is_palindrome(word):
	"""
	************************************************************************************************
	is_palindrome('testing')               # False
	is_palindrome('tacocat')               # True
	is_palindrome('hannah')                # True
	is_palindrome('robert')                # False
	is_palindrome('amanaplanacanalpanama') # True
	"""
	temp = list(word)
	temp.reverse()
	if list(word) == temp:
		return True
	else:
		return False

print(is_palindrome.__doc__)
print(f"\n\n        is_palindrome('tacocat'):\n")
print(f"        {is_palindrome('tacocat')}\n\n\n")



#	Alternative code:
#	Simpler version that doesn't ignore whitespaces
def is_palindrome2(string):
	return string == string[::-1]



#	Alternative code:
#	Bonus Version: that ignores whitespaces
def is_palindrome3(string):
	stripped = string.replace(" ", "").lower()
	return stripped == string[::-1]



#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------



#	Coding Exercise 51: frequency



#	frequency

def frequency(collection, search_term):
	"""
	************************************************************************************************
	frequency([1, 2, 3, 4, 4, 4], 4)               # 3
	frequency([True, False, True, True], False)    # 1
	"""
	return collection.count(search_term)
	
print(frequency.__doc__)
print(f"\n\n        frequency([1, 2, 3, 4, 4, 4], 4):\n")
print(f"        {frequency([1, 2, 3, 4, 4, 4], 4)}\n\n\n")



#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------



#	Coding Exercise 52: multiply_even_numbers



#	multiply_even_numbers

def multiply_even_numbers(collection):
	"""
	************************************************************************************************
	multiply_even_numbers([2, 3, 4, 5, 6])    # 48
	"""
	number = 1
	for num in collection:
		if num % 2 == 0:
			number = number * num
	return number

print(multiply_even_numbers.__doc__)
print(f"\n\n        multiply_even_numbers([2, 3, 4, 5, 6]):\n")
print(f"        {multiply_even_numbers([2, 3, 4, 5, 6])}\n\n\n")



#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------



#	Coding Exercise 53: capitalize



#	capitalize

def capitalize(string):
	"""
	************************************************************************************************
	capitalize("tim")     # "Tim"
	capitalize("matt")    # "Matt"
	"""
	return string[0].upper() + string[1:]

print(capitalize.__doc__)
print(f"\n\n        capitalize('matt'):\n")
print(f"        {capitalize('matt')}\n\n\n")



#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------



#	Coding Exercise 54: compact



#	compact

def compact(collection):
	"""
	************************************************************************************************
	compact([0, 1, 2, "", [], False, {}, None, "All done"])    # [1, 2, "All done"]
	"""
	new_collection = [val for val in collection if val]
	return new_collection


def compact2(collection):
	truthy_vals = []
	for val in collection:
		if val:
			truthy_vals.append(val)
	return truthy_vals



print(compact.__doc__)
print(f"\n\n        compact([0,1,2,'',[], False, None, 'All done']):\n")
print(f'        {compact([0,1,2,"",[], False, {}, None, "All done"])}\n\n\n')



#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------



#	Coding Exercise 55: intersection



#	intersection

def intersection(collection1, collection2):
	"""
	************************************************************************************************
	intersection([1, 2, 3], [2, 3, 4])                # [2, 3]
	intersection(['a', 'b', 'z'], ['x', 'y', 'z'])    # ['z']
	"""
	return [val for val in collection1 if val in collection2]

print(intersection.__doc__)
print(f"\n\n        intersection(['a', 'b', 'z'], ['x', 'y', 'z']):\n")
print(f"        {intersection(['a', 'b', 'z'], ['x', 'y', 'z'])}\n\n\n")



#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------



#	Coding Exercise 56: partition



#	partition

def isEven(num):
        return num % 2 == 0

def partition(collection, callback):
	"""
	************************************************************************************************
	def isEven(num):
		return num % 2 == 0

	partition([1, 2, 3, 4], isEven)    # [[2, 4],[1, 3]]
	"""
	truthy = []
	falsy = []
	for val in collection:
		if callback(val):
			truthy.append(val)
		else:
			falsy.append(val)
	return [truthy, falsy]

print(partition.__doc__)
print(f"\n\n        partition([1,2,3,4], isEven):\n")
print(f"        {partition([1,2,3,4], isEven)}\n\n\n")



#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------






#	================================================================================================
#	================================================================================================
#	================================================================================================



#	Section 20: Lambdas and Built-in Functions



#	184. Lambdas
#	186. Map
#	188. Filter
#	190. Any and All
#	191. Generator Expressions and Using sys.getsizeof
#	193. Sorted
#	194. Min and Max
#	196. Reversed
#	197. Len() and a Special Sneak Peak of OOP!
#	198. Abs(), Sum(), and Round()
#	202. Zip Basics
#	203. More Complex Zip Examples



#	Coding Exercise 61: Writing Your Own Lambda!
#	Coding Exercise 63: Filter Exercise!
#	Coding Exercise 64: Any/All Exercise
#	Coding Exercise 65: Extremes Exercise - Using Min and Max
#	Coding Exercise 66: Greatest Magnitude Exercise
#	Coding Exercise 67: sum_even_values
#	Coding Exercise 68: sum_floats
#	Coding Exercise 69: Interleaving Strings (kind of tough!)
#	Coding Exercise 70: triple_and_filter
#	Coding Exercise 71: extract_full_name



#	================================================================================================
#	================================================================================================
#	================================================================================================



#	184. Lambdas



def square(num):
	return num * num
print(square(9))
# 81

def square(num):	return num * num
print(square(9))
# 81

#	Lambdas are like Anonimous Functions, they are not defined but can be assigned to a variable. Lambda can take just one expresion and returns stight away so you dont need to type in return.
square2 = lambda num: num * num
print(square2(9))
# 81

add = lambda a, b: a + b
print(add(2, 3))
# 5

print(square.__name__)
# square
print(square2.__name__)
# <lambda>
print(add.__name__)
# <lambda>



add_values = lambda x, y: x + y
multiply_values = lambda x, y: x * y
print(add_values(10, 20))
#30
print(multiply_values(10, 20))
# 200



#	================================================================================================
#	================================================================================================
#	================================================================================================



#	186. Map



#	Maps can be used just ONCE, if needed they need to be recreated
#	A  standard function that accepts at least two arguments, a function and an "iterable".
#	Runs the lambda for each value in the iterable and returns a map object which can be converted into another data structure



nums = [2, 4, 6, 8, 10]
squares = map(lambda x: x ** 2, nums)
print(squares)
# <map object at 0x102583e80>
for num in squares:
	print(num)
# 4
# 16
# 36
# 64
# 100



doubles = list(map(lambda num: num * 2, nums))
print(doubles)
# [4, 8, 12, 16, 20]



people = ["Darcy", "Christina", "Dana", "Annabel"]
peeps = map(lambda name: name.upper(), people)
peeps = list(peeps)
print(peeps)
# ['DARCY', 'CHRISTINA', 'DANA', 'ANNABEL']

print(list(map(lambda name: name.upper(), people)))
# ['DARCY', 'CHRISTINA', 'DANA', 'ANNABEL']



names = [
	{'first': 'Ruby', 'last': 'Steeele'},
	{'first': 'Colt', 'last': 'Steele'},
	{'first': 'Blue', 'last': 'Steele'}
]
first_names = list(map(lambda x: x['first'], names))
print(first_names)
# ['Rusty', 'Colt', 'Blue']



#	================================================================================================
#	================================================================================================
#	================================================================================================



#	188. Filter



#	There is a lambda for each value in the iterable.
#	Returns filter object which can be converted into other iterables.
#	The object contains only the values that return true to the lambda.



collection = [1, 2, 3, 4]
evens = list(filter(lambda num: num % 2 == 0, collection))
print(evens)
# [2, 4]



names = ["austin", "penny", "angel", "billy"]
a_names = list(filter(lambda char: char[0] == "a", names))
print(a_names)
# ['austin', 'angel']



users = [
	{"username": "samuel", "tweets": ["I love cake", "I love pie"]},
	{"username": "katie", "tweets": ["I love my cat"]},
	{"username": "jeff", "tweets": []},
	{"username": "bob123", "tweets": []},
	{"username": "doggo_luvr", "tweets": ["dogs are the best", "I'm hungry"]},
	{"username": "guitar_gal", "tweets": []}
]
inactive_users = list(filter(lambda user: len(user["tweets"])  == 0, users))
print(inactive_users)
# [{"username": "jeff", "tweets": []}, {"username": "bob123", "tweets": []}, {"username": "guitar_gal", "tweets": []}]

inactive_users = list(filter(lambda user: not user["tweets"], users))    #    <<<===    not negates True and flips filter(True) to filter(false)
print(inactive_users)
# [{"username": "jeff", "tweets": []}, {"username": "bob123", "tweets": []}, {"username": "guitar_gal", "tweets": []}]

user_names = list(map(lambda user: user["username"].upper(),
	filter(lambda user: not user["tweets"], users)
))
print(user_names)
# ['JEFF', 'BOB123', 'GUITAR_GAL']



#	Combining filter and map



#	To return a list with a string "Your instructor is" + each value in the list, but only if the value is ledd than 5 characters
#	Iterable(filter) runs 1st, thats why the output is just one value.
names = ['Lassie', 'Colt', 'Rusty']
print(list(map(lambda name: f"Your instructor is {name}", filter(lambda value: len(value) < 5, names))))
#	map(               ^^^ function ^^^                                                             ^^^ iterable ^^^                                   )
# ['Your instructor is Colt']

print(list(map(lambda name: f"Your instructor is {name}",
	filter(lambda value: len(value) < 5, names))))
# ['Your instructor is Colt']



#	What about List Comprehension?



users = [
	{"username": "samuel", "tweets": ["I love cake", "I love pie"]},
	{"username": "katie", "tweets": ["I love my cat"]},
	{"username": "jeff", "tweets": []},
	{"username": "bob123", "tweets": []},
	{"username": "doggo_luvr", "tweets": ["dogs are the best", "I'm hungry"]},
	{"username": "guitar_gal", "tweets": []}
]
#	To return a list with a string "Your instructor is" + each value in the list, but only if the value is ledd than 5 characters
inactive_users_2 = [user for user in users if not user["tweets"]]
print(inactive_users_2)
# [{"username": "jeff", "tweets": []}, {"username": "bob123", "tweets": []}, {"username": "guitar_gal", "tweets": []}]
inactive_users_3 = [user["username"].upper() for user in users if not user["tweets"]]
print(inactive_users_3)
# ['JEFF', 'BOB123', 'GUITAR_GAL']



#	================================================================================================
#	================================================================================================
#	================================================================================================



#	190. Any and All



#	All
#	Takes in iterable and returns True if all values are True



all([0, 1, 2, 3])    # False
all([char for char in 'eio' if char in 'aeiou'])    # True
all([num for num in [4, 2, 10, 6, 8] if num % 2 == 0])    # True



people = ["Charlie", "Casey", "Cody", "Carly", "Cristina"]
[name[0] == 'C' for name in people]
# [True, True, True, True, True]
all([name[0] == 'C' for name in people])
# True
people.append("Kristy")
[name[0] == 'C' for name in people]
# [True, True, True, True, True, False]
all([name[0] == 'C' for name in people])
# False



#	Any
#	Takes in iterable and returns True if any of the values is True



any([0, 1, 2, 3])    # True
any([val for val in [1, 2, 3] if val > 2])    # True
any([val for val in [1, 2, 3] if val > 5])    # False



#	================================================================================================
#	================================================================================================
#	================================================================================================



#	191. Generator Expresions and Using sys.getsizeof



#	They are more light weight and quiker



people = ["Charlie", "Casey", "Cody", "Carly", "Cristina", "Kristy"]
print(people)
all(name[0] == 'C' for name in people)
# False
people2 = (name[0] == 'C' for name in people)
print(people2)
# <generator object <genexpr> at 0x7f872a2750>



#	Memory Size Comparison List Comprehension vs Generator Expression


import sys
list_comp = sys.getsizeof([x * 10 for x in range(1000)])
gen_exp = sys.getsizeof(x * 10 for x in range(1000))
print("To do the same thing, it takes...")
print(f"List Comprehension: {list_comp} bytes")
print(f"Generator Expression: {gen_exp} bytes")
# To do the same thing, it takes...
# List Comprehension: 9024 bytes
# Generator Expression: 120 bytes



#	================================================================================================
#	================================================================================================
#	================================================================================================



#	Coding Exercise 64: Any/All Exercise



#	is_all_strings are True



def is_all_strings_1(collection):
	print(all(type(val) == str for val in collection))
is_all_strings_1(['a', 'b', 'c'])
is_all_strings_1([2, 'a', 'b', 'c'])
is_all_strings_1(['hello', 'googbye'])
# True
# False
# True

def is_all_strings_2(collection):
	print(all([type(val) == str for val in collection]))
is_all_strings_2(['a', 'b', 'c'])
is_all_strings_2([2, 'a', 'b', 'c'])
is_all_strings_2(['hello', 'googbye'])
# True
# False
# True



#	================================================================================================
#	================================================================================================
#	================================================================================================



#	193. Sorted



#	Sorted works with anything that is iterable, but it does not override original iterable unless redefined over original iterable



more_numbers = [6, 1, 8, 2]
print(sorted(more_numbers))
print(more_numbers)
print(sorted(more_numbers, reverse = True))
print(sorted([4, 6, 1, 30, 55, 23]))    #    <<<===    tuple, but it still returns list
# [1, 2, 6, 8]
# [6, 1, 8, 2]
# [8, 6, 2, 1]
# [1, 4, 6, 23, 30, 55]



users = [
	{"username": "samuel", "tweets": ["I love cake", "I love pie"]},
	{"username": "katie", "tweets": ["I love my cat"]},
	{"username": "jeff", "tweets": []},
	{"username": "bob123", "tweets": []},
	{"username": "doggo_luvr", "tweets": ["dogs are the best", "I'm hungry"]},
	{"username": "guitar_gal", "tweets": []}
]
#sorted(users)
# TypeError: ...
print(sorted(users, key = len))
# {"username": "samuel", "tweets": ["I love cake", "I love pie"]}
# {"username": "katie", "tweets": ["I love my cat"]}
# {"username": "jeff", "tweets": [], "color": "purple"}
# {"username": "bob123", "tweets": [], "name": "Blue", "color": "teal"}
# {"username": "doggo_luvr", "tweets": ["dogs are the best", "I'm hungry"]}
# {"username": "guitar_gal", "tweets": []}
print(sorted(users, key = lambda user: user['username']))
# {"username": "bob123", "tweets": [], "name": "Blue", "color": "teal"}
# {"username": "doggo_luvr", "tweets": ["dogs are the best", "I'm hungry"]}
# {"username": "guitar_gal", "tweets": []}
# {"username": "jeff", "tweets": [], "color": "purple"}
# {"username": "katie", "tweets": ["I love my cat"]}
# {"username": "samuel", "tweets": ["I love cake", "I love pie"]}
print(sorted(users, key = lambda user: len(user['tweets'])))
# {"username": "jeff", "tweets": [], "color": "purple"}
# {"username": "bob123", "tweets": [], "name": "Blue", "color": "teal"}
# {"username": "guitar_gal", "tweets": []}
# {"username": "katie", "tweets": ["I love my cat"]}
# {"username": "samuel", "tweets": ["I love cake", "I love pie"]}
# {"username": "doggo_luvr", "tweets": ["dogs are the best", "I'm hungry"]}
print(sorted(users, key = lambda user: len(user['tweets']), reverse = True))
# {"username": "samuel", "tweets": ["I love cake", "I love pie"]}
# {"username": "doggo_luvr", "tweets": ["dogs are the best", "I'm hungry"]}
# {"username": "katie", "tweets": ["I love my cat"]}
# {"username": "jeff", "tweets": [], "color": "purple"}
# {"username": "bob123", "tweets": [], "name": "Blue", "color": "teal"}
# {"username": "guitar_gal", "tweets": []}



songs = [
	{"title": "happy bithday", "playcount": 1},
	{"title": "Survive", "playcount": 6},
	{"title": "YMCA", "playcount": 99},
	{"title": "Toxic", "playcount": 31}
]
print(sorted(songs, key = lambda playcount: playcount["playcount"]))
# {"title": "happy bithday", "playcount": 1}
# {"title": "Survive", "playcount": 6}
# {"title": "Toxic", "playcount": 31}
# {"title": "YMCA", "playcount": 99}
print(sorted(songs, key = lambda playcount: playcount["playcount"], reverse = True))
# {"title": "YMCA", "playcount": 99}
# {"title": "Toxic", "playcount": 31}
# {"title": "Survive", "playcount": 6}
# {"title": "happy bithday", "playcount": 1}



#	================================================================================================
#	================================================================================================
#	================================================================================================



#	194. Min and Max



#	max(strings, dics with the same keys)
#	min(strings, dics with the same keys)


max(1, 4, 76)                      # 76
max('c', 'd', 'a')                    # 'd'
max([3, 4, 1, 2])                  # 4
max([1, 2, 3, 4])                  # 4
max('hello world')             # 'w'
min('hello world')              # ' '
max({1: 'a', 3: 'c', 2: 'b'})    # 3



names = ['Arya', 'Samson', 'Dora', 'Tim', 'Ollivander']
min(names)    # 'Arya'
max(names)    # 'Tim'
print(min(len(name) for name in names))    #    <<<===    length of shortest word in this iterable
# 3
print(max(names, key = lambda longest_name: len(longest_name)))    #    <<<===    longest name in this iterable
# Ollivander
print(min(names, key = lambda longest_name: len(longest_name)))    #    <<<===    shortest name in this iterable
# Tim


songs = [
	{"title": "happy bithday", "playcount": 1},
	{"title": "Survive", "playcount": 6},
	{"title": "YMCA", "playcount": 99},
	{"title": "Toxic", "playcount": 31}
]
print(min(songs, key = lambda song: song["playcount"]))
# {"title": "happy bithday", "playcount": 1}
print(max(songs, key = lambda song: song["playcount"]))
#{"title": "YMCA", "playcount": 99}
print(min(songs, key = lambda song: song["playcount"])["title"])
# happy birthday
print(max(songs, key = lambda song: song["playcount"])["title"])
# YMCA



highest_playcount = 0
for song in songs:
	if song["playcount"] > highest_playcount:
		highest_playcount = song["playcount"]
print(highest_playcount)
# 99



#	================================================================================================
#	================================================================================================
#	================================================================================================



#	196. Reversed


nums = [1, 2, 3, 4]
print(reversed(nums))
#<list_reverseiterator object at 0x102.........>
print(list(reversed(nums)))
# [4, 3, 2, 1]



for char in reversed("hello world"):
	print(char)
# d
# l
# r
# o
# w
#  
# o
# l
# l
# h



#	================================================================================================
#	================================================================================================
#	================================================================================================



#	197. Len() and a Special Sneak Peak of OOP!



len('awesome')              # 7
len((1, 2, 3, 4))               # 4
len([1, 2, 3, 4])                # 4
len(range(0, 10))           # 10
len({1, 2, 3, 4})               # 4
len({'a': 1, 'b':2, 'c': 2})    # 3



print('awesome'.__len__())    # 7
[1, 2, 3, 4].__len__()                  # 4
'hi'.__len__()                             # 2



#	================================================================================================
#	================================================================================================
#	================================================================================================



#	198. Abs(), Sum(), and Round()



#	abs()
#	Returns the absolute value of the number. The argument may be an integer or a floating point number.
#	The Official Definition:    The magnitude of a real number without regard to its sign



abs(-5)    # 5
abs(5)     # 5

abs(-3.4444)    # 3.4444
abs(3.4444)     # 3.4444

#abs('20')    # TypeError: bad operand type for abs(): 'str'
abs(float('20'))    # 20.0



import math
math.fabs(-4)
# 4.0



#	sum()
#	Takes an iterable and an optional start.
#	Returns the sum of start and the items of an iterable form left to right and returns the total.
#	Start by default is 0.



sum([1, 2, 3])          # 6
sum([1, 2, 3], 10)    # 16
sum([1, 2, 3], -6)     # 0
sum((1.5, 2, 3.7))   # 7.2
sum({1, 50, 100})   # 151



#	round()



round(10.2)                 # 10
round(10.2, None)      # 10
round(1.212121, 2)    # 1.21
round(9.9999999999999999999999999, 15)    # 10.0



#	================================================================================================
#	================================================================================================
#	================================================================================================



#	Coding Exercise 66: Greatest Magnitude Exercise



def max_magnitude(collection):
	print(max(abs(val) for val in collection))
max_magnitude([300, 20, -900])
max_magnitude([10, 11, 12])
max_magnitude([-5, -1, -89])
max_magnitude([300, 20, -900])



#	================================================================================================
#	================================================================================================
#	================================================================================================



#	Coding Exercise 67: sm_even_values



def sum_even_values1(*args):
	"""
	sum_even_values(1, 2, 3, 4, 5, 6)    # 12
	sum_even_values(4, 2, 1, 10)          # 16
	sum_even_values(1)                        # 0
	"""
	print(sum(arg for arg in args if arg % 2 == 0))

sum_even_values1(1, 2, 3, 4, 5, 6)    # 12
sum_even_values1(4, 2, 1, 10)         # 16
sum_even_values1(1)                   # 0



#	================================================================================================
#	================================================================================================
#	================================================================================================



#	Coding Exercise 68: sum_floats



def sum_floats1(*args):
	final = 0
	for arg in args:
		if type(arg) == float:
			final += arg
	print(final)
sum_floats1(1.5, 2.4, 'awesome', [], 1)    # 3.9
sum_floats1(1, 2, 3, 4, 5)                 # 0



def sum_floats2(*args):
	"""
	sum_floats(1.5, 2.4, 'awesome', [], 1) # 3.9
	sum_floats(1,2,3,4,5) # 0
	"""
	print(sum(arg for arg in args if type(arg) == float))
sum_floats2(1.5, 2.4, 'awesome', [], 1)    # 3.9
sum_floats2(1, 2, 3, 4, 5)                 # 0



#	================================================================================================
#	================================================================================================
#	================================================================================================



#	202. Zip Basics



#	Makes an iterator that aggregates elements form each of the iterables.
#	Returns an iterator of tuples, where the i-th tuple contains the i-th element form each of the argument sequences or iterables.
#	The iterator stops when the shortest input iterable is exhausted.



first_zip = zip([1, 2, 3], [4, 5, 6])
list(first_zip)    # [(1, 4), (2, 5), (3, 6)]    <<<===    list of tuples
dict(first_zip)    # {1: 4, 2: 5, 3: 6}          <<<===    dictionary



nums1 = [1, 2, 3, 4, 5]
nums2 = [6, 7, 8, 9, 10]
zip(nums1, nums2)    # <zip object at 0x102...>
list(zip(nums1, nums2))    # [(1, 6), (2, 7), (3, 8), (4, 9), (5, 10)]    <<<===    list of tuples



nums3 = [1, 2, 3, 4, 5]
nums4 = [6, 7, 8, 9, 10, 11, 12]
list(zip(nums3, nums4))    # [(1, 6), (2, 7), (3, 8), (4, 9), (5, 10)]    <<<===    it stops at shortest iterable



nums1 = [1, 2, 3, 4, 5]
nums2 = [6, 7, 8, 9, 10]
words = ['hi', 'lol', 'haha', ':)']
list(zip(words, nums1, nums2))    # [('hi', 1, 6), ('lol', 2, 7), ('haha', 3, 8), (':)', 4, 9)]



five_by_two = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]
list(zip(*five_by_two))    # [(0, 1, 2, 3, 4), (1, 2, 3, 4, 5)]



#	================================================================================================
#	================================================================================================
#	================================================================================================



#	201. More Complex Zip Example



midterms = [80, 91, 78]
finals = [98, 89, 53]
students = ['dan', 'ang', 'kate']

final_grades = [pair for pair in zip(midterms, finals)]
print(final_grades)    # [(80, 98), (91, 89), (78, 53)]

final_grades = [max(pair) for pair in zip(midterms, finals)]
print(final_grades)    # [98, 91, 78]

#	Final version
final_grades = {student[0]:max(student[1], student[2]) for student in zip(students, midterms, finals)}
print(final_grades)    # {'dan': 98, 'ang': 91, 'kate': 78}



#	Alternative
midterms = [80, 91, 78]
finals = [98, 89, 53]
students = ['dan', 'ang', 'kate']

scores = map(
	lambda pair: max(pair),    # what to do 
	zip(midterms, finals)      # with what to do
)
print(list(scores))    # [98, 91, 78]

#	Final version
grades = zip(
	students,
	map(
		lambda pair: max(pair),
		zip(midterms, finals)
	)
)
print(dict(grades))    # {'dan': 98, 'ang': 91, 'kate': 78}




#	Alternative
final_grades = dict(
	zip(
	students,
		map(
			lambda pair: max(pair),    # what to do
			zip(midterms, finals)      # with what to do
		)
	)
)
print(final_grades)    # {'dan': 98, 'ang': 91, 'kate': 78}



#	Alternative
avg_grades = dict(
	zip(
		students,
		map(
			lambda pair: ((pair[0] + pair[1]) / 2),    # what to do
			zip(midterms, finals)                      # with what to do
		)
	)
)
print(avg_grades)    # {'dan': 89.0, 'ang': 90.0, 'kate': 65.5}



#	================================================================================================
#	================================================================================================
#	================================================================================================



#	Coding Exercise 69: Interveaving Strings (kind of tough!)



def interleave(string1, string2):
	"""
	interveaving('ha', 'hi')      # hhia
	interveaving('aaa', 'zzz')    # azaza
	interveaving('lzr', 'iad')    # lizard
	"""
	print(''.join(''.join(char) for char in (zip(string1, string2))))
interleave("hi", "ha")
interleave("aaa", "zzz")
interleave("lzr", "iad")



#	================================================================================================
#	================================================================================================
#	================================================================================================



#	Coding Exercise 70: triple_and_filter



def triple_and_filter1(collection):
	"""
	triple_and_filter([1,2,3,4]) # [12]
	triple_and_filter([6,8,10,12]) # [24,36]
	"""
	num_list = [num for num in collection if num % 4 == 0]
	final = [val * 3 for val in num_list]
	print(final)
triple_and_filter1([1, 2, 3, 4])
triple_and_filter1([6,8,10,12])



def triple_and_filter2(collection):
	print(list(filter(lambda num: num % 4 == 0, map(lambda num: num * 3, collection))))
triple_and_filter2([1, 2, 3, 4])
triple_and_filter2([6,8,10,12])



#	================================================================================================
#	================================================================================================
#	================================================================================================



#	Coding Exercise 71: extract_full_name



names = [{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]
def extract_full_name(string):
	"""
	names = [{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]
	extract_full_name(names) # ['Elie Schoppik', 'Colt Steele']
	"""
	print(list(map(lambda char: f"{char['first']} {char['last']}", string)))
	print(list(map(lambda val: "{} {}".format(val['first'], val['last']), string)))

extract_full_name(names)



#	================================================================================================
#	================================================================================================
#	================================================================================================



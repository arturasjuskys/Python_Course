#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------



#			udemy course: Colt Steele
#			Modern Python 3 Bootcamp


			
#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------



#	39.Numbers: Weirder Operators
# 	+ 
# 	- 
# 	* 
# 	/ 
# 	** Exponentials (3^3=9)
# 	% Modulo (remainder operator, 10 % 3 = 1)
# 	// Integer Division (10 // 3 = 3)



#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------



#	Order of Maths

# 	Parentheses
# 	Exponents
# 	Multiplication
# 	Division
# 	Addition
# 	Subtraction



#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------



#	50. String Escape Sequences 

# 		\n	- new line



#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------



#	54. String Formating



x = 10
formatted = f"I've told you {x} times already!"
formatted = f"I've told you {x + 100} times already!"


fruit = "banana"
ripness = "unripe"

print(f"The {fruit} is {ripness}")
print("The {} is {}".format(fruit, ripeness))










#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------










#	Truthiness & Falsyness

# 	Besides conditional check other things that are natursly falsy:
#		empty objects, empty strings, None, 0 (number zero).

# 	Naturaly truthy:
# 		1 (number one), 	










#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------










#	Section 10: Looping in Python



#	for loops


for item in iterable_object:
	# do something with item


for number in range(1, 8):
	print(number)
	print(number * 8)



#	range()



r = range(0, 20, 2)
print(list(r))
t = range(20, 0, -2)
print(list(t))



for num in range(0, 20, 2):
	print(num)



#	while loop


user = None
while user != "please":
	user = input("Ah ah ah, you didn't say the magic word: ")



num = 1    #    wariable needs to be set before while loop
while num < 11:
	print(num)    #    this will cause infinite loop, because num never changes



num = 1
while num < 11:
	num +=1    #    this is to update num value, and to excape infinite loop (num = num + 1)
	print(num)


#	break



while True:
	command = input("Type 'exit' to exit:")
	if (command == "exit"):
		break



times = int(input("How many times do I have to tell you? "))
for time in range(1, times):
	print("CLEAN UP YOUR ROOM!")
	if time >= 4:
		print("do you even listening me?")
		break










#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------










#	Section 12. Lists



tasks = ["Install Python", "Learn Python", "Take a break"]	# ["Intall Python", "Learn Python", "Take a break"]



nums = list(range(1, 100))



#	==



first_task = "Install Python"
second_task = "Learn Python"
third_task = "Take a break"

tasks = [first_task, second_task, third_task]	# ["Intall Python", "Learn Python", "Take a break"]

numbers = [2.22, 23452356, "dfgdf"]
numbers[2] = 687.2345
print(numbers)
# [2.22, 23452356, 687.2345]



#	Built in functions



len(tasks)	# 3	[ len ] this function is to check the length of the list

tasks = list(range(1, 4))	# [1, 2, 3]

print(tasks[0])	# 'Install Python'
print(tasks[1])	# 'Learn Python'
print(tasks[3])	# IndexError

print(tasks[-1])	# 'Take a break'
print(tasks[-2])	# 'Learn Python'
print(tasks[-3])	# 'Install Python'
print(tasks[-4])	# IndexError



#	.in this function is to check if a value is in the list 



"Install Python" in tasks	# True
"Forget Python" in tasks	# False



#	Iterating over Lists



tasks = ["Install Python", "Learn Python", "Take a break", True, 8.9]
for task in tasks:
	print(task)



num = [1, 4, 7, 8.9]
for number in num:
	print(number * number)



tasks = ["Install Python", "Learn Python", "Take a break", True, 8.9]
index = 0		
while index < len(tasks):
	print(f"{index}: {tasks[index]}")
	index += 1



#	.append does just one argument at the time


	
first_list = [1, 2, 3, 4]
first_list.append(5)
print(first_list)
# [1, 2, 3,4, 5]



#	.extend does multiple arguments at the time



correct_list = [1, 2, 3, 4]
correct_list.extend([5, 6, 7, 8])
print(correct_list)
# [1, 2, 3, 4, 5, 6, 7, 8]



#	.insert does an item to any given location in the list



first_list = [1, 2, 3, 4]
first_list.insert(2, "Hi")	# index starts from 0, thats why it pts it instead of numer 3
first_list.insert(-1, "The End")	# in this case .insert calculate index before inserting value in the list where -1 is the last index(4) but after it adds the value to 4th place thr list becomes 5 indexes lond and that value stays in 4th index not in the 5th index.
print(first_list)



#	if you want to add value to the actual last place use the code belaw with len function or use .append instead



first_list = [1, 2, 3, 4]
first_list.insert(len(first_list), "Last!!!")
print(first_list)



#	.clear will remove all items from the list no matter what the values are



first_list = [1, 2, 3, 4]
first_list.clear()
print(first_list)
# [ ]



#	.pop removes any specified item from the list and returns it, and if not specified will remove a last item by default (this return feature canbe used tho capture the value to a variable or something)



first_list = [1, 2, 3, 4]
first_list.pop()
print(first_list)
# [1, 2, 3]

first_list.pop(1)
print(first_list)
# [1, 3, ]



#	.remove works by removing value by using value it self instead of index



num_list = [1, 2, 3, 4, 4, 4]
num_list.remove(2)
print(num_list)
# [1, 3, 4, 4, 4]

num_list.remove(4)
print(num_list)
# [1, 3, 4, 4]



#	.index allows to find index of any give value



num_list = [5, 6, 7, 8, 9]
num_list.index(6)	# 1
num_list.index(9)	# 4

num_list = [5, 5, 6, 7, 5, 8, 8, 9, 10]
num_list.index(5)	# 0
num_list.index(5, 1)	# 1	- in this example second value specifies starting point
num_list.index(5, 2)	# 4
num_list(8, 6, 8)	# 8	- in this example 1st value is what you are looking for, and 2nd value is starting point, and 3rd value is end point in the list



#	.count takes one value and counts how many times it repeats in a given list



num_list = [1, 2, 3, 4, 3, 2, 1, 4, 10, 2]
num_list.count(2)	# 3
num_list.count(21)	# 0
num_list.count(3)	# 2



#	.reverse updates specified list in reverse order without making any copies



num_list = [1, 2, 3, 4]
num_list.reverse()
print(num_list)
# [4, 3, 2, 1]



#	.sort 



num_list = [6, 4, 1, 2, 5]
num_list.sort()
print(num_list)
# [1, 2, 4, 5, 6]



#	.join converts list to strings by combining all indexes with specified symbol or empty space in ' '



words = ["Coding", "Is", "Fun!"]
' '.join(words)	# Coding Is Fun!
name = ["Mr", "Stelee"]
'. '.join(name)	# Mr. Stelee
print(' '.join(words), '. '.join(name))
temp_string = ". ".join(name)



#	[slicing] creates new lists out of old list



some_list[start:end:step]

num_list = [1, 2, 3, 4]
num_list[1:]	# [2, 3, 4]	slicing: starts at index 0
num_list[3:]	# [4]			slicing: started fron origial list index 0 and original lists index 3 is value 4
num_list[-1:]	# [4]
num_list[-3:]	# [2, 3, 4]

num_list = [1, 2, 3, 4]
num_list[:2]	# [1, 2]	slicing:end is a exclusive value, mesning it does not include specified stop idex in new list
num_list[:4]	# [1, 2, 3, 4]	in this instance index 4 doesnt exist in this list so python returns everything before index 4 in this case whole list
num_list[1:3]	# [2, 3]	this time start point is from index 1 inclusive, and end point is index 3 which is exclusove and it returns values 2 and 3.
num_list[1:-1]	# [2, 3]	start index 1 inclusive, and end index -1 exclusive, which returns 2 and 3

num_list = [1, 2, 3, 4, 5, 6]
num_list[1::2]	# [2, 4, 6]    :start index is 1 which means the value is 2, and :end index is 5 which gives value of 6 the last value in the list(in this example :: in the middle is a short hand for :end point to be the end of list), and :step value of 2 means that it will use every other valua in the list
num_list[::2]	# [1, 3, 5]    the :start value is index 0, :end value is index 5(last item in the list), and :setp is every athor index in the list
num_list[1::-1]    # [2, 1]    :start is index 1(value of 2 in the list), :end index 5(last item in the list), :step -1 reverses direction of values used from
num_list[:1:-1]     # [6, 5, 4, 3]    :start point is not specified, :end point is index 1(list value of 2), :step -1(reverses direction of values used)
num_list[2::-1]     # [3, 2, 1]    :start point is index 2(list value of 3), :end point not specified, :step -1(which reverses direction of values used from)

numbers = [1, 2, 3, 4, 5]
numbers[1:3] = ["a", "b", "c"]    #    you can modifie list with :start and :end Slices to add or change values
print(a)
# [1, "a", "b", "c", 4, 5]

colours = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
colours[5][::-1]    # "ogidni"    in this instance [5] returns it as a string, and [::-1] reverses the order meaning string gets returned backwards



#	Swapping Values



names = ["James", "Michelle"]
names[0], names[1] = names[1], names[0]
print(names)
# ["Michelle", "James"]










#---------------------------------------------------------------------
#---------------------------------------------------------------------
#---------------------------------------------------------------------










#	Section 13: List Comprehension



#	[ __ for __ in __ ]



nums = [1, 2, 3]
[x*10 for x in nums]	# [10, 20 ,30]    fist value(x*10) is modifier, second value(x) is temporary variable, third value is the iterable.

name = "colt"
[char.upper() for char in name]    # ['C', 'O', 'L', 'T']

friends = ['ashley', 'matt', 'michael']
[friend[0].upper() for friend in friends]    # ['Ashley', 'Matt', 'Michael']

[num*10 for num in range(1, 6)]    # [10, 20, 30, 40, 50]

[bool(val) for val in [0, [], '']]    # [False, False, False]

numbers = [1, 2, 3, 4, 5]
string_list = [str(num) for num in numbers]
print(string_list)
# ['1', '2', '3', '4', '5']



#	List Conprehension with Conditional Logic



numbers = [1, 2, 3, 4, 5, 6]
evens = [num for num in numbers if num % 2 == 0]
odds = [num for num in numbers if num % 2 != 0]
rest = [num*2 if num % 2 == 0 else num/2 for num in numbers]    # in this Comprehension code takes even numbers and multiplies them by 2, and odds numbers divide by two
print(evens, odds, rest)



#    to take away values for a string or a list with a string or a list



with_vowels = "This is so much fun!"
''.join(char for char in with_vowels if char not in "aeiou")
# "Ths s s mch fn!"



#    to check if one list items are contained in another list



answer = [val for val in [1, 2, 3, 4] if val in [3, 4, 5, 6]]
print(answer)
# [3, 4]
answer2 = [name[::-1].lower() for name in ["Elie", "Tim", "Matt"]]
print(answer2)
# ['eile', 'mit', 'ttam']



#    Nested Lists



nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
nested_list[0][1]    # 2
nested_list[1][-1]    # 6



#    to loop through nested structures you need to use two loops, 1st loop to iterate over top structure, and second loop to iterate over structure below



nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for num in nested_list:
	for val in num:
		print(val)
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9



nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
[[print(val) for val in num] for num in nested_list]
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9



board = [[num for num in range(1, 4)] for val in range(1, 4)]
print(board)
# [[1, 2, 3], [1, 2, 3], [1, 2, 3]]



#    this comprehansion is to generate an 'X' to odd numbers, and 'O' to even numbers



XOXO = [["X" if num % 2 != 0 else "O" for num in range(1, 4)] for val in range(1, 4)]
print(XOXO)
# [['X', 'O', 'X'], ['X', 'O', 'X'], ['X', 'O', 'X']]










#---------------------------------------------------------------------
#---------------------------------------------------------------------
#---------------------------------------------------------------------










#    Section 14: Dictionaries



instructor = {
	"name": "Colt",
	"owns_dog": True,
	44: "favorite number"
}



instructor = dict(name = 'Colt', owns_dog = True)    #    not sure for now how to add 44 = 'favorite number'
print(instructor)
# {'name': 'Colt', 'owns_dog' = True}



instructor["name"]    # 'Colt'
instructor["thing"]    # KeyError



#    .values()



instructor = {
	"name": "Colt",
	"owns_dog": True,
	44: "favorite number"
}
for value in instructor.values():
	print(value)
# 'Colt'
# True
# 'favorite number'



#    .keys()



instructor = {
	"name": "Colt",
	"owns_dog": True,
	44: "favorite number"
}
for key in instructor.keys():
	print(key)
# 'name'
# 'owns_dogl'
# 'favorite number'



#    .items()



instructor = {
	"name": "Colt",
	"owns_dog": True,
	44: "favorite number"
}
for key,value in instructor.items():
	print(f"{key}: {value}")
# name: Colt
# owns_dog: True
# 44: favorite number



#    in



instructor = {
	"name": "Colt",
	"owns_dog": True,
	44: "favorite number"
}
"name" in instructor    # True
"awesom" in instructor    # False

"Colt" in instructor.values()    # True



#    .clear()



instructor = {
	"name": "Colt",
	"owns_dog": True,
	44: "favorite number"
}
instructor.clear()
instructor    # { }



#    .copy()



instructor = {
	"name": "Colt",
	"owns_dog": True,
	44: "favorite number"
}
instructor2 = instructor.copy()
print(instructor2)
# {'name': 'Colt', 'owns_dog': True, 44: 'favorite number'}
instructor == instructor2    # True
instructor2 is instructor    # False



#    .fromkeys()



{}.fromkeys("a", "b")    # {'a': 'b'}
{}.fromkeys(["email"], "unknown")    # {'email': 'unknown'}
{}.fromkeys("a", [1, 2, 3, 4, 5])    # {'a': [1, 2, 3, 4, 5]}
{}.fromkeys("hello", "unknown")    # {'h': 'unknown', 'e': 'unknown', 'l': 'unknown', 'l': 'unknown', 'o': 'unknown'}



#    .get()



instructor = {
	"name": "Colt",
	"owns_dog": True,
	44: "favorite number"
}
instructor.get("name")    # 'Colt'

instructor["no_key"]    # KeyError
instructor.get("no_key")    # None



#    .pop()



instructor = {
	"name": "Colt",
	"owns_dog": True,
	44: "favorite number"
}
instructor.pop("name")    # 'Colt'
print(instructor)
# {'owns_dog': True, 44: 'favorite number'}
instructor.pop("surname")    # KeyError



#    .popitem()    it removes random key value pair and returns it.



instructor = {
	"name": "Colt",
	"owns_dog": True,
	44: "favorite number"
}
instructor.popitem()    # (44, 'favorite number')
instructor.popitem('name')    # TypeError: popitem() takes no arguments (1 given)



#    .update()    updates keys and values in a dictionary with another set of key value pairs



first = dict(a = 1, b = 2, c = 3, d = 4, e = 5)
second = {}

second = {"f": 9}
second.update(first)
print(second)
# {'f': 9, 'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}




#    in this instance .update() does override an exsisting key value pair
person = {
	"name": "Colt"
}
instructor = {
	"name": "Colt",
	"owns_dog": True,
	44: "favorite number"
}
instructor["name"] = "John"
print(instructor)
# {'name': 'John', 'owns_dog': True, 44: 'favorite number'}
instructor.update(person)
print(instructor)
# {'name': 'Colt', 'owns_dog': True, 44: 'favorite number'}
instructor["surname"] = "surname"
print(instructor)
# {'name': 'Colt', 'owns_dog': True, 44: 'favorite number', 'surname': 'surname'}



#    Dictionary Comprehension



#    {___:___ for ___ in ___}



numbers = dict(first = 1, second = 2, third = 3)
squared_numbers = {key: value ** 2 for key,value in numbers.items()}
print(squared_numbers)
# {'first': 1, 'second': 4, 'third': 9}



numbers2 = {num: num ** 2 for num in [1, 2, 3, 4, 5]}
print(numbers2)
# {1:1, 2: 4, 3: 9, 4: 16, 5: 25}



str1 = "ABC"
str2 = "123"
combo = {str1[i]: str2[i] for i in range(0, len(str1))}
print(combo)
# {'A': '1', 'B': '2', 'C': '3'}



instructor = {"name": "colt", "city": "san francisco", "colour": "purple"}
yelling_instructor = {key.upper():value.upper() for key,value in instructor.items()}
print(yelling_instructor)
# {'NAME': 'COLT', 'CITY': 'SAN FRANCISCO', 'COLOUR': 'PURPLE'}

sometimes_yelling_instructor = {(key.upper() if key is "colour" else key):value.upper() for key,value in instructor.items()}
print(sometimes_yelling_instructor)
# {'name': 'COLT', 'city': 'SAN FRANCISCO', 'COLOUR': 'PURPLE'}



num_list = [1, 2, 3, 4]
altered = {num:("even" if num % 2 == 0 else "odd") for num in num_list}
print(altered)
# {1: 'odd', 2: 'even', 3: 'odd', 4: 'even'}



names = [["name", "Colt"], ["surname", "Stelee"], ["courses", 8]]
new_names_list = {val[0]: val[1] for val in names}
print(new_names_list)
# {'name': 'Colt', 'surname': 'Stelee', 'courses': 8}
names = [["name", "Colt"], ["surname", "Stelee"], ["courses", 8]]
new_names_list = {key: value for key,value in names}
print(new_names_list)
# {'name': 'Colt', 'surname': 'Stelee', 'courses': 8}
names = [["name", "Colt"], ["surname", "Stelee"], ["courses", 8]]
new_names_list = dict(names)
print(new_names_list)
# {'name': 'Colt', 'surname': 'Stelee', 'courses': 8}



answer1 = {char:0 for char in 'aeiou'} 
print(answer1)
# {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
answer2 = dict.fromkeys("aeiou", 0) 
print(answer2)
# {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}



#    chr()



answer = {num: chr(num) for num in range(65, 91)}
print(answer)
# {65: 'A', 66: 'B', 67: 'C', 68: 'D', 69: 'E', 70: 'F', 71: 'G', 72: 'H', 73: 'I', 74: 'J', 75: 'K', 76: 'L', 77: 'M', 78: 'N', 79: 'O', 80: 'P', 81: 'Q', 82: 'R', 83: 'S', 84: 'T', 85: 'U', 86: 'V', 87: 'W', 88: 'X', 89: 'Y', 90: 'Z'}










#---------------------------------------------------------------------
#---------------------------------------------------------------------
#---------------------------------------------------------------------










#    Section 16: Tuples and Sets



#    Its an ordered collection or grouping of items, and it is immutable, meaning after setting tuple you can't update it or change it's values. Tuples are faster than lists, it makes code safer against ascidental changes and bugs.



#    tuples



numbers1 = (1, 2, 3, 4)
numbers2 = ()
tuple()



value = (1,)    #    to create tuple with one value you need to include comma at the back



x = (1, 2, 3, 3, 3)
3 in x    # True
x[0] = "change me!"    # TypeError: 'tuple' object does not support item assignment


months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
months[0]    # 'January'
months[-1]    # 'December'



nums = (1, 2, 3, (4, 5), 6, 7)
print(nums)
# (1, 2, 3, (4, 5), 6, 7)
nums[0]    # 1
nums[3]    # (4 ,5)
nums[3][1]    # 5



#    In this example tuple is set as dictionaries first value



locations = {
	(35.6895, 39.6917): "Tokyo Office",
	(40.7128, 74.0060): "New York Office",
	(37.7749, 122.4194): "San Francisco Office"
}
location[(37.7749, 122.4194)]    # 'San Francisco'



locs = {[35, 39]: "Tokyo Office"}    # TypeError: unhashable type: 'list'    in this instance its possible to use tuple instead



#    looping over tuples



names = ('Colt', 'Blue', 'Rusty', 'Lassie')
for name in names:
	print(name)
# Colt
# Blue
# Rusty
# Lassie



months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
i = len(months) -1
while i >= 0:
	print(months[i])
# December
# November
# October
# September
# August
# July
# June
# May
# April
# March
# February
# January



#    .count()



x = (1, 2, 3 , 3, 3)
x.count(1)    # 1
x.count(3)    # 3



#    .index()



t = (1, 2, 3, 3, 3)
t.index(1)    # 0
t.index(5)    # ValueError: tuple.index(x): x not in tuple
t.index(3)    # 2    only the 1st matching index is returned










#    Sets



#    Seets are like formal mathematical sets
#    Sets do not have dublicate values
#    Elements in sets aren't ordered
#    You cannot access items in a set by index
#    Sets can be useful if you need to keep track of a collection of elements, but don't care about ordering, keys or values and duplicates



#    Sets cannot have duplicates
set = set({1, 2, 3, 4, 5, 5, 5})    # {1, 2, 3, 4, 5}

#    Creating new set
set = set({1, 4, 5})

#    Alternative
set = {1, 4, 5}

4 in set   # True
8 in set    # False



numbers = {1, 2, 3, 4}
for number in numbers:
	print(number)
# 1
# 2
# 3
# 4



cities = {"Los Angeles", "Florence", "Boulder", "Oslo", "Tokyo", "Santiago", "Tokyo", "San Francisco", "Shanghai", "San Francisco", "Oslo", "Boulder"}
print(list(set(cities)))
# ['Los Angeles', 'Florence', 'Boulder', 'Oslo', 'Tokyo', 'Santiago', 'Shanghai', 'San Francisco']
print(len(set(cities)))
# 8



#    .add()



set = set({1, 2, 3})
set.add(4)
print(set)
# {1, 2, 3, 4}
set.add(4)
print(set)
# {1, 2, 3, 4}



#    .remove()



set = set({1, 2, 3, 4, 5, 6})
set.remove(3)
print(set)
# {1, 2, 4, 5, 6}
set.remove(7)    # KeyError: '7'



#    .discard()
#    it will remove the value if it is there, but will not throw an error if the value is not in set



set = set({1, 2, 3, 4, 5, 6})
set.discard(7)
print(set)
# {1, 2, 3, 4, 5, 6}



#    .copy()



set = set({1, 2, 3})
another_set = set.copy()
print(another_set)
# {1 ,2, 3}
another_set is set    # False



#    .clear()



set = set({1, 2, 3})
set.clear()
print(set)
# set( )



#    Set Math



#    intersection



math_students = {"Matthew", "Helen", "Prashant", "James", "Aparna"}
biology_students = {"Jane", "Matthew", "Charlotte", "Mesut", "Oliver", "James"}
both_classes = math_students & biology_students
print(both_classes)
# {'James', 'Matthew'}



#    symmetric_difference



#    union



math_students = {"Matthew", "Helen", "Prashant", "James", "Aparna"}
biology_students = {"Jane", "Matthew", "Charlotte", "Mesut", "Oliver", "James"}
both_classes = math_students | biology_students
print(both_classes)
# {'Charlotte', 'Prashant', 'Jane', 'Oliver', 'Mesut', 'Helen', 'Aparna', 'Matthew'} 










#    Set Comprehension



#    to create set with set comprehension you need to specifie just one value not to like with dictionaries
value = {val ** 2 for val in range(10)}
print(value)
# {0, 1, 64, 4, 36, 9, 16, 49, 81, 25}



value2 = {char.upper() for char in "hello"}
print(value2)
# {'O', 'L', 'H', 'E'}










#---------------------------------------------------------------------
#---------------------------------------------------------------------
#---------------------------------------------------------------------



#---------------------------------------------------------------------
#---------------------------------------------------------------------
#---------------------------------------------------------------------



#---------------------------------------------------------------------
#---------------------------------------------------------------------
#---------------------------------------------------------------------



#---------------------------------------------------------------------
#---------------------------------------------------------------------
#---------------------------------------------------------------------



#---------------------------------------------------------------------
#---------------------------------------------------------------------
#---------------------------------------------------------------------



#---------------------------------------------------------------------
#---------------------------------------------------------------------
#---------------------------------------------------------------------



#---------------------------------------------------------------------
#---------------------------------------------------------------------
#---------------------------------------------------------------------



#---------------------------------------------------------------------
#---------------------------------------------------------------------
#---------------------------------------------------------------------



#---------------------------------------------------------------------
#---------------------------------------------------------------------
#---------------------------------------------------------------------



#---------------------------------------------------------------------
#---------------------------------------------------------------------
#---------------------------------------------------------------------



#---------------------------------------------------------------------
#---------------------------------------------------------------------
#---------------------------------------------------------------------



#---------------------------------------------------------------------
#---------------------------------------------------------------------
#---------------------------------------------------------------------



#---------------------------------------------------------------------
#---------------------------------------------------------------------
#---------------------------------------------------------------------



#---------------------------------------------------------------------
#---------------------------------------------------------------------
#---------------------------------------------------------------------
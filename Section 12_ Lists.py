


#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------



#	Section 12: Lists



#	97. Intro to Lists and Objectives
#	98. Creating Lists
#	100. Accessing Data in Lists
#	102. Iterating Over Lists
#	104. List Methods: Append, Insert, and Extend
#	106. List Methods: Clear, Pop, and Remove,
#	107. List Methods: Index, Count, Sort, Reverse, and Join
#	109. Slices
#	110. Swapping Values in Lists



#	Coding Exercise 15: Creating Lists Exercise
#	Coding Exercise 16: Accessing List Data
#	Coding Exercise 17: List Iteration Exercise
#	Coding Exercise 18: Lists Basics Exercise
#	Coding Exercise 19: Lists Methods Exercise



#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------



#	98. Creating Lists



first_task = "Install Python"
second_task = "Learn Python"
third_task = "Take a break"

tasks1 = ["Install Python", "Learn Python", "Take a break"]

tasks2 = [first_task, second_task, third_task]
print(tasks1)	# ['Install Python', 'Learn Python', 'Take a break']
print(tasks2)	# ['Install Python', 'Learn Python', 'Take a break']
print(len(tasks1))	# 3



tasks3 = list(range(1, 10))    #	list()	converts in this intance range to a list.
print(tasks3)
# [1, 2, 3, 4, 5, 6, 7, 8, 9]



#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------



#	100. Accessing Data in Lists



friends = ["Ashley", "Matt", "Michael"]

print(friends[0])	# 'Ashley'
print(friends[1])	# 'Matt'
print(friends[2])	# 'Michael'
# print(friends[4])	# IndexError

print(friends[-1])	# 'Michael'
print(friends[-2])	# 'Matt'
print(friends[-3])	# 'Ashley'
# print(friends[-4])	# IndexError

"Ashley" in friends    # True
"Colt" in friends      # False



#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------



#	102. Iterating Over Lists



numbers = [1, 2, 3, 4]
for number in numbers:
	print(number)
# 1
# 2
# 3
# 4



numbers = [1, 2, 3, 4]
index = 0
while index < len(numbers):
	print(numbers[index])
	index += 1
# 1
# 2
# 3
# 4



colours = ["purple", "teal", "magenta", "crimson", "emerald"]
index = 0
while index < len(colours):
	print(f"{index}: {colours[index]}")
	index += 1
# 0: purple
# 1: teal
# 2: magenta
# 3: crimson
# 4: emerald



#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------



#	104. List Methods: Append, Insert, and Extend



#	.append does just one argument at the time


	
first_list = [1, 2, 3, 4]
first_list.append(5)
print(first_list)
# [1, 2, 3,4, 5]



first_list = [1, 2, 3, 4]
first_list.append([5, 6, 7, 8])
print(first_list)
#	[1, 2, 3, 4, [5, 6, 7, 8]]



#	.extend does multiple arguments at the time



correct_list = [1, 2, 3, 4]
correct_list.extend([5, 6, 7, 8])
print(correct_list)
# [1, 2, 3, 4, 5, 6, 7, 8]



# #	.insert does an item to any given location in the list



first_list = [1, 2, 3, 4]
first_list.insert(2, "Hi")
print(first_list)
# [1, 2, 'Hi!', 3, 4]
first_list.insert(-1, "The End")    # in this case .insert calculate index before inserting value in the list where -1 is the last index(4) but after it adds the value to 4th place thr list becomes 5 indexes lond and that value stays in 4th index not in the 5th index.
print(first_list)
# [1, 2, 'Hi!', 3, 'The End', 4]



first_list = [1, 2, 3, 4]
first_list.insert(len(first_list), "Last!!!")
print(first_list)
# [1, 2, 3, 4, 'Last!!!']



#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------



#	106. List Methods: Clear, Pop, Remove






#	.clear will remove all items from the list no matter what the values are

first_list = [1, 2, 3, 4]
first_list.clear()
print(first_list)
# []



#	.pop removes any specified item from the list and returns it, and if not specified will remove a last item by default (this return feature canbe used tho capture the value to a variable or something)

first_list = [1, 2, 3, 4]
first_list.pop()
print(first_list)
# [1, 2, 3]

first_list.pop(1)
print(first_list)
# [1, 3]



#	.remove works by removing first value provided using value itself instead of index

num_list = [1, 2, 3, 4, 4, 4]
num_list.remove(2)
print(num_list)
# [1, 3, 4, 4, 4]

num_list.remove(4)
print(num_list)
# [1, 3, 4, 4]

# num_list.remove(5)
# print(num_list)    # ValueError



#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------



#	107. List Methods: Index, Count, Sort, Reverse, and Join



#	.index allows to find index of any give value

num_list = [5, 6, 7, 8, 9]
num_list.index(6)	# 1
num_list.index(9)	# 4

num_list = [5, 5, 6, 7, 5, 8, 8, 9, 10]
num_list.index(5)	# 0
num_list.index(5, 1)	# 1	- in this example second value specifies starting point
num_list.index(5, 2)	# 4
num_list.index(8, 6, 8)	# 6	- in this example 1st value is what you are looking for, and 2nd value is starting point, and 3rd value is end point in the list



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
# Coding Is Fun! Mr. Steele
temp_string = ". ".join(name)
print(temp_string)
# Mr. Steele



#	================================================================================================
#	================================================================================================
#	================================================================================================



#	109. Slices
#	some_list[start:end:step]



first_list = [1, 2, 3, 4]
first_list[1:]    # [2, 3, 4]
first_list[3:]    # [4]

first_list[-1:]    # [4]
first_list[-3:]    # [2, 3, 4]



first_list = [1, 2, 3, 4]
first_list[:2]    # [1 ,2]    end point IS NOT INCLUSIVE
first_list[:4]    # [1, 2, 3, 4]    index[4] DOES NOT EXIST in this list and it is not inclusive, thats why it returns everything and not IndexError.
first_list[1:3]    # [2, 3]

first_list[:-1]    # [1 , 2, 3]
first_list[1:-1]    # [2, 3]



first_list = [1, 2, 3, 4, 5, 6]
first_list[1:: 2]    # [2, 4, 6]
first_list[::2]    # [1, 3, 5]

first_list[1::-1]    # [2, 1]
first_list[:1:-1]    # [6, 5, 4, 3]
first_list[2::-1]    # [3, 2, 1]



string = "This is fun!"
string[::-1]    # "!nuf si sihT"
print(string[::-1])



numbers = [1, 2, 3, 4, 5]
numbers[1:3] = ['a', 'b', 'c']
print(numbers)
# [1, 'a', 'b', 'c', 4, 5]



colors = ["red", "Orange"]
print(colors[1][::-1])
# egnarO



"helllllooo"[0]    # 'h'
"helllllooo"[:4]    # 'hell'
"helllllooo"[::3]    # 'hllo'



#	================================================================================================
#	================================================================================================
#	================================================================================================



#	110. Swapping Values in Lists



names = ["James", "Michelle"]
names[0], names[1] = names[1], names[0]
print(names)
# ['Michelle', 'James']



#	================================================================================================
#	================================================================================================
#	================================================================================================



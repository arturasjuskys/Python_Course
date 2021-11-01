


#	================================================================================================
#	================================================================================================
#	================================================================================================



#	111. List Comprehension
#	112. List Comprehension With Conditional Logic
#	117. Nested Lists
#	120. Lists Recap


#	Coding Exercise 20: List Comprehension Exercises
#	Coding Exercise 21: More List Comprehension Exercises
#	Coding Exercise 22: Another List Comp Exercise
#	Coding Exercise 23: List Exercises 4
#	Coding Exercise 24: List Exercises 5
#	Coding Exercise 25: One More Nested List Comp Challenge



#	================================================================================================
#	================================================================================================
#	================================================================================================



#	111. List Comprehension
#	[ __ for __ in __ ]



nums = [1, 2, 3]
[x*10 for x in nums]	# [10, 20 ,30]    fist value(x*10) is modifier, second value(x) is temporary variable, third value is the iterable.



#	For Loop solution
numbers = [1, 2, 3, 4, 5]
doubled_numbers = []
for num in numbers:
	doubled_number = num * 2
	doubled_numbers.append(doubled_number)
print(doubled_numbers)
# [2, 4, 6, 8, 10]

#	List Comprehension solution with set variable
numbers = [1, 2, 3, 4, 5]
doubled_numbers_2 = [num * 2 for num in numbers]
print(doubled_numbers_2)

#	List Comprehension executed inside print() function
print([num * 2 for num in [1, 2, 3, 4, 5]])



name = "colt"
[char.upper() for char in name]
# ['C', 'O', 'L', 'T']



friends = ['ashley', 'matt', 'michael']
[friend[0].upper() for friend in friends]
# ['Ashley', 'Matt', 'Michael']



[num * 10 for num in range(1, 6)]
# [10, 20, 30, 40, 50]



[bool(val) for val in [0, [], '']]
# [False, False, False]



numbers = [1, 2, 3, 4, 5]
string_list = [str(num) for num in numbers]
print(string_list)
# ['1', '2', '3', '4', '5']



#	================================================================================================
#	================================================================================================
#	================================================================================================



#	112. List Conprehension with Conditional Logic



numbers = [1, 2, 3, 4, 5, 6]
evens = [num for num in numbers if num % 2 == 0]
odds = [num for num in numbers if num % 2 != 0]
# in this Comprehension code takes even numbers and multiplies them by 2, and odds numbers divide by two
rest = [num*2 if num % 2 == 0 else num/2 for num in numbers]
print(evens, odds, rest)
# [2, 4, 6] [1, 3, 5] [0.5, 4, 1.5, 8, 2.5, 12]



#    to take away values for a string or a list with a string or a list
with_vowels = "This is so much fun!"
''.join(char for char in with_vowels if char not in "aeiou")
# "Ths s s mch fn!"

print([char for char in "This is so much fun!" if char not in "aeiou"])
# ['T', 'h', 's', ' ', 's', ' ', 's', ' ', 'm', 'c', 'h', ' ', 'f', 'n', '!']

print(''.join(["cool", "dude"]))
# cooldude
print('...'.join(["cool", "dude"]))
# cool...dude



#    to check if one list items are contained in another list
answer = [val for val in [1, 2, 3, 4] if val in [3, 4, 5, 6]]
print(answer)
# [3, 4]

answer2 = [name[::-1].lower() for name in ["Elie", "Tim", "Matt"]]
print(answer2)
# ['eile', 'mit', 'ttam']



#	================================================================================================
#	================================================================================================
#	================================================================================================



#	117. Nested Lists



nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
nested_list[0][1]    # 2
nested_list[1][-1]    # 6



#    to loop through nested structures you need to use two loops, 1st loop to iterate over top structure, and second loop to iterate over structure below

nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for layer_1 in nested_list:
	for val_in_layer_1 in layer_1:
		print(val_in_layer_1)
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
[[print(val_in_layer_1) for val_in_layer_1 in layer_1] for layer_1 in nested_list]
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9



board = [[val_in_layer_1 for val_in_layer_1 in range(1, 4)] for layer_1 in range(1, 4)]
board2 = [[val_in_layer_1 for val_in_layer_1 in range(1, 5)] for layer_1 in range(1, 4)]
print(board)
print(board2)
# [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
# [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]



#    this comprehansion is to generate an 'X' to odd numbers, and 'O' to even numbers

XOXO = [["X" if num % 2 != 0 else "O" for num in range(1, 4)] for val in range(1, 4)]
print(XOXO)
# [['X', 'O', 'X'], ['X', 'O', 'X'], ['X', 'O', 'X']]



#	================================================================================================
#	================================================================================================
#	================================================================================================



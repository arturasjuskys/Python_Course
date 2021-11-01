


#	================================================================================================
#	================================================================================================
#	================================================================================================



#	Section 27: Iterators & Generators



#	265. Section Introduction and Objectives
#	266. Iterators vs. Iterables?!?!?
#	267. Writing Our Own Version of for loops
#	268. Writing a Custom Iterator
#	269. Making our Deck class Iterable
#	270. Introduction to Generators
#	273. Writing a Beat Making Generator
#	275. Testing Memory Usage With Generators
#	278. Generator Expressions AND Speed Testing!



#	Coding Exercise 84: Week Generator Exercise
#	Coding Exercise 85: yes_or_no
#	Coding Exercise 86: make_song
#	Coding Exercise 87: get_multiples
#	Coding Exercise 88: get_unlimited_multiples



#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n___   ___   ___   Iterators vs. Iterables?!?!?   ___   ___   ___\n")


#	266. Iterators vs. Iterables?!?!?



#	Iterator - an object that can be iterated upon. An object which returns data, one element at a time when next() is called on it.
#	Iterable - an object which will return an Iterator when iter() is called on it.
#	next() - is called on an iterator, the iterator returns the next item. It keeps doing so until it raises a StopIteration error.



name = "Oprah"
#next(name)    # TyperError: 'str' object is not an iterator
iter(name)    # <str_iterator object at 0x1...>
iterator_item = iter(name)
next(iterator_item)    # 'O'
next(iterator_item)    # 'p'
next(iterator_item)    # 'r'
next(iterator_item)    # 'a'
next(iterator_item)    # 'h'
#next(iterator_item)    # StopIteration



#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n___   ___   ___   267. Writing Our Own Version of for loops   ___   ___   ___\n")



#	267. Writing Our Own Version of for loops



#	Custom For Loop
def my_for(iterable, fn):
	iterator = iter(iterable)
	while True:
		try:
			item = next(iterator)
		except StopIteration:
			print("End of Iterator!")
			break
		else:
			fn(item)

def square(x):
	print(x * x)

my_for("hello", print)
# h
# e
# l
# l
# o
# End of Iterator!
my_for([1, 2, 3, 4], square)
# 1
# 4
# 9
# 16
# End of Iterator!



#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n___   ___   ___   268. Writing a Custom Iterator   ___   ___   ___\n")



#	268. Writing a Custom Iterator



class Counter:
	def __init__(self, low, high):
		self.current = low
		self.high = high

	def __iter__(self):
		return self

	def __next__(self):
		if self.current < self.high:
			num = self.current
			self.current += 1
			return num
		raise StopIteration

for x in Counter(0, 10):
	print(x)
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9


#	Result We Want
	# for n in Counter(50, 55):
	# 	print(n)
	# 50
	# 51
	# 52
	# 53
	# 54



#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n___   ___   ___   269. Making our Deck class Iterable   ___   ___   ___\n")



#	269. Making our Deck class Iterable



from random import shuffle
class Card:
	def __init__(self, value, suit):
		self.value = value
		self.suit = suit

	def __repr__(self):
		return "{} of {}".format(self.value, self.suit)

class Deck:
	def __init__(self):
		suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
		values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
		self.cards = [Card(value, suit) for suit in suits for value in values]

	def count(self):
		return len(self.cards)

	def __repr__(self):
		return "Deck of {} cards".format(self.count())

	def __iter__(self):    #    <<<===    custom __iter__()
		return iter(self.cards)

	def _deal(self, num):
		count = self.count()
		actual = min([count, num])
		if count == 0:
			raise ValueError("All cards have been dealt")
		cards = self.cards[-actual:]
		self.cards = self.cards[:-actual]
		return cards

	def deal_card(self):
		return self._deal(1)[0]

	def deal_hand(self, hand_size):
		return self._deal(hand_size)

	def shuffle(self):
		if self.count() < 52:
			raise ValueError("Only full deck can be shuffled")
		shuffle(self.cards)
		return self

my_deck = Deck()
my_deck.shuffle()

for card in my_deck:    #    <<<===    for loop with a use of custom iterator
	print(card)


for card in my_deck.cards:    #    <<<===    for loop accessing cards directly
	print(card)



#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n___   ___   ___   270. Introduction to Generators   ___   ___   ___\n")



#	270. Introduction to Generators



#	Generators are iterators, but not all iterators are generators
#	Generators can be created with generator functions
	#	Generator functions use the yield keyword
	#	Generators can be created with generator expressions

#	Function
		#	uses return
		#	returns once
		#	when invoked, returns the return value
#	Generator Function
		#	uses yield
		#	can yield multiple times
		#	when invoked, returns a generator



def count_up_to(max):
	count = 1
	while count <= max:
		yield count
		count += 1

count_up_to(5)
#<generator object count_up_to at 0x0...>
counter = count_up_to(5)
#	this will store just one value at the time, on every new line previous value is not stored and lost
next(counter)    # 1
next(counter)    # 2
next(counter)    # 3
next(counter)    # 4
next(counter)    # 5
#next(counter)    # StopIteration



counter = count_up_to(10)
for num in counter:
	print(num)
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10



#	================================================================================================
#	================================================================================================
#	================================================================================================



#	Coding Exercise 84: Week Generator Exercise



def week():
	"""
	days = week()
	next(days) # 'Monday'
	next(days) # 'Tuesday'
	next(days) # 'Wednesday'
	next(days) # 'Thursday'
	next(days) # 'Friday'
	next(days) # 'Saturday'
	next(days) # 'Sunday'
	next(days) # StopIteration
	"""
	week_days = [
		"Monday",
		"Tuesday",
		"Wednesday",
		"Thursday",
		"Friday",
		"Saturday",
		"Sunday"
	]
	for day in week_days:
		yield day



#	================================================================================================
#	================================================================================================
#	================================================================================================



#	Coding Exercise 85: yes_or_no



def yes_or_no():
	"""
	infinite loop
	gen = yes_or_no()
	next(gen) # 'yes'
	next(gen) # 'no'
	next(gen) # 'yes'
	next(gen) # 'no'
	"""
	answer = "yes"
	while True:
		yield answer
		answer = "no" if answer == "yes" else "yes"



#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n___   ___   ___   273. Writing a Beat Making Generator   ___   ___   ___\n")



#	273. Writing a Beat Making Generator



#	This will generate a list of all the values at once, to generate one alue at the time we need something different
def current_beat():
	max = 100
	nums = (1, 2, 3, 4)
	i = 0
	result = []
	while len(result) < max:
		if i >= len(nums): i = 0
		result.append(nums[i])
		i += 1
	return result

print(current_beat())
# [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]



#	This example will return one value at hte time as infinite loop
def infinite_current_beat():
	nums = (1, 2, 3, 4)
	i = 0
	while True:
		if i >= len(num): i = 0
		yield nums[i]
		i += 1



#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n___   ___   ___   Coding Exercise 86: make_song   ___   ___   ___\n")



#	Coding Exercise 86: make_song



def make_song(count = 99, beverage = "soda"):
	"""
	kombucha_song = make_song(5, "kombucha")
	next(kombucha_song) # '5 bottles of kombucha on the wall.'
	next(kombucha_song) # '4 bottles of kombucha on the wall.'
	next(kombucha_song) # '3 bottles of kombucha on the wall.'
	next(kombucha_song) # '2 bottles of kombucha on the wall.'
	next(kombucha_song) # 'Only 1 bottle of kombucha left!'
	next(kombucha_song) # 'No more kombucha!'
	next(kombucha_song) # StopIteration

	default_song = make_song()
	next(default_song) # '99 bottles of soda on the wall.'
	"""
	for count in range(count, -1, -1):
		if count > 1:
			yield f"{count} bottles of {beverage} on the wall."
			count -= 1
		elif count == 1:
			yield f"Only {count} bottle of {beverage} left!"
		else:
			yield f"No more {beverage}!"

default_song = make_song(5)
print(next(default_song))
print(next(default_song))
print(next(default_song))
print(next(default_song))
print(next(default_song))
print(next(default_song))
# 5 bottles of soda on the wall.
# 4 bottles of soda on the wall.
# 3 bottles of soda on the wall.
# 2 bottles of soda on the wall.
# Only 1 bottle of soda left!
# No more soda!



#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n___   ___   ___   275. Testing Memory Usage With Generators   ___   ___   ___\n")



#	275. Testing Memory Usage With Generators



def fib_list(max):
	nums = []
	a, b = 0, 1
	while len(nums) < max:
		nums.append(b)
		a, b = b, a + b
	return nums

print(fib_list(10))
# [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]



def fib_gen(max):
	x = 0
	y = 1
	count = 0
	while count < max:
		x, y = y, x + y
		yield x
		count += 1

for n in fib_gen(30):
	print(n)
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34
# 55
# 89
# 144
# 233
# 377
# 610
# 987
# 1597
# 2584
# 4181
# 6765
# 10946
# 17711
# 28657
# 46368
# 75025
# 121393
# 196418
# 317811
# 514229
# 832040



#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n___   ___   ___   Coding Exercise 87: get_multiples   ___   ___   ___\n")



#	Coding Exercise 87: get_multiples



def get_multiples(number = 1, count = 10):
	"""
	evens = get_multiples(2, 3)
	next(evens) # 2
	next(evens) # 4
	next(evens) # 6
	next(evens) # StopIteration

	default_multiples = get_multiples()
	"""
	for num in range(1, count + 1):
		print(number * num)

num = get_multiples()
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
num = get_multiples(2, 3)
# 2
# 4
# 6



#	================================================================================================
#	================================================================================================
#	================================================================================================



def get_unlimited_multiples(number = 1):
	"""
	sevens = get_unlimited_multiples(7)
	[next(sevens) for i in range(15)] 
	# [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105]

	ones = get_unlimited_multiples()
	[next(ones) for i in range(20)]
	# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
	"""
	next_number = number
	while True:
		yield next_number
		next_number += number



#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n___   ___   ___   278. Generator Expressions AND Speed Testing!   ___   ___   ___\n")



#	278. Generator Expressions AND Speed Testing!



#	You can also create generators from generator expressopns
#	Generator expresions look a lot like list comprehensions
#	Generator expressions use () instead of []



def nums():
	for num in range(1, 10):
		yield num
g = nums()
print(g)
# <generator object nums at 0x0...>    <<<===    it came form nums variable
next(g)    # 1
next(g)    # 2
next(g)    # 3
next(g)    # 4
next(g)    # 5
next(g)    # 6
#            ...



g2 = (num for num in range(1, 10))
print(g)
# <generator object <genexpr> at 0x0...>    <<<===     ir came from Generator Expresion
next(g2)    # 1
next(g2)    # 2
next(g2)    # 3
next(g2)    # 4
next(g2)    # 5
next(g2)    # 6
#            ...



import time
gen_start_time = time.time()
print(sum(n for n in range(50000000)))
gen_time = time.time() - gen_start_time


list_start_time = time.time()
print(sum([n for n in range(50000000)]))
list_time = time.time() - list_start_time

print(f"generator expresion took: {gen_time} to run 50 000 000")
print(f"list comprehension took: {list_time} to run 50 000 000")
# generator expresion took: 5.6446990966796875 to run 50 000 000
# list comprehension took: 5.23059606552124 to run 50 000 000



#	================================================================================================
#	================================================================================================
#	================================================================================================






#	================================================================================================
#	================================================================================================
#	================================================================================================



#	Section 28: Testing with Python



#	293. Section Introduction
#	294. Why Test?
#	295. Assertions
#	296. Doctests
#	297. Doctests Exercise
#	298. Introduction to Unittest
#	299. Other Types of Assertions
#	300. Before and after hooks
#	301. Testing Card/Deck Exercise
#	302. Testing Card/Deck Exercise Intro
#	303. Testing Card/Deck Solution



#	================================================================================================
#	================================================================================================
#	================================================================================================
#print(f"\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 294. Why Test? \n")



#	294. Why Test?



#	Reduce bugs in existing code
#	Ensure bugs that are fixed stay fixed
#	Ensure that new features don't break old ones
#	Ensure that cleaning up code does't introduce new bugs
#	Makes development more fun!



#	Test Driven Development

#	Development begins by writing tests
#	Once tests are written, write code to make tests pass
#	Once tests pass, a feature is considered complete



#	Red, Green, Refactor

#	Red - Write a test that fails
#	Green - Write the minimal amount of code necessary to make the test pass
#	Refactor - Clean up the code, while ensuring that tests still pass



#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 295. Assertions \n")



#	295. Assertions



#	We can make simple assertions with the assert keyword
#	assert accepts an expresion
#	Returns None if the exression is truthy
#	Raises an EssartionError if the expresion is falsy
#	Accepts an optional error message as a second argument



#	Assertions Examples

def add_positive_numbers(x, y):
	assert x > 0 and y > 0, "Both numbers must be positive!"
	print(x + y)

add_positive_numbers(1, 1)    # 2
#add_positive_numbers(1, -1)    # AssertionError: Both numbers must be positive!



def eat_junk(food):
	assert food in [
		"pizza",
		"ice cream",
		"candy",
		"fried butter",
	], "food must be a junk food!"
	return f"NOM NOM NOM I am eating {food}"
food = input("Enter a food please: ")
print(eat_junk(food))



#	Assertion Warning

		#	If a Python file is run with -O (letter o not a number zero) flag, assertion will not be evaluated!
				# If you run .py file over console: python -O 001_test.py, like so then the file will be ignoring all assert statments.



#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 296. Doctests \n")



#	296. Doctests



#	We can write tests for functions inside of the docstring
#	Write code that looks like it's inside of a REPL
def add(x, y):
	"""add together x and y

	>>> add(1, 2)
	3

	>>> add(8, "hi")
	Traceback (most recent call last):
		...
	TypeError: unsupported operand type(s) for +: 'int' and 'str'
	"""
	return x + y

			#	To execute the test use comand promt:
			#	python -m doctest -v doctest_demo.py



def double(values):
	""" doubles the values in a list

	>>> double([1, 2, 3, 4])
	[2, 4, 6, 8]

	>>> double(['a', 'b', 'c'])
	['aa', 'bb', 'cc']

	>>> double([])
	[]

	>>> double([True, None])
	Traceback (most recent call last):
		...
	TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
	"""
	return [2 * element for element in values]



#	This example shows that if you want to test for string values in answers you need to use ' ' NOT " ", otherwise you will fail the test
def say_hi1():
	"""
	>>> say-hi1()
	"hi"    #    <<<===    this will fail the test because of " " NOT ' '
	"""

def say_hi2():
	"""
	>>> say_hi2()
	'hi'
	"""
	return "hi"



#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 298. Introduction to Unittest \n")



#	298. Introduction to Unittest



#	Unit testing

		#	Test smaller parts of an application in isolation (e.g. units)
		#	Good candidates for unit testing: individual classes, modules, or functions
		#	Bad candidates for unit testing: an entire application, dependancies across several classes or modules



#	unittest

		#	Python comes with a built-in module called unittest
		#	You can write unit tests encapsulated as classes that inherit from unittest.TestCase
		#	This inheritance gives you access to many assertion helpers that let you test the behavior of your functions
		#	You can run tests by calling unittest.main()

#	activities.py
#def eat(food, is_healthy):
#	pass

#def nap(num_hours):
#	pass

#	test.py
import unittest
from activities import eat, nap, is_funny, laugh

class ActivityTests(unittest.TestCase):
	def test_eat_healthy(self):
		"""eat should have a positive message for healthy eating"""
		self.assertEqual(
			eat("broccoli", is_healthy = True),
			"I'm eating broccoli, because my body is a temple"
		)
	def test_eat_unhealthy(self):
		"""eat should indicate you've given up for eating unhealthy"""
		self.assertEqual(
			eat("pizza", is_healthy = False),
			"I'm eating pizza, because YOLO"
		)
	def test_eat_healthy_boolean(self):
		"""is_healthy must be a boolean value"""
		with self.assertRaises(ValueError):
			eat("pizza", is_healthy = "who cares?")
	def test_short_nap(self):
		"""short naps should be refreshing"""
		self.assertEqual(
			nap(1),
			"I'm feeling refreshed after my 1 hour nap"
		)
	def test_long_nap(self):
		"""long naps should be discouraging"""
		self.assertEqual(
			nap(3),
			"Ugh I overslept. I didn't meant to nap for 3 hours!"
		)
	def test_is_funny_tim(self):
		self.assertEqual(is_funny("tim"), False)
#			self.assertFalse(is_funny("tim"), "tim should not be funny")
	def test_is_funny_anyone_else(self):
		self.assertTrue(is_funny("blue"), "blue should be funny")
		self.assertTrue(is_funny("tammy"), "tammy should be funny")
		self.assertTrue(is_funny("sven"), "sven should be funny")
	def test_laugh(self):
		#	testing for random thing using tuple as a data type
		self.assertIn(laugh(), ("lol", "haha", "tehehe"))

if __name__ == "__main__":
	unittest.main()

#		^^^^^^^^^		END OF TEST CODE



#	Commenting Tests

def thing():
	pass
def another_thing():
	pass
class SomeTests(unittest.TestCase):
	def first_test(self):
		"""testing a thing"""
		self.assertEqual(thing(), "something")
	def second_test(self):
		"""test another thing"""
		self.assertEqual(another_thing(), "something else")
#			To see comments, run
#			python NAME_OF_TEST_FILE.py -v



#	Testing for Errors

class SomeTests(unittest.TestCase):
	def testing_for_error(self):
		"""testing for an error"""
		with self.assertRaise(IndexError):
			l = [1, 2, 3]
			l[100]




#	================================================================================================
#	================================================================================================
#	================================================================================================
#print(f"\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 299. Other Types of Assertions \n")



#	299. Other Types of Assertions



#	Types of Assertions

		#	self.assertEqual(x, y)
		#	self.assertNotEqual(x, y)
		#	self.assertTrue(x)
		#	self.assertFalse(x)
		#	self.assertIsNone(x)
		#	self.assertIsNotNone(x)
		#	self.assertIn(x)
		#	self.assertNotIn(x)
		#	... and more







#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 300. Before and after hooks \n")



#	300. Before and after hooks



#	setUp and tearDown

		#	For larger applications, you may want similar application state before running tests
		#	setUp runs before each test method
		#	tearDown runs after each test method
		#	Common use cases: adding/removing data form a test database, creating instances of a class



class SomeTests(unittest.TestCase):
	def setUp(self):
		#	do setup here
		pass
	def test_first(self):
		#	setUp runs before
		#	tearDown runs after
		pass
	def sets_second(self):
		#	setUp runs before
		#	tearDown runs after
		pass
	def tearDown(self):
		#	do teardown here
		pass



import unittest
from activities import Robot
class RobotTests(unittest.TestCase):
	def setUp(self):
		self.mega_man = Robot("Mega Man", battery = 50)
	def test_charge(self):
		self.mega_man.charge()
		self.assertEqual(self.mega_man.battery, 100)
	def test_say_name(self):
		self.assertEqual(
			self.mega_man.say_name(),
			"BEEP BOOP BEEP BOOP. I AM MEGA MAN")
		self.assertEqual(self.mega_man.battery, 49)

if __name__ == "__name__":
	unittest.main()



#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 303. Testing Card/Deck Solution \n")



#	303. Testing Card/Deck Solution



from activities import Card
from activities import Deck
import unittest

class CardTests(unittest.TestCase):
	def setUp(self):
		self.card = Card("Hearts", "A")
	def test_init(self):
		"""cards should have a suit and a value"""
		self.assertEqual(self.card.suit, "Hearts")
		self.assertEqual(self.card.value, "A")
	def test_repr(self):
		"""repr should return a string of the form 'VALUE of SUIT'"""
		self.assertEqual(repr(self.card), "A of Hearts")
class DeckTests(unittest.TestCase):
	def setUp(self):
		self.deck = Deck()
	def test_init(self):
		"""decks should have a cards attribute, which is a list"""
		self.assertTrue(isinstance(self.deck.cards, list))
		self.assertEqual(len(self.deck.cards), 52)
	def test_repr(self):
		"""repr should return a string of the form 'Deck of COUNT cards.'"""
		self.assertEqual(repr(self.deck), "Deck of 52 cards.")
	def test_count(self):
		"""count should return a count of the number of cards in the deck"""
		self.assertEqual(self.deck.count(), 52)
		self.deck.cards.pop()
		self.assertEqual(self.deck.count(), 51)
	def test_deal_sufficient_cards(self):
		"""_deal should deal the number of cardss specified, """
		cards = self.deck._deal(10)
		self.assertEqual(len(cards), 10)
		self.assertEqual(self.deck.count(), 42)
	def test_deal_insufficient_cards(self):
		"""_deal should deal the number of cards left in the deck"""
		cards = self.deck._deal(100)
		self.assertEqual(len(cards), 52)    #    <<<===    this checks that _deal took all 52 cards to a variable cards
		self.assertEqual(self.deck.count(), 0)
	def test_deal_no_cards(self):
		"""_deal should throw a ValueError if the deck is empty"""
		self.deck._deal(self.deck.count())    #    <<<===    this should deal all the cards that are in the deck, and drain the deck
		with self.assertRaises(ValueError):
			self.deck._deal(1)
	def test_deal_cards(self):
		"""deal_cards should deal a single card form the deck"""
		card = self.deck.cards[-1]
		dealt_card = self.deck.deal_card()
		self.assertEqual(card, dealt_card)
		self.assertEqual(self.deck.count(), 51)
	def test_deal_hand(self):
		"""deal_hand should deal the number of cards passed"""
		cards = self.deck.deal_hand(20)
		self.assertEqual(len(cards), 20)
		self.assertEqual(self.deck.count(), 32)
	def test_shuffle_full_deck(self):
		"""shuffle should shuffle the deck if the deck is full"""
		cards = self.deck.cards[:]
		self.deck.shuffle()
		self.assertNotEqual(cards, self.deck.cards)
		self.assertEqual(self.deck.count(), 52)
	def test_shuffle_not_full_deck(self):
		"""shuffle should throw a ValueError of the deck """
		self.deck._deal(1)
		with self.assertRaises(ValueError):
			self.deck.shuffle()
if __name__ == "__main__":
	unittest.main()





#	================================================================================================
#	================================================================================================
#	================================================================================================



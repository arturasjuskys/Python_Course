from random import choice

def eat(food, is_healthy):
	if not isinstance(is_healthy, bool):
		raise ValueError("is_healthy must be a boolean value")
	ending = "because YOLO"
	if is_healthy:
		ending = "because my body is a temple"
	return f"I'm eating {food}, {ending}"
	
def nap(num_hours):
	if num_hours >= 2:
		return f"Ugh I overslept. I didn't meant to nap for {num_hours} hours!"
	else:
		return f"I'm feeling refreshed after my {num_hours} hour nap"

def is_funny(person):
	if person is "tim": return False
	return True

def laugh():
	return choice(("lol", "haha", "tehehe"))



#	================================================================================================
#	================================================================================================
#	================================================================================================



class Robot:
	def __init__(self, name, battery = 100, skills = []):
		self.name = name
		self.battery = battery
		self.skills = skills
	def charge(self):
		self.battery = 100
		return self
	def say_name(self):
		if self.battery > 0:
			self.battery -= 1
			return f"BEEP BOOP BEEP BOOP. I AM {self.name.upper()}"
		return "Low power. Please charge and try again"
	def learn_skill(self, new_skill, cost_to_learn):
		if self.battery >= cost_to_learn:
			self.battery -= cost_to_learn
			self.skills.append(new_skill)
			return f"WOAH. I KNOW {new_skill.upper()}"
		return "Insufficient battery. Please charge and try again"



#	================================================================================================
#	================================================================================================
#	================================================================================================



from random import shuffle
class Card:
	def __init__(self, suit, value):
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
		return "Deck of {} cards.".format(self.count())

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






#	================================================================================================
#	================================================================================================
#	================================================================================================



#	Section 24: Object Oriented Programming



#	232. Section Introduction and Objectives
#	233. Defining Classes and Objects
#	234. Abstaction and Encalsulation
#	235. Creating Classes and Instances
#	237. The __int__ method
#	239. Underscores: Dunder Methods, Name Mangling, and More!
#	240. Adding Instance Methods
#	242. Introducing Class Attributes
#	243. Class Attributes Continued
#	245. Class Methods
#	246. A More Advance Class Method Example
#	The __repr__ method



#	Coding Exercise 76: World's Simplest Class Exercise
#	Coding Exercise 77: Your First Class - Social Media Comments
#	Coding Exercise 78: Bank Account OOP Exercise
#	Coding Exercise 79: Chicken Coop Exercise



#	================================================================================================
#	================================================================================================
#	================================================================================================



#	233. Defining Classes and Objects



#	What is OOP?
#	Object oriented programming is a method of programming that attempts to model some process or thing in the world as a CLASS or OBJECT

#	class - a blueprint for objects. Classes can contain methods (functions) and attributes (similar to keys in a dict).
#	instance - objects that are constructed from a class blueprint that contains their class's methods and properties.



#	================================================================================================
#	================================================================================================
#	================================================================================================



#	234. Abstaction and Encalsulation



#	Encapsulation - the grouping of public and private attributes and methods into a programming class, making abstaction possible

#	Abstraction - exposing only "relavant" data in a class interface, hiding private attributes and methods (aka the inner workings) from users



#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n___   ___   ___   235. Creating Classes and Instances   ___   ___   ___\n")



#	235. Creating Classes and Instances



#	Convension is to use Upper Camel Cases
class User:
	pass    #    <<<===    this allows to keep empty class, without breaking the code
class PockerDeck:
	pass



user1 = User()
print(user1)
# <__main__.User object at 0x...>
print(type(User()))
# <class '__main__.User'>



#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n___   ___   ___   237. The __int__ method   ___   ___   ___\n")



#	237. The __int__ method



class Vehicle:
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year



class User:
	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		self.age = age

user1 = User("Joe", "Smith", 68)
user2 = User("Blanca", "Lopez", 41)
print(user1)
print(user1.first, user1.last)
print(user2.first, user2.last)
# <__main__.User object at 0x...>
# Joe Smith
# Blanca Lopez



#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n___   ___   ___   239. Underscores: Dunder Methods, Name Mangling, and More!   ___   ___   ___\n")



#	239. Underscores: Dunder Methods, Name Mangling, and More!



#	_name    #    <<<===    is meant to be used inside this class and not outside of it, private variable (even thow python technicaly dont have private attributes)
#	__name    #    <<<===    Name Mangling by Python, to make this attribute unique to this class but not other classes
#	__name__


class Person:
	def __init__(self):
		self.name = "Tony"
		self._secret = "hi!"
		self.__msg = "I like turtles!"
		self.__lol = "HAHAHA"
	def doorman(self, guess):
		if guess == self._secret:
			return "Let them in!"

p = Person()

print(p.name)
print(p._secret)    #    <<<===    this is a private variable (even thow python technicaly dont have private attributes)
#print(p.__msg)    #    AttributeError: ...
print(dir(p))
#['_Person__msg', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_secret', 'doorman', 'name']
print(p._Person__msg)
print(p._Person__lol)
# I like turtles
# HAHAHA



#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n___   ___   ___   240. Adding Instance Methods   ___   ___   ___\n")



#	240. Adding Instance Methods



class User:
	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		self.age = age

	def full_name(self):
		return f"{self.first} {self.last}"

	def initials(self):
		return f"{self.first[0]}.{self.last[0]}."

	def likes(self, thing):
		return f"{self.first} likes {thing}"
	
	def is_senior(self):
		return self.age >= 65
	
	def birthday(self):
		self.age += 1
		return f"Happy {self.age}th, {self.first}"
	
	def say_hi(self):
		print("HELLO!")
	

user1 = User("Joe", "Smith", 68)
user2 = User("Blanca", "Lopez", 41)
print(user2.full_name())
print(user2.initials())
print(user1.likes("Ice Cream"))
# Blanca Lopez
# B.L.
# Joe likes Ice Cream

print(user1.is_senior())
print(user2.age)
print(user2.birthday())
print(user2.age)
# True
# 41
# Happy 42th, Blanca
# 42

user1.say_hi()
# HELLO!



#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n___   ___   ___   Coding Exercise 78: Bank Account OOP Exercise   ___   ___   ___\n")



#	Coding Exercise 78: Bank Account OOP Exercise



# Define Bank Account Below:
class BankAccount():
	"""
	acct = BankAccount("Darcy")
	acct.owner #Darcy
	acct.balance #0.0
	acct.deposit(10)  #10.0
	acct.withdraw(3)  #7.0
	acct.balance .  #7.0
	"""

	def __init__(self, name):
		self.owner = name
		self.balance = 0.0

	def balance(self):
		return self.balance
  
	def deposit(self, amount):
		self.balance += amount
		return self.balance
  
	def withdraw(self, amount):
		self.balance -= amount
		return self.balance
	

acct = BankAccount("Joe")
#print(user1.balance)
print(acct.owner)
print(acct.balance)
print(acct.deposit(3))
print(acct.withdraw(3))



#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n___   ___   ___   242. Introducing Class Attributes   ___   ___   ___\n")



#	242. Introducing Class Attributes



class User:
	
	active_users = 0
	
	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		self.age = age
		User.active_users += 1
	
	def logout(self):
		User.active_users -= 1
		return f"{self.first} has logged uot"

	def full_name(self):
		return f"{self.first} {self.last}"

	def initials(self):
		return f"{self.first[0]}.{self.last[0]}."

	def likes(self, thing):
		return f"{self.first} likes {thing}"
	
	def is_senior(self):
		return self.age >= 65
	
	def birthday(self):
		self.age += 1
		return f"Happy {self.age}th, {self.first}"
	
	def say_hi(self):
		print("HELLO!")

print(User.active_users)
user1 = User("Joe", "Smith", 68)
user2 = User("Blanca", "Lopez", 41)
print(User.active_users)
print(user2.logout())
print(User.active_users)
# 0
# 2
# Blanca has logged out
# 1



#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n___   ___   ___   243. Class Attributes Continued   ___   ___   ___\n")



#	243. Class Attributes Continued



class Pet:
	allowed = ["cat", "dog", "fish", "rat"]    #    <<<===    this can be used for analytical purposes or validating new data
	
	def __init__(self, name, species):
		if species not in Pet.allowed:
#		if species not in self.allowed:    #    <<<===    Alternative
			raise ValueError(f"You can't have a {species} pet!")
		self.name = name
		self.species = species
	
	def set_species(self, species):
		if species not in Pet.allowed:
			raise ValueError(f"You can't have a {species} pet!")
		self.species = species
	
cat = Pet("Blue", "cat")
dog = Pet("Wyatt", "dog")



#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n___   ___   ___   Coding Exercise 79: Chicken Coop Exercise   ___   ___   ___\n")



#	Coding Exercise 79: Chicken Coop Exercise



class Chicken:
	total_eggs = 0
	def __init__(self, name, species):
		self.name = name
		self.species = species
		self.eggs = 0
	def lay_egg(self):
		self.eggs += 1
		Chicken.total_eggs += 1
		return self.eggs

c1 = Chicken(name = "Alice", species = "Partridge Silkie")
c2 = Chicken(name = "Amelia", species = "Speckled Sussex")
Chicken.total_eggs # 0
c1.lay_egg() # 1
Chicken.total_eggs # 1
c2.lay_egg() # 1
c2.lay_egg() # 2
Chicken.total_eggs #3
	



#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n___   ___   ___   245. Class Methods   ___   ___   ___\n")



#	245. Class Methods



class Person():
	# . . .
	@classmethod    #    <<<===    decorator
	def from_csv(cls, filename):
		return cls(*params)    # this is the same as calling Person(*params)
#Person.from_csv(my_csv)



#	classmethod to display active users
class User:
	active_users = 0
	@classmethod
	def display_active_users(cls):
		return f"There are curently {cls.active_users} active users"
		
	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		self.age = age
		User.active_users += 1
	def logout(self):
		User.active_users -= 1
		return f"{self.first} has logged uot"
	def full_name(self):
		return f"{self.first} {self.last}"
	def initials(self):
		return f"{self.first[0]}.{self.last[0]}."
	def likes(self, thing):
		return f"{self.first} likes {thing}"
	def is_senior(self):
		return self.age >= 65
	def birthday(self):
		self.age += 1
		return f"Happy {self.age}th, {self.first}"
	def say_hi(self):
		print("HELLO!")
user1 = User("Joe", "Smith", 68)
user2 = User("Blanca", "Lopez", 41)
user1.display_active_users()
print(User.display_active_users())
user3 = User("Joe", "Smith", 68)
user4 = User("Blanca", "Lopez", 41)
print(User.display_active_users())
# There are curently 2 active users
# There are curently 4 active users



#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n___   ___   ___   246. A More Advance Class Method Example   ___   ___   ___\n")



#	246. A More Advance Class Method Example



#	convert data types form string to new User
class User:
	active_users = 0
	@classmethod
	def display_active_users(cls):
		return f"There are curently {cls.active_users} active users"
	@classmethod
	def from_string(cls, data_str):
		first, last, age = data_str.split(",")
		return cls(first, last, int(age))    #    <<<===    this will pass this new data to new user class, because @classmethod belongs to class itself nad it is not an instance like other def(functions/instances)
		
	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		self.age = age
		User.active_users += 1
	def logout(self):
		User.active_users -= 1
		return f"{self.first} has logged uot"
	def full_name(self):
		return f"{self.first} {self.last}"
	def initials(self):
		return f"{self.first[0]}.{self.last[0]}."
	def likes(self, thing):
		return f"{self.first} likes {thing}"
	def is_senior(self):
		return self.age >= 65
	def birthday(self):
		self.age += 1
		return f"Happy {self.age}th, {self.first}"
	def say_hi(self):
		print("HELLO!")
tom = User.from_string("Tom, Jones, 89")    #    <<<===    string convertion
print(tom.first)
print(tom.full_name())
print(tom.birthday())
# Tom
# Tom Jones
# Happy 90th, Tom



#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n___   ___   ___   247. The __repr__ method   ___   ___   ___\n")



#	247. The __repr__ method



#	The __repr__ method is one of several ways to provide a nicer string representation:
class Human:
	def __init__(self, name = "somebody"):
		self.name = name
	def __repr__(self):
		return self.name
dude = Human()
print(dude)
# somebody
colt = Human(name = "Colt Steele")
print(f"{colt} is totally rad (probably)")
# Colt Steele is totally rad (probably)

#	There are also several other dunders to return classes in string formats (notably _str__ and __foramt__), and choosing one is a bit complicated!



class User:
	active_users = 0
	@classmethod
	def display_active_users(cls):
		return f"There are curently {cls.active_users} active users"
	@classmethod
	def from_string(cls, data_str):
		first, last, age = data_str.split(",")
		return cls(first, last, int(age))
		
	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		self.age = age
		User.active_users += 1
	def __repr__(self):
		return f"{self.first} is {self.age}"    #    <<<===    this is custome representation of User class when print()

	def logout(self):
		User.active_users -= 1
		return f"{self.first} has logged uot"
	def full_name(self):
		return f"{self.first} {self.last}"
	def initials(self):
		return f"{self.first[0]}.{self.last[0]}."
	def likes(self, thing):
		return f"{self.first} likes {thing}"
	def is_senior(self):
		return self.age >= 65
	def birthday(self):
		self.age += 1
		return f"Happy {self.age}th, {self.first}"
	def say_hi(self):
		print("HELLO!")
tom = User.from_string("Tom, Jones, 89")    #    <<<===    string convertion
print(tom)



#	================================================================================================
#	================================================================================================
#	================================================================================================



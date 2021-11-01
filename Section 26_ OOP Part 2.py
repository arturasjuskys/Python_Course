


#	================================================================================================
#	================================================================================================
#	================================================================================================



#	Section 26: OOP Part 2



#	253. Inheritance and Objectives
#	254. All About Properties
#	255. Introduction to Super()
#	256. Inheritance Examples: User and Moderator
#	258. The Crazy World of Multiple Inheritance
#	259. WTF is Method Resolution Order(MRO)
#	261. Polymorphism Introduction
#	262. Special __magic__ methods
#	263. Making a Grumpy Dictionary - Overriding Dict



#	Coding Exercise 81: Roleplaying Game Classes
#	Coding Exercise 82: MRO Genetics
#	Coding Exercise 83: Special Methods Train



#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n___   ___   ___   253. Inheritance and Objectives   ___   ___   ___\n")


#	253. Inheritance and Objectives



#	A key freature of OOP is the ability to define class which inherits from another class (a "base" or "parent" class).
#	In Python, inheritance works by passing the parent class as an argument to the definition of a child class:
class Animal:
	cool = True
	def make_sound(self, sound):
		return f"this animal says {sound}"


class Cat(Animal):
	pass
	
gandalf = Cat()
print(gandalf.make_sound("meow"))
print(gandalf.cool)
# Meow
# True



#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n___   ___   ___   254. All About Properties   ___   ___   ___\n")



#	254. All About Properties



class Human:
	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		if age >= 0:
			self._age = age
		else:
			self._age = 0
	def get_age(self):
		return self._age
	def set_age(self, new_age):
		if new_age >= 0:
			self._age = new_age
		else:
			self._age = 0

jane = Human("Jane", "Goodall", -100)
print(jane.get_age())
# 0
jane.set_age(40)
print(jane.get_age())
# 40



class Human:
	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		if age >= 0:
			self._age = age
		else:
			self._age = 0
#	def get_age(self):
#		return self._age
#	def set_age(self, new_age):
#		if new_age >= 0:
#			self._age = new_age
#		else:
#			self._age = 0
	@property
	def age(self):
		return self._age
	@age.setter
	def age(self, value):
		if value >= 0:
			self._age = value
		else:
			raise ValueError("Age can't be negative")
	@property
	def full_name(self):
		return f"{self.first} {self.last}"
		
jane = Human("Jane", "Smith", 34)
print(jane.age)
# 34
jane.age = 20
print(jane.age)
#20
#jane.age = -100
#print(jane.age)
# ValueError: ...
print(jane.full_name)
# Jane Smith
print(jane.__dict__)
# {'first': 'Jane', 'last': 'Smith', '_age': 20}



#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n___   ___   ___   255. Introduction to Super()   ___   ___   ___\n")



#	255. Introduction to Super()



class Animal:
	def __init__(self, name, species):
		self.name = name
		self.species = species
	def __repr__(self):
		return f"{self.name} is a {self.species}"
	def make_sound(self, sound):
		print(f"this animal says {sound}")

class Cat(Animal):
	def __init__(self, name, species, breed, toy):
		super().__init__(name, species)
#	Alternative code
#		Animal.__init__(self, name, species)
		self.breed = breed
		self.toy = toy

blue = Cat("Blue", "Cat", "Scottish Fold", "String")
print(blue)
print(blue.species)
print(blue.toy)
# Blue is a Cat
# Cat
# String




#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n___   ___   ___   256. Inheritance Examples: User and Moderator   ___   ___   ___\n")



#	256. Inheritance Examples: User and Moderator



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
		return f"{self.first} is {self.age}"

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


class Moderator(User):
	total_moderators = 0
	def __init__(self, first, last, age, community):
		super().__init__(first, last, age)
		self.community = community
		Moderator.total_moderators += 1
	
	@classmethod
	def display_active_moderators(cls):
		return f"There are currently {cls.total_moderators} active moderators"
	
	def remove_post(self):
		return f"{self.full_name} removed a post from the {self.community} community "

print(User.display_active_users())
u1 = User("Tom", "Garcia", 35)
u2 = User("Tom", "Garcia", 35)
u3 = User("Tom", "Garcia", 35)
print(User.display_active_users())
jasmine1 = Moderator("Jasmine", "O'conner", 61, "Piano")
jasmine2 = Moderator("Jasmine", "O'conner", 61, "Piano")
print(User.display_active_users())
print(Moderator.display_active_moderators())
# There are currently 0 active users
# There are currently 3 active users
# There are currently 5 active users
# There are currently 2 active moderators
print(jasmine1.full_name())
print(jasmine1.community)
# Jasmine O'conner
# Piano



#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n___   ___   ___   258. The Crazy World of Multiple Inheritance   ___   ___   ___\n")



#	258. The Crazy World of Multiple Inheritance



class Aquatic:
	def __init__(self, name):
		self.name = name
		
	def swim(self):
		return f"{self.name} is swimming"
	
	def greet(self):
		return f"I am {self.name} of the sea!"


class Ambulatory:
	def __init__(self, name):
		self.name = name
	
	def walk(self):
		return f"{self.name} is walking!"
	
	def greet(self):
		return f"I am {self.name} of the land!"


class Penguin(Ambulatory, Aquatic):    #    <<<===    the order of passed arguments defines the order of inheritance.
	def __init__(self, name):
		super().__init__(name = name)


jaws = Aquatic("Jaws")
lassie = Ambulatory("Lassie")
captain_cook = Penguin("Captain Cook")

print(captain_cook.swim())
print(captain_cook.walk())
print(captain_cook.walk())
# Captain Cook is swimming
# Captain Cook is walking
# I am Captain Cook of the land!
print(f"captain_cook is instance of Penguin: {isinstance(captain_cook, Penguin)}")
print(f"captain_cook is instance of Aquatic: {isinstance(captain_cook, Aquatic)}")
print(f"captain_cook is instance of Ambulatory: {isinstance(captain_cook, Ambulatory)}")
# captain_cook is instance of Penguin: True
# captain_cook is instance of Aquatic: True
# captain_cook is instance of Ambulatory: True



#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n___   ___   ___   259. WTF is Method Resolution Order(MRO)   ___   ___   ___\n")



#	259. WTF is Method Resolution Order(MRO)



#	Whenever you create a class, Python sets a Method Resolution Order, or MRO, for that class, which is the order in which Python will look for methods on instances of that class.
#	You can programmatically reference the MRO three ways:
		#	__mro__ atribute on the class
		#	use the mro() method on the class
		#	use the built-in help(cls) method


class A:
	def do_something(self):
		print("Method Defned In: A")

class B(A):
	def do_something(self):
		print("Method Defned In: B")

class C(A):
	def do_something(self):
		print("Method Defned In: C")

class D(B, C):
	def do_something(self):
		print("Method Defned In: D")

thing = D()
print(thing.do_something())


		#        A
		#     /    \
		#   B      C
		#     \    /
		#        D
		#	D, B, C, A, Object


# Method Defined In: D
print(D.__mro__)
# (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object>)
print(D.mro())
#[<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object>]
print(help(D))
		#Help on class D in module __main__:

		#class D(B, C)
		# |  Method resolution order:
		# |      D
		# |      B
		# |      C
		# |      A
		# |      builtins.object
		# |
		# |  Methods defined here:
		# |
		# |  do_something(self)
		# |
		# |  ----------------------------------------------------------------------
		# |  Data descriptors inherited from A:
		# |
		# |  __dict__
		# |      dictionary for instance variables (if defined)
		# |
		# |  __weakref__
		# |      list of weak references to the object (if defined)



#	================================================================================================
#	================================================================================================
#	================================================================================================



#	Coding Exercise 82: MRO Genetics



class Mother:
    def __init__(self):
        self.eye_color = "brown"
        self.hair_color = "dark brown"
        self.hair_type = "curly"

class Father:
    def __init__(self):
        self.eye_color = "blue"
        self.hair_color = "blond"
        self.hair_type = "straight"

class Child(Mother, Father):
    pass



#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n___   ___   ___   261. Polymorphism Introduction   ___   ___   ___\n")



#	261. Polymorphism Introduction



#	A key principle in OOP is the idea of polymorphism - an object can take on many (poly) forms (morph)
#	1. The same class method working in a similar way for different classes
		#	Cat.speak()           # meow
		#	Dog.speak()         # woof
		#	Human.speak()    # yo

#	2. The same operation works for different kinds of objects
		#	sample_list = [1, 2, 3]
		#	sample_tuple = (1, 2, 3)
		#	sample_string = "awesome"
		
		#	len(sample_list)
		#	len(sample_tuple)
		#	len(sample_string)



#	1. Example - Polymorphism & Inheritance
#	If not overriden by other class this will return an error, like with class of Fish
class Animal:
	def speak(self):
		raise NotImplementedError("Subclass needs to implement this method")

class Dog(Animal):
	def speak(self):
		return "woof"

class Cat(Animal):
	def speak(self):
		return "meow"

class Fish(Animal):
	pass

d = Dog()
print(d.speak())
f = Fish()
#print(f.speak())
# woof
# NotImplementedError: ...



#	2. Example
	
8 + 2    # 10
"8" + "2"    # 82




#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n___   ___   ___   262. Special __magic__ methods   ___   ___   ___\n")



#	262. Special __magic__ methods



8 + 2    # 10
"8"  + "2"    # 82
#    ^^^    ^^^
#	The + operator is shorthand for a special method called __add__() that gets called on the first operand.
#	If the first (left) operand is an instance of int, __add__() does mathematical addition. If it's a string, it does string concatination.



#	Therefore, you can declare special methods on your own classes to mimic the behavior of built-in objects, like so using __len__:
class Human:
	def __init__(self, height):
		self.height = height    # in inches
	
	def __len__(self):
		return self.height

Colt = Human(60)
print(len(Colt))
# 60



#	String Representation Example



class Human:
	def __init__(self, name = "somebody"):
		self.name = name
	
	def __repr__(self):
		return self.name

dude = Human()
print(dude)
# somebody



#	This example will __add__() two Human() together and create a new Human("last_name from 1st Human()", "age = 0")
class Human:
	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		self.age = age
	
	def __repr__(self):
		return f"Human named {self.first} {self.last} aged {self.age}"

	def __len__(self):
		return self.age
	
	def __add__(self, other):
		if isinstance(other, Human):    #    this will check if this instance is Human
			return Human(first = "Newborn", last = self.last, age = 0)
		return "TypeError: You can't add that!"
	
	def __mul__(self, other):
		#	Cloning method
		if isinstance(other, int):
			return [self for i in range(other)]
		return "Can't Multiply"
	
j = Human("Jenny", "Larsen", 47)
k = Human("Kevin", "Jones", 49)
print(j)
# Human named Jenny Larsen aged 47
print(len(j))
# 47
print(j + k)    #    <<<===    this does the new class of __add__()
# Human named Newborn Larsen aged 0
print(j + 2)
# TypeError: You can't add that
print(j * 2)
# [Human named Jenny Larsen aged 47, Human named Jenny Larsen aged 47]
triplets = j * 3
triplets[1].first = "Jessica"
print(triplets)    #    <<<===    in this instance all three new objects are references to the same class, thus when trying to change one name we end up changing all names. To change one name we need to import copy built-in module.
# [Human named Jessica Larsen aged 47, Human named Jessica Larsen aged 47, Human named Jessica Larsen aged 47]


from copy import copy
class Human:
	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		self.age = age
	
	def __repr__(self):
		return f"Human named {self.first} {self.last} aged {self.age}"

	def __len__(self):
		return self.age
	
	def __add__(self, other):
		if isinstance(other, Human):    #    this will check if this instance is Human
			return Human(first = "Newborn", last = self.last, age = 0)
		return "TypeError: You can't add that!"
	
	def __mul__(self, other):
		#	Cloning method
		if isinstance(other, int):
			return [copy(self) for i in range(other)]    #    <<<===    here we need to use copy(self) to make real copies of Human not references
		return "Can't Multiply"
	
j = Human("Jenny", "Larsen", 47)
k = Human("Kevin", "Jones", 49)
triplets2 = j * 3
triplets2[1].first = "Jessica"
print(triplets2)
# [Human named Jenny Larsen aged 47, Human named Jessica Larsen aged 47, Human named Jenny Larsen aged 47]
# Jenny and Kevin having triples
triplets = (j + k) * 3
print(triplets)
# [Human named Newborn Larsen aged 0, Human named Newborn Larsen aged 0, Human named Newborn Larsen aged 0]




#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n___   ___   ___   263. Making a Grumpy Dictionary - Overriding Dict   ___   ___   ___\n")



#	263. Making a Grumpy Dictionary - Overriding Dict



class GrumpyDict(dict):
	#def __init__(self):
		# is not required because we not going to add any new properties or values to dict class
	def __repr__(self):
		print("NONE OF YOUR BUSINESS")
		return super().__repr__()
	
	def __missing__(self, key):
		print(f"YOU WANT '{key.upper()}'? WELL IT AINT HERE!")
	
	def __setitem__(self, key, value):
		print("YOU WANT TO CHANGE THE DICTIONARY?")
		print("OK FINE...")
		super().__setitem__(key, value)    #    <<<===    this is to update actual dict

d = GrumpyDict({"name": "Yoko", "city": "New York"})
print(d)
# NONE OF YOUR BUSINESS
# {"name": "Yoko", "city": "New York"}
d["city"] = "SF"
# YOU WANT TO CHANGE THE DICTIONATY?
# OK FINE...
print(d)
# NONE OF YOUR BUSINESS
# {"name": "Yoko", "city": "SF"}
d['place']
# YOU WANT 'PLACE'? WELL IT AINT HERE!




#	================================================================================================
#	================================================================================================
#	================================================================================================






#	================================================================================================
#	================================================================================================
#	================================================================================================



#	121. Intro To Dictionaries: Creating Dictionaries
#	123. Accessing Data in Dictionaries
#	125. Iterating Dictionaries
#	127. Using In With Dictionaries
#	128. Dictionary Methods: Clear, Copy, Fromkeys, and Get
#	131. Dictionary Methods: Pop, Popitems, and Update
#	133. Spotify Playlist Example
#	134. Dictionary Comprehension



#	Coding Exercise 26: Dictionary Creation Exercise
#	Coding Exercise 27: Access Data in a Dictionary Exercise
#	Coding Exercise 28: Totaling Donations Exercise
#	Coding Exercise 29: Dictionary Access
#	Coding Exercise 30: Fromkeys Exercise
#	Coding Exercise 31: Dictionary Methods Exercise



#	================================================================================================
#	================================================================================================
#	================================================================================================



#	121. Intro To Dictionaries: Creating Dictionaries



instructor = {
	"name": "Colt",
	"owns_dog": True,
	"num_courses": 4,
	"favorite_language": "Pyhton",
	"is_hilarious": False,
	44: "my favorite number!"
}
print(instructor)



instructor = dict(name = 'Colt', owns_dog = True)    #    not sure for now how to add 44 = 'favorite number'
print(instructor)
# {'name': 'Colt', 'owns_dog' = True}



#	================================================================================================
#	================================================================================================
#	================================================================================================



#	123. Accessing Data in Dictioonaries



instructor = {
	"name": "Colt",
	"owns_dog": True,
	"num_courses": 4,
	"favorite_language": "Pyhton",
	"is_hilarious": False,
	44: "my favorite number!"
}
instructor["name"]    # 'Colt'
# instructor["thing"]    # KeyError
print(instructor["name"] + " loves " + instructor["favorite_language"])
# Colt loves Python



#	================================================================================================
#	================================================================================================
#	================================================================================================



#	125. Iterating Dictionaries



instructor = {
	"name": "Colt",
	"owns_dog": True,
	"num_courses": 4,
	"favorite_language": "Pyhton",
	"is_hilarious": False,
	44: "my favorite number!"
}



#    .values()

for value in instructor.values():
	print(value)
# Colt
# True
# 4
# Python
# False
# my favorite number!



#    .keys()

for key in instructor.keys():
	print(key)
# name
# owns_dog
# num_courses
# favorite_language
# is_hilarious
# 44



#    .items()

for key,value in instructor.items():
	print(f"{key}: {value}")
# name: Colt
# owns_dog: True
# num_courses: 4
# favorite_language: Python
# is_hilarious: False
# 44: favorite number



#	================================================================================================
#	================================================================================================
#	================================================================================================



#    in

instructor = {
	"name": "Colt",
	"owns_dog": True,
	"num_courses": 4,
	"favorite_language": "Pyhton",
	"is_hilarious": False,
	44: "my favorite number!"
}
"name" in instructor     # True
"awesom" in instructor   # False
"Colt" in instructor     # False
"Colt" in instructor.values()    # True
# "Nope!" in instructor.values()   # False



#	================================================================================================
#	================================================================================================
#	================================================================================================



#	128. Dictionary Methods: Clear, Copy, Fromkeys, and Get



#    .clear()

instructor = {
	"name": "Colt",
	"owns_dog": True,
	"num_courses": 4,
	"favorite_language": "Pyhton",
	"is_hilarious": False,
	44: "my favorite number!"
}
instructor.clear()
instructor    # { }



#    .copy()

instructor = {
	"name": "Colt",
	"owns_dog": True,
	"num_courses": 4,
	"favorite_language": "Pyhton",
	"is_hilarious": False,
	44: "my favorite number!"
}
instructor2 = instructor.copy()
print(instructor2)
# {'name': 'Colt', 'owns_dog': True, 'num_courses': 4, 'favorite_language': 'Python', 'is_hilarious': False, 44: 'favorite number'}
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
	"num_courses": 4,
	"favorite_language": "Pyhton",
	"is_hilarious": False,
	44: "my favorite number!"
}
instructor.get("name")    # 'Colt'
# instructor["no_key"]    # KeyError
instructor.get("no_key")    # None



#	================================================================================================
#	================================================================================================
#	================================================================================================



#	Coding Exercise 29: Dictionary Access



from random import choice
food = choice(["cheese pizza", "quiche", "morning bun", "gummy bear", "tea cake"])
bakery_stock = {
	"almond croissant": 12,
	"toffee cookie": 3,
	"morning bun": 1,
	"chocolate chunk cookie": 9,
	"tea cake": 25
}

print(food)
if food in bakery_stock:
    print(str(bakery_stock.get(food)) + " left")
else:
    print("We Don't make that")



#    in

item = bakery_stock.get(food)
if item:
	print(f"{bakery_stock[food]} {food} left")
else:
	print("we don't make that")



#    .get
	
if food in bakery_stock:
	print(f"{food}: {bakery_stock[food]} in stock")
else:
	print("we don't make that")



#	================================================================================================
#	================================================================================================
#	================================================================================================



#	Coding Exercise 30: Fromkeys Exercise


game_properties = ["current_score", "high_score", "number_of_lives", "items_in_inventory", "power_ups", "ammo", "enemies_on_screen", "enemy_kills", "enemy_kill_streaks", "minutes_played", "notifications", "achievements"]
initial_game_states = dict.fromkeys(game_properties, 0)
print(initial_game_states)
# {'current_score': 0, 'high_score': 0, 'number_of_lives': 0, 'items_in_inventory': 0, 'power_ups': 0, 'ammo': 0, 'enemies_on_screen': 0, 'enemy_kills': 0, 'enemy_kill_streaks': 0, 'minutes_played': 0, 'notifications': 0, 'achievements': 0}



#	================================================================================================
#	================================================================================================
#	================================================================================================



#	131. Dictionary Methods: Pop, Popitems, and Update



#    .pop()

instructor = {
	"name": "Colt",
	"owns_dog": True,
	44: "favorite number"
}
instructor.pop("name")    # 'Colt'
print(instructor)
# {'owns_dog': True, 44: 'favorite number'}
#instructor.pop("surname")    # KeyError
#instructor.pop()             # TypeError: pop expected at least 1 argument, got 0



#    .popitem()    it removes random key value pair and returns it.

instructor = {
	"name": "Colt",
	"owns_dog": True,
	44: "favorite number"
}
instructor.popitem()    # (44, 'favorite number')
#instructor.popitem('name')    # TypeError: popitem() takes no arguments (1 given)
print(instructor)
# {'name': 'Colt', 'owns_dog': True}



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



#	================================================================================================
#	================================================================================================
#	================================================================================================



#	133. Spotify Playlist Example



playlist = {
	"Name of the Playlist": "Patagonia Bus",
	"Creator": "Colt",
	"Songs": [
		{
		"Song Name": "title1",
		"Artist": ["artist1", "artist2"],
		"Album": "title1",
		"Duration": 2.5
		},
		{
		"Song Name": "title2",
		"Artist": ["artist1"],
		"Album": "title2",
		"Duration": 5.1
		},
		{
		"Song Name": "title3",
		"Artist": ["artist12", "artist27", "artist23"],
		"Album": "title3",
		"Duration": 3.0
		}
	]
}

total_length = 0
for song in playlist["Songs"]:
	total_length += song["Duration"]
print(total_length)

for song in playlist["Songs"]:
	print(song["Song Name"])



#	================================================================================================
#	================================================================================================
#	================================================================================================



#    134. Dictionary Comprehension
#    {___:___ for ___ in ___}



numbers = dict(first = 1, second = 2, third = 3)
squared_numbers = {key: value ** 2 for key,value in numbers.items()}
print(squared_numbers)
# {'first': 1, 'second': 4, 'third': 9}



numbers2 = {num: num ** 2 for num in [1, 2, 3, 4, 5]}
print(numbers2)
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}



str1 = "ABC"
str2 = "123"
combo = {str1[i]: str2[i] for i in range(0, len(str1))}
print(combo)
# {'A': '1', 'B': '2', 'C': '3'}



#	Conditional Logic 

num_list = [1, 2, 3, 4]
altered = {num:("even" if num % 2 == 0 else "odd") for num in num_list}
print(altered)
# {1: 'odd', 2: 'even', 3: 'odd', 4: 'even'}

instructor = {"name": "colt", "city": "san francisco", "colour": "purple"}
yelling_instructor = {key.upper():value.upper() for key,value in instructor.items()}
print(yelling_instructor)
# {'NAME': 'COLT', 'CITY': 'SAN FRANCISCO', 'COLOUR': 'PURPLE'}

sometimes_yelling_instructor = {(key.upper() if key is "colour" else key):value.upper() for key,value in instructor.items()}
print(sometimes_yelling_instructor)
# {'name': 'COLT', 'city': 'SAN FRANCISCO', 'COLOUR': 'PURPLE'}



#	================================================================================================
#	================================================================================================
#	================================================================================================



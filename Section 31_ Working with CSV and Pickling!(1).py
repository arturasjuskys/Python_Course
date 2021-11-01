


#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - Section 31: Working with CSV and Pickling! \n")



#	Section 31: Working with CSV and Pickling!



#	314. Reading CSV Files
#	315. Writing to CSV Files: Writer
#	316. Writing to CSV Files: DictWriter
#	320. Pickling Time!
#	321. Extra Fancy JSON Pickling



#	Coding Exercise 99: add_user
#	Coding Exercise 100: print_users
#	Coding Exercise 101: find_user
#	Coding Exercise 102: update_users
#	Coding Exercise 103: delete_users



#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 314. Reading CSV Files \n")



#	314. Reading CSV Files



#	CSV - Comma Seperated Values

		#	CSV files are common file format for tabular data
		#	We can read CSV files just like other text files
		#	Python has buiilt-in CSV module to read/write CSVs more easily



#	CSV Module

		#	reader - lets you iterate over rows of the CSV as lists
		#	DictReader - lets you iterate over rows of hte CSV as OrderedDicts



#	BAD Way of Doing it!!!

with open("fighters.csv") as file:
	data = file.read()
	print(data)
# Name,Country,Height (in cm)
# Ryu,Japan,175
# Ken,USA,175
# Chun-Li,China,165
# Guile,USA,182
# E. Honda,Japan,185
# Dhalsim,India,176
# Blanka,Brazil,192
# Zangief,Russia,214

#	because then you need to manually pars the data to make it more usable, where CSV Module does it for you



#	reader

from csv import reader
with open("fighters.csv") as file:
	csv_reader = reader(file)
	for row in csv_reader:
		#	each row is a list
		print(row)
# ['Name', 'Country', 'Height (in cm)']
# ['Ryu', 'Japan', '175']
# ['Ken', 'USA', '175']
# ['Chun-Li', 'China', '165']
# ['Guile', 'USA', '182']
# ['E. Honda', 'Japan', '185']
# ['Dhalsim', 'India', '176']
# ['Blanka', 'Brazil', '192']
# ['Zangief', 'Russia', '214']



with open("fighters.csv") as file:
	csv_reader = reader(file)
	next(csv_reader)    #    <<<===    this moves cursor to next line, thus skipping header as a first line
	for fighter in csv_reader:
		print(f"{fighter[0]} is from {fighter[1]}")
# Ryu is from Japan
# Ken is from USA
# Chun-Li is from China
# Guile is from USA
# E. Honda is from Japan
# Dhalsim is from India
# Blanka is from Brazil
# Zangief is from Russia



with open("fighters.csv") as file:
	csv_reader = reader(file)
	data = list(csv_reader)
	print(data)
# [['Name', 'Country', 'Height (in cm)'], ['Ryu', 'Japan', '175'], ['Ken', 'USA', '175'], ['Chun-Li', 'China', '165'], ['Guile', 'USA', '182'], ['E. Honda', 'Japan', '185'], ['Dhalsim', 'India', '176'], ['Blanka', 'Brazil', '192'], ['Zangief', 'Russia', '214']]



#	DictReader

from csv import DictReader
with open("fighters.csv") as file:
	csv_reader = DictReader(file)
	for row in csv_reader:
		#	each row is an OrderedDict!
		print(row)
# {'Name': 'Ryu', 'Country': 'Japan', 'Height (in cm)': '175'}
# {'Name': 'Ken', 'Country': 'USA', 'Height (in cm)': '175'}
# {'Name': 'Chun-Li', 'Country': 'China', 'Height (in cm)': '165'}
# {'Name': 'Guile', 'Country': 'USA', 'Height (in cm)': '182'}
# {'Name': 'E. Honda', 'Country': 'Japan', 'Height (in cm)': '185'}
# {'Name': 'Dhalsim', 'Country': 'India', 'Height (in cm)': '176'}
# {'Name': 'Blanka', 'Country': 'Brazil', 'Height (in cm)': '192'}
# {'Name': 'Zangief', 'Country': 'Russia', 'Height (in cm)': '214'}



with open("fighters.csv") as file:
	csv_reader = DictReader(file)
	for row in csv_reader:
		print(row['Name'])
# Ryu
# Ken
# Chun-Li
# Guile
# E. Honda
# Dhalsim
# Blanka
# Zangief



#	Other Delimiters



#	Readers accept a delimiter kwarg in case your data isn't seperated by commas.



from csv import reader
with open("fighters.csv") as file:
	csv_reader = reader(file, delimiter = "|")    #    <<<===    this is where you provide other types of delimiters
	for row in csv_reader:
		#	each row is a list!
		print(row)
# ['Name,Country,Height (in cm)']
# ['Ryu,Japan,175']
# ['Ken,USA,175']
# ['Chun-Li,China,165']
# ['Guile,USA,182']
# ['E. Honda,Japan,185']
# ['Dhalsim,India,176']
# ['Blanka,Brazil,192']
# ['Zangief,Russia,214']

#	^^^^^^^^^^^^^^^^^ - this print(row) prints whole line as one list item because this file doesnt have 'delimiter = "|"'



#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 315. Writing to CSV Files: Writer \n")



#	315. Writing to CSV Files: Writer



#	Writing CSV Files

	#	Using lists

		#	writer - creates a writer object for writing to CSV
		#	writerow - method on a writer to write a row to the CSV



from csv import writer
with open("fighters2.csv", "w") as file:
	csv_writer = writer(file)
	csv_writer.writerow(["Character", "Move"])
	csv_writer.writerow(["Ryu", "Hadouken"])



#	This example will read original file and copy everything capitalized to new file
#	Approach, with only 1 file open at a time
from csv import reader, writer
with open("fighters.csv") as file:
	csv_reader = reader(file)
	fighters = [[s.upper() for s in row] for row in csv_reader]
	for row in fighters:
		print(row)
# ['NAME', 'COUNTRY', 'HEIGHT (IN CM)']
# ['RYU', 'JAPAN', '175']
# ['KEN', 'USA', '175']
# ['CHUN-LI', 'CHINA', '165']
# ['GUILE', 'USA', '182']
# ['E. HONDA', 'JAPAN', '185']
# ['DHALSIM', 'INDIA', '176']
# ['BLANKA', 'BRAZIL', '192']
# ['ZANGIEF', 'RUSSIA', '214']
with open("screaming_fighters.cvs", "w") as file:
	csv_writer = writer(file)
	for fighter in fighters:
		csv_writer.writerow(fighter)



#	Slitly more efficient way of manipulating data
#	using nested with statments
from csv import reader, writer
with open("fighters.csv") as file:
	csv_reader = reader(file)
	with open("screaming_fighters2.cvs", "w") as file:
		csv_writer = writer(file)
		for fighter in csv_reader:
			csv_writer.writerow([s.upper() for s in fighter])



#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 316. Writing to CSV Files: DictWriter \n")



#	316. Writing to CSV Files: DictWriter



#	Writing CSV Files

	#	Using Dictionaries

		#	DictWriter - creates a writer object for writing using dictionaries
		#	fieldnames - kwarg for the DictWriter specifying headers
		#	writeheader - method on a writer to write header row
		#	writerow - method on a writer to write a row based on a dictionary



from csv import DictWriter
with open("example.csv", "w") as file:
	headers = ["Character", "Move"]
	csv_writer = DictWriter(file, fieldnames = headers)
	csv_writer.writeheader()
	csv_writer.writerow({
		"Character": "Ryu",
		"Move": "Hadouken"
	})
	
from csv import writer, DictWriter
with open("cats.csv", "w") as file:
	headers = ["Name", "Breed", "Age"]
	csv_writer = DictWriter(file, fieldnames = headers)
	csv_writer.writeheader()
	csv_writer.writerow({
		"Name": "Garfield",
		"Breed": "Orange Tabby",
		"Age": 10
	})



#	This example will take fighters.cvs and will creater fighters3.cvs with height changed from cm to inch
from csv import DictReader, DictWriter
def cm_to_in(cm):
	return round(float(cm) * 0.393701, 2)
with open("fighters.csv") as file:
	csv_reader = DictReader(file)
	fighters = list(csv_reader)
with open("fighters3.csv", "w") as file:
	headers = ("Name", "Country", "Height")    #    <<<===    here we change from Height (in cm) to just Height in new file
	csv_writer = DictWriter(file, fieldnames = headers)
	csv_writer.writeheader()
	for fighter in fighters:
		csv_writer.writerow({    #    <<<===    because to update new key in fighters.csv we needed to write them manually
			"Name": fighter["Name"],
			"Country": fighter["Country"],
			"Height": cm_to_in(fighter["Height (in cm)"])
		})





#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - Coding Exercise 99: add_user \n")



#	Coding Exercise 99: add_user



def add_user(first, last):
	from csv import reader, writer
	"""add_user("Dwayne", "Johnson") # None
	# CSV now has two data rows:

	# First Name,Last Name
	# Colt,Steele
	# Dwayne,Johnson
	"""
	with open("users.csv", "a") as file:
		csv_writer = writer(file)
		csv_writer.writerow([first, last])






#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - Coding Exercise 100: print_users \n")



#	Coding Exercise 100: print_users



def print_users():
	from csv import DictReader, DictWriter
	with open("users.csv") as file:
		csv_reader = DictReader(file)
		for user in csv_reader:
			print(f"{user['First Name']} {user['Last Name']}")





#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - Coding Exercise 101: find_user \n")



#	Coding Exercise 101: find_user



from csv import reader, writer
def find_user(first_name, last_name):
	"""
	find_user("Colt", "Steele") # 1
	find_user("Alan", "Turing") # 3
	find_user("Not", "Here") # 'Not Here not found.'
	"""
	with open("users.csv") as file:
		csv_reader = reader(file)
		for (index, row) in enumerate(csv_reader):
			first_name_match = first_name == row[0]
			last_name_match = last_name == row[1]
			if first_name_match and last_name_match:
				return index
		return f"{first_name} {last_name} not found."




#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 320. Pickling Time! \n")



#	320. Pickling Time!



import pickle
class Animal:
	def __ini__(self, name, species):
		self.name = name
		self.species = species
	def __rep__(self):
		return f"{self.name} is a {self.species}"
	def make_sound(self, sound):
		print(f"this animal says {sound}")
class Cat(Animal):
	def __init__(self, name, breed, toy):
		super().__init__(name, species = "Cat")    #    <<<===    call init ojn parent class
		self.breed = breed
		self.toy = toy
	def play(self):
		print(f"{self.name} plays with {self.toy}")

blue = Cat("Blue", "Scottish Fold", "String")

#	To pickle an object:
with open("pets.pickle", "wb") as file:
	pickle.dump(blue, file)    #    <<<===    this line stores the file in binary stream

#	class saved in pickle with still require class defined, but blue variable is no longer needed
# To unpickle something:
with open("pets.pickle", "rb") as file:
	zombie_blue = pickle.load(file)
	print(zombie_blue)
	print(zombie_blue.play())







#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 321. Extra Fancy JSON Pickling \n")



#	321. Extra Fancy JSON Pickling







#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - Coding Exercise 102: update_users \n")



#	Coding Exercise 102: update_users








#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - Coding Exercise 103: delete_users \n")



#	Coding Exercise 103: delete_users












#	================================================================================================
#	================================================================================================
#	================================================================================================



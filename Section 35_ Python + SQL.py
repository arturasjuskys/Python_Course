


#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - Section 35: Python + SQL \n")



#	Section 35: Python + SQL



#	356. Intro to Section
#	357. Installing SQLite3
#	358. SQL Basics: Creating Tables
#	359. SQL Basics: Inserting
#	360. SQL Basics: Selecting
#	361. Connecting to a DB With Python
#	362. Inserting With Python
#	363. Bulk Inserts With Python
#	364. Selecting With Python
#	365. SQL INJECTION!
#	367. Scraping to a Database Pt.1
#	367. Scraping to a Database Pt.2



#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 357. Installing SQLite3 \n")



#	357. Installing SQLite3



#	To check if SQLite3 is preinstalled on the machine:
	#	type the following line to terminal:
		#	sqlite3	|	sqlite
				#	to know if sqlite is not installed there will be a message with 'command not regonised' or something similar



#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 358. SQL Basics: Creating Tables \n")



#	358. SQL Basics: Creating Tables



#	Storage Classes and Datatypes
		#	NULL	The value is a NULL value.
		#	INTEGER	The value is a signed integer, stored 1, 2, 3, 4, 5, 6, or 8 bytes dependihhng on the magnitude of the value.
		#	REAL	The value is a floating point, stored as a 8-byte IEEE floating point number.
		#	TEXT	The value is a text string, storeg using the database encoding (UTF-8, UTF-16BE or UTF-16LE).
		#	BLOB	The value is a blob of data, stored exactly as it was input



#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 359. SQL Basics: Inserting \n")



#	359. SQL Basics: Inserting



#	commandline code:
		#	INSERT INTO cats (name, breed, age) VALUES ("Blue", "Scottish Fold", 3);
		#	SELECT * FROM cats;
				#	Blue|Scottish Fold|3

#	To read from file:
		#	sqlite3 dog_db.db
		#	.tables
		#	.read Section 35; Python + SQL.sql    <<<===    this will read from a sql file, and will executs it.
		#	SELECT * FROM dogs;
				#	Champ|Husky|4
				#	Rose|Chihuahua|11
				#	...
				#	...



#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 360. SQL Basics: Selecting \n")



#	360. SQL Basics: Selecting



#	commandline code
		#	.read Section 35; Python + SQL.sql
		
		#	SELECT * FROM dogs;
		#	SELECT * FROM dogs WHERE name IS "Piggy";
		#	SELECT * FROM dogs WHERE breed IS "Husky";
		#	SELECT name FROM dogs WHERE breed IS "Husky";
		#	SELECT name,age,breed FROM dogs WHERE breed IS "Husky";
		#	SELECT * FROM dogs WHERE breed IS NOT "Chihuahua";
		#	SELECT * FROM dogs WHERE breed IS NOT "Chihuahua" AND breed IS NOT "Pug";
		#	SELECT * FROM dogs WHERE age > 8;
		
		#	SELECT * FROM dogs WHERE name LIKE "%gg%"    <<<===    this "%gg%" will select any name that has a two 'g' letters together, and '%' means any character.		



#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 361. Connecting to a DB With Python \n")



#	361. Connecting to a DB With Python



import sqlite3
connection = sqlite3.connect("my_friends.db")
sql_code = "CREATE TABLE friends (first_name TEXT, last_name TEXT, closeness INTEGER);"
#	create a cursor object
cursor = connection.cursor()
#	execute some sql
#cursor.execute(sql_code)    <<<===    this is commented out so code below would work
#	commit changes
connection.commit()
connection.close()



#	commandline code:
		#	python3 Section 35; Python + SQL.py
		#	sqlite3 my_test.db
		#	.tables
				#	test    <<<===    this is the table created
		#	.schema my_test
				#	CREATE TABLE test (first_name TEXT, last_name TEXT, closeness INTEGER);



#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 362. Inserting With Python \n")



#	362. Inserting With Python



import sqlite3
connection = sqlite3.connect("my_friends.db")
#	create a cursor object
cursor = connection.cursor()
#	execute some sql
insert_query = "INSERT INTO friends VALUES ('Merriweather', 'Lewis', 7)"
#cursor.execute(insert_query)    <<<===    this is commented out so code below would work
#	commit changes
connection.commit()
connection.close()



#	bad way of interpolating data to tables
connection = sqlite3.connect("my_friends.db")
#	create a cursor object
cursor = connection.cursor()
#	execute some sql
from_first = "Dana"
query = f"INSERT INTO friends (first_name) VALUES ('{from_first}')"
#cursor.execute(query)    #    <<<===    this is commented out so code below would work
#	commit changes
connection.commit()
connection.close()



#	BETTER WAY!!!
connection = sqlite3.connect("my_friends.db")
#	create a cursor object
cursor = connection.cursor()
#	execute some sql
form_first = "Mary-Todd"
query2 = f"INSERT INTO friends (first_name) VALUES (?)"    #    <<<===    (?) is a value added bolow
#cursor.execute(query2, (form_first,))    #    <<<===    values need to be in a tuple, otherwise they will be iterated over as letter after letter.
#	commit changes
connection.commit()
connection.close()



#	Inserting a friend with multiple values
connection = sqlite3.connect("my_friends.db")
#	create a cursor object
cursor = connection.cursor()
#	execute some sql
data = ("Steve", "Irwin", 9)
query3 = "INSERT INTO friends VALUES (?,?,?)"    #    <<<===    3x for every value in friends variable
cursor.execute(query3, data)    #    <<<===    because variable is formated into a tuple here is enough to refer to the variable itself
#	commit changes
connection.commit()
connection.close()



#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 363. Bulk Inserts With Python \n")



#	363. Bulk Inserts With Python



connection = sqlite3.connect("my_friends.db")
#	create a cursor object
cursor = connection.cursor()

people = [
	("Roald", "Amundsen", 5),
	("Rosa", "Parks", 8),
	("Henry", "Hudson", 7),
	("Neil", "Armstrong", 7),
	("Daniel", "Boone", 3)
]
#	OPTION 1
#	this will allow just one action, inserting
cursor.executemany("INSERT INTO friends VALUES (?, ?, ?)", people)

#	OPTION 2
#	this will allow to do multiple actions
for person in people:
	cursor.execute("INSERT INTO friends VALUES (?, ?, ?)", person)    #    <<<===    use a temporary variable used in loop
	print("INSERTING...")
	#	any other math or action u want to take

connection.commit()
connection.close()



#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 364. Selecting With Python \n")



#	364. Selecting With Python



#	this example will will print out all the data in my_friends file the table friends
connection = sqlite3.connect("my_friends.db")
cursor = connection.cursor()
cursor.execute("SELECT * FROM friends")
#	
for result in cursor:
	print(result)
connection.commit()
connection.close()



connection = sqlite3.connect("my_friends.db")
cursor = connection.cursor()
cursor.execute("SELECT * FROM friends")
#	this example will return all the data in a single list of tuple values
print(cursor.fetchall())
connection.commit()
connection.close()



#	this example will return one value
connection = sqlite3.connect("my_friends.db")
cursor = connection.cursor()
cursor.execute("SELECT * FROM friends WHERE first_name IS 'Rose'")
print(cursor.fetchone())
connection.commit()
connection.close()



#	this will return a list of friends by closenes and order them
connection = sqlite3.connect("my_friends.db")
cursor = connection.cursor()
cursor.execute("SELECT * FROM friends WHERE closeness > 5 ORDER BY closeness")
print(cursor.fetchall())
connection.commit()
connection.close()



#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 365. SQL INJECTION! \n")



#	365. SQL INJECTION!



#	this example will go to data base and search for whaterver user inputs
connection = sqlite3.connect("users.db")

#query = "CREATE TABLE users (username TEXT, password TEXT)"    #    <<<===    table is created
username = input("Please enter your username...")
password = input("Please enter you password...")

#	this is the wrong way because u can skip password verification bit
#query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
query = f"SELECT FROM users WHERE username = ? AND password = ?"

cursor = connection.cursor()
cursor.execute(query, (username, password))

result = cursor.fetchone()
if result:
	print("Welcome Back")
else:
	print("Failed Login") 

connection.commit()
connection.close()



#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 367. Scraping to a Database Pt.1 \n")



#	366. Scraping to a Database Pt.1



import sqlite3
import requests
from bs4 import BeautifulSoup

def scrape_books(url):
	response = requests.get(url)
	soup = BeautifulSoup(response.text, "html.parser")
	books = soup.find_all("article")
	all_books = []
	for book in books:
		book_data = (get_title(book), get_price(book), get_rating(book))
		all_books.append(book_data)
	save_books(all_books)

def save_books(all_books):
	connection = sqlite3.connect("books.db")
	cursor = connection.cursor()
	cursor.execute('''CREATE TABLE books
		(title TEXT, price REAL, rating INTEGER)''')
	cursor.executemany("INSERT INTO books VALUES (?,?,?)", all_books)
	connection.commit()
	connection.close()

def get_title(book):
	return book.find("h3").find("a")["title"]

def get_price(book):
	price = book.select(".price_color")[0].get_text()
	return float(price.replace("£", "").replace("Â", ""))

def get_rating(book):
	ratings = {"Zero": 0, "One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
	word = book.select(".star-rating")[0].get_attribute_list("class")[-1]
	return ratings[word]


scrape_books("http://books.toscrape.com/catalogue/category/books/history_32/index.html")
#	print(int_star_rating)
#	print(title, price)
# Initialize BS
# Exctarct data we want
# Save data to database



#	================================================================================================
#	================================================================================================
#	================================================================================================



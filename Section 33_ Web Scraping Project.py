


#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - Section 33: Web Sracping Project \n")



#	Section 33: Web Sracping Project



#	332. Qoute Scraping Project: Intro
#	333. Scraping Project
#	334. Qoute Scarping Project: Part 1
#	335. Qoute Scarping Project: The Game Logic
#	336. Qoute Scarping Project: Refactoring
#	337. Qoute Scarping Project: Adding CSV
#	338. Creating A Web Crawler with Scrapy



#	================================================================================================
#	================================================================================================
#	================================================================================================



#	333. Scraping Project



import requests
from bs4 import BeautifulSoup
from csv import DictWriter, DictReader
from time import sleep
from random import choice

BASE_URL = "http://quotes.toscrape.com/"

def scrape_quotes():
	all_quotes = []
	url = "/page/1"
	while url:
		response = requests.get(f"{BASE_URL}{url}")
		print(f"Now Scarping {BASE_URL}{url}...")
		soup = BeautifulSoup(response.text, "html.parser")
		quotes = soup.find_all(class_ = "quote")

		for quote in quotes:
			all_quotes.append({
				"text": quote.find(class_ = "text").get_text(),
				"author": quote.find(class_ = "author").get_text(),
				"bio-link": quote.find("a")["href"]
			})
		next_btn = soup.find(class_ = "next")
		url = next_btn.find("a")["href"] if next_btn else None
		#sleep(2)
	return all_quotes

def start_game(quotes):     #    <<<===    this is to introduce the repeatability without using to many nested loops or nested conditiopnal logic
	quote = choice(quotes)
	remaining_guesses = 4

	print("Here's a quote:")
	print(quote["text"])
	print(quote["author"])

	guess = ""
	while guess.lower() != quote["author"].lower() and remaining_guesses != 0:
		guess = input(f"Who said this quote? Guesses remaining {remaining_guesses}\n")
		if guess.lower() == quote["author"].lower():
			print("YOU GOT IT RIGHT!")
			break
		remaining_guesses -= 1
		if remaining_guesses == 3:
			response = requests.get(f"{BASE_URL}{quote['bio-link']}")
			soup = BeautifulSoup(response.text, "html.parser")
			birth_date = soup.find(class_ = "author-born-date").get_text()
			birth_place = soup.find(class_ = "author-born-location").get_text()
			print(f"Here's a hint: The author was born {birth_date} {birth_place}")
		elif remaining_guesses == 2:
			print(f"Here's a hint: The author's first name start whith: {quote['author'][0]}")
		elif remaining_guesses == 1:
			last_initial = quote["author"].split(" ")[1][0]    #    this will split the name, and select 2nd value in the list, and then will select 1st index
			print(f"Here's a hint: The author's last name start whith: {last_initial}")
		else:
			print(f"Sorry you ran out of guesses. The answer was {quote['author']}")

	again = ''
	while again.lower() not in ('y', 'yes', 'n', 'no'):
		again = input("Would you like to play again (y/n)?")
	if again.lower() in ('yes', 'y'):
		return start_game(quotes)
	else:
		print("OK GOODBYE!")


def write_quotes(quotes):
	with open("quotes.csv", "w") as csv_file:
		headers = ["text", "author", "bio-link"]
		csv_writer = DictWriter(csv_file, fieldnames = headers)
		csv_writer.writeheader()
		for quote in quotes:
			csv_writer.writerow(quote)

quotes = scrape_quotes()    #    <<<===    this is to start scraping process
write_quotes(quotes)
start_game(quotes)    #    <<<===    this is to start the game 



#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - Section 33: Web Sracping Project \n")



#	338. Creating A Web Crawler with Scrapy



#	Full documentation is on http://scapy.org
		#	python -m pip install scarpy
		#	to execute the spider:
				#	scarpy runspider -o books.csv Section 33; Web Scraping Project.py
				#	                    ^^^^^^^^^       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
				#	                   where to save            code files name








#	================================================================================================
#	================================================================================================
#	================================================================================================



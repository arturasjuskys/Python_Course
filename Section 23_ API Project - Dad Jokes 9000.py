import requests
from random import choice
from pyfiglet import figlet_format
import colorama
from termcolor import colored

header = ("DAD JOKES OVER 9000")
header = colored(header, color = "magenta")
print(header)
url = "https://icanhazdadjoke.com/search"
user_input = input("What type of joke you want to hear? ")
response = requests.get(
	url,
	headers = {"Accept": "application/json"},
	params = {"term": user_input}
).json()
#num_jokes = len(response["results"])
num_jokes = response["total_jokes"]
results = response["results"]
if num_jokes > 1:
	print(f"I found {num_jokes} jokes about {user_input}s. Here's one:")
	print(choice(results)["joke"])
elif num_jokes == 1:
	print(f"I found one joke about {user_input}")
	print(results[0]["joke"])
else:
	print(f"Sorry, couldn't find a joke with your term: {user_input}")


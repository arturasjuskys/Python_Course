


#	================================================================================================
#	================================================================================================
#	================================================================================================



#	Section 23: OPTIONAL SECTION: Making HTTP Requests with Python



#	224. HTTP: START HERE
#	225. HTTP Introduction and Crash Course
#	226. HTTP Verbs and APIs
#	227. Writing Your First Python Request
#	228. Requesting JSON with Python
#	229. Sending Requests with Params
#	230. API Project
#	231. API Project Solution



#	================================================================================================
#	================================================================================================
#	================================================================================================



#	225. HTTP Introduction and Crash Course



#	URL bar
	#	1. DNS Loopup
		#	Reqest/Response cycle
			#	2. Computer makes a REQUEST to a server
			#	3. Sever processes the REQUEST
			#	4. Server issues a RESPONSE
				#	Responce Status Codes
					#	2xx - Success
					#	3xx - Redirect
					#	4xx - Client Error (your fault)
					#	5xx - Server Error (not your fault)



#	================================================================================================
#	================================================================================================
#	================================================================================================



#	226. HTTP Verbs and APIs



	#	HTTP Verbs

		# Get
			# Useful for retrieving data
			# Data passed in query string
			# Should have no "side-effects"
			# Can be cashed
			# Can be bookmarked

		# Post
			# Useful for writing data
			# Data passed in request body
			# Can have "side-effects"
			# Not cached
			# Can't be bookmarked

		# More...



	#	API
		# API - Application Programming Interface
			# This is ment to be read by coputers
		# Allows you to get data from another application without needing to understand how the application works
		# Can often send data back in different formats
		# Examples of companies with APIs: GitHub, Spotify, Google, More...


		# API Formats

			# JSON - JavaScript Object Notation
			# XML - Extensible Markup Language



#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n___   ___   ___   227. Writing Your First Python Request   ___   ___   ___\n")




#	227. Writing Your First Python Request



# Using the requests Module



#	python -m pip install requests

import requests
response = requests.get("https://news.ycombinator.com/")
print(response)
# <Response [200]>
print(response.ok)
# True
# print(response.headers)
	# {'Server': 'nginx', 'Date': 'Mon, 25 Nov 2019 13:51:00 GMT', 'Content-Type': 'text/html; charset=utf-8', 'Transfer-Encoding': 'chunked', 'Connection': 'keep-alive', 'Vary': 'Accept-Encoding', 'Cache-Control': 'private; max-age=0', 'X-Frame-Options': 'DENY', 'X-Content-Type-Options': 'nosniff', 'X-XSS-Protection': '1; mode=block', 'Referrer-Policy': 'origin', 'Strict-Transport-Security': 'max-age=31556900', 'Content-Security-Policy': "default-src 'self'; script-src 'self' 'unsafe-inline' https://www.google.com/recaptcha/ https://www.gstatic.com/recaptcha/ https://cdnjs.cloudflare.com/; frame-src 'self' https://www.google.com/recaptcha/; style-src 'self' 'unsafe-inline'", 'Content-Encoding': 'gzip'}
# print(f"\n\n\n{response.text}")
	#	Brings back all HTML for that page which is designed for human eye



import requests
url = "http://www.google.com"
responce = requests.get(url)
print(f"Your request to {url} came back with a status code {response.status_code}")



#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n___   ___   ___   228. Requesting JSON with Python   ___   ___   ___\n")




#	228. Requesting JSON with Python



	# requests Module
		# Lets us make HTTP requests from our Python cose!
		# Installed using pip
		# Useful for web scraping/crowling, grabbing data from other APIs, ect



import requests
response = requests.get(
	"http://www.examples.com",
	headers = {
		"header1": "value1",
		"header2": "value2"
	}
)



url = "https://icanhazdadjoke.com/"
response1 = requests.get(url, headers = {"Accept": "text/plain"})
response2 = requests.get(url, headers = {"Accept": "application/json"})
print("\nresponse1\n")
print(response1.text)
print("\nresponse2\n")
print(response2.text)
print(type(response2.text))
# <class 'str'>
print(response2.json())

joke_data = response2.json()
print(type(joke_data))
print(joke_data["joke"])
print(f"Status: {joke_data['status']}")



#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n___   ___   ___   229. Sending Requests with Params   ___   ___   ___\n")



#	229. Sending Requests with Params



#	Query String
	# A way to pass data to the sever as part of a GET request
	# http://www.example.com/?key1=value1&key2=value2



# #	OPTION 1
# import requests
# response = requests.get(
# 	"http://www.example.com/?key1=value1&key2=value2"
# 	#                      ^^^    this is query string syntax
# )

# #	OPTION 2
# import requests
# response = requests.get(
# 	"http://www.example.com",
# 	params = {
# 		"key1": "value1",
# 		"key2": "value2"
# 	}
# )



import requests
url = "https://icanhazdadjoke.com/search"
response = requests.get(
	url,
	headers = {"Accept": "application/json"},
	params = {"term": "cat", "limit": 1}
)
joke_data = response.json()
print(joke_data["results"])



#	================================================================================================
#	================================================================================================
#	================================================================================================



#	230. API Project



#	================================================================================================
#	================================================================================================
#	================================================================================================



#	231. API Project Solution



import requests
from random import choice
from pyfiglet import figlet_format
import colorama
from termcolor import colored

header = figlet_format("DAD JOKES OVER 9000")
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




#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - Section 32: Web Scarping with BeautifulSoup \n")




#	Section 32: Web Scarping with BeautifulSoup



#	324. Introduction to Web Scraping
#	325. Is Scraping...OK?
#	326. Optional HTML/CSS Crash Course
#	327. Selecting with BeautifulSoup: find()
#	328. Selecting With BeautifulSoup: CSS Style Selectors
#	329. Accessing Data with Beautiful Soup
#	330. Navigating With BeautifulSoup
#	331. Our First Scraping Program



#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 324. Introduction to Web Scraping \n")



#	324. Introduction to Web Scraping



#	Introduction to Web Scarpping

		#	Web scarpping involves programmatically grabbing data from a web page
		#	Three Steps: Download, extract data, PROFIT!

#	Why Scrape?
	
		#	There's data on a site that you want to store or analyze
		#	You can't get by other means (e.ge an API)
		#	You want to programmatically grab the data (instead of lots of manual copying/pasting)



#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 325. Is Scraping...OK? \n")



#	325. Is Scraping...OK?



#	Some websites don't want peolpe scraping them
#	Best practice: consult the robots.txt file
#	If makeing many requests, time them out
#	If you're too aggresive, you IP can be blocked



#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 327. Selecting with BeautifulSoup: find() \n")



#	327. Selecting with BeautifulSoup: find()



#	To Install BeautifulSoup
	#	command line
		#	python -m pip install bs4

#	Getting started with Beautiful Soup
		#	To extact data from HTML, we'll use Beautiful Soup
		#	Install it with pip
		#	Beautiful Soup leys us navigate through HTML with Python
		#	Beautiful Soup does NOT download HTML - for this, we need to requests module!



#	Parsing and Navigating HTML

		#	BeautifulSoup(html_string, "html.parser") - parse HTML
		#	Once parsed, There are several ways to navigate:
			#	By Tag Names
			#	Using find - returns one matching tag
			#	Using find_all - returns a list of matching tags


from bs4 import BeautifulSoup
html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>First HTML Page</title>
</head>
<body>
  <div id="first">
    <h3 data-example="yes">hi</h3>
    <p>more text.</p>
  </div>
  <ol>
    <li class="special">This list item is special.</li>
    <li class="special">This list item is also special.</li>
    <li>This list item is not special.</li>
  </ol>
  <div data-example="yes">bye</div>
</body>
</html>
"""
soup = BeautifulSoup(html, "html.parser")
print(soup)

print(type(soup))
# <!DOCTYPE html>

# <html lang="en">
# <head>
# <meta charset="utf-8"/>
# <title>First HTML Page</title>
# </head>
# <body>
# <div id="first">
# <h3 data-example="yes">hi</h3>
# <p>more text.</p>
# </div>
# <ol>
# <li class="special">This list item is special.</li>
# <li class="special">This list item is also special.</li>
# <li>This list item is not special.</li>
# </ol>
# <div data-example="yes">bye</div>
# </body>
# </html>

# <class 'bs4.BeautifulSoup'>
print("\n")

print(soup.body)
# <body>
# <div id="first">
# <h3 data-example="yes">hi</h3>
# <p>more text.</p>
# </div>
# <ol>
# <li class="special">This list item is special.</li>
# <li class="special">This list item is also special.</li>
# <li>This list item is not special.</li>
# </ol>
# <div data-example="yes">bye</div>
# </body>


#	This will return just the 1st div tag
print("\n")

print(soup.body.div)
# <div id="first">
# <h3 data-example="yes">hi</h3>
# <p>more text.</p>
# </div>
print("\n")

print(soup.find("div"))
# <div id="first">
# <h3 data-example="yes">hi</h3>
# <p>more text.</p>
# </div>


#	This example returns a list of two div tags
print("\n")

print(soup.find_all("div"))
# [<div id="first">
# <h3 data-example="yes">hi</h3>
# <p>more text.</p>
# </div>, <div data-example="yes">bye</div>]
print("\n")

print(soup.find(id = "first"))
# <div id="first">
# <h3 data-example="yes">hi</h3>
# <p>more text.</p>
# </div>
print("\n")

print(soup.find_all(class_ = "special"))    #    <<<===    to select HTML class you need to add _ at the back of class name
# [<li class="special">This list item is special.</li>, <li class="special">This list item is also special.</li>]
print("\n")

print(soup.find(attrs = {"data-example": "yes"}))
# <h3 data-example="yes">hi</h3>



#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 328. Selecting With BeautifulSoup: CSS Style Selectors \n")



#	328. Selecting With BeautifulSoup: CSS Style Selectors



#	Naviogating with CSS Selectors

		#	select - returns a list of elements matching a CSS selector

			#	Selector CheatSheet

				#	Select by id of foo: #foo
				#	Select by class of bar: .bar
				#	Select children: div > p
				#	Select descendents: div p



from bs4 import BeautifulSoup
html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>First HTML Page</title>
</head>
<body>
  <div id="first">
    <h3 data-example="yes">hi</h3>
    <p>more text.</p>
  </div>
  <ol>
    <li class="special">This list item is special.</li>
    <li class="special">This list item is also special.</li>
    <li>This list item is not special.</li>
  </ol>
  <div data-example="yes">bye</div>
</body>
</html>
"""
soup = BeautifulSoup(html, "html.parser")

#	This will allways will return a list
print(soup.select("#first"))
# [<div id="first">
# <h3 data-example="yes">hi</h3>
# <p>more text.</p>
# </div>]

#	If you need just the data then you need to select 0nth index
print("\n")

print(soup.select("#first")[0])
# <div id="first">
# <h3 data-example="yes">hi</h3>
# <p>more text.</p>
# </div>
print("\n")

print(soup.select(".special"))
# [<li class="special">This list item is special.</li>, <li class="special">This list item is also special.</li>]
print("\n")

print(soup.select("div"))
# [<div id="first">
# <h3 data-example="yes">hi</h3>
# <p>more text.</p>
# </div>, <div data-example="yes">bye</div>]
print("\n")

print(soup.select("[data-example]"))
# [<h3 data-example="yes">hi</h3>, <div data-example="yes">bye</div>]



#	Selecting Elements by Attribute



#	find an element with an id of foo
soup.find(id = "foo")
#soup.select("#foo")[0]

#	find all elements with a class of bar carefull! "class" is a reserved word in Python
soup.find_all(class_ = "bar")
soup.select(".bar")

#	find all elements with a data attribute of "baz" using the general attrs kwarg
soup.find_all(attrs = {"data-baz": True})
soup.select("[data-baz]")



#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 329. Accessing Data with Beautiful Soup \n")



#	329. Accessing Data with Beautiful Soup



#	Accessing Data in Elements

		#	get_text - access the inner text in an element
		#	name - tag name
		#	attrs - dictionary of attributes
		#	You can also access attribute values using brackets



from bs4 import BeautifulSoup
html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>First HTML Page</title>
</head>
<body>
  <div id="first">
    <h3 data-example="yes">hi</h3>
    <p>more text.</p>
  </div>
  <ol>
    <li class="special">This list item is special.</li>
    <li class="special">This list item is also special.</li>
    <li>This list item is not special.</li>
  </ol>
  <div data-example="yes">bye</div>
</body>
</html>
"""
soup = BeautifulSoup(html, "html.parser")
el = soup.select(".special")[0]

print(el)
# li class="special">This list items is special.</li>

print(el.get_text())
# This list item is special.
print("\n")

for el in soup.select(".special"):
	print(el.name)
	print(el.attrs)
	print(el.get_text())
# li
# {'class': ['special']}
# This list item is special.
# li
# {'class': ['special']}
# This list item is also special.

attr = soup.find("h3")["data-example"]
print(attr)
# yes

attr2 = soup.find("div")["id"]
print(attr2)
# first

attrs3 = soup.find("div").attrs
print(attrs3)
# {'id': 'first'}



#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 330. Navigating With BeautifulSoup \n")



#	330. Navigating With BeautifulSoup



#	Via Tags
		#	parent / parents
		#	contents
		#	next_sibling / next_siblings

#	Via Searching
		#	find_parent / find_parents
		#	find_next_sibling / find_next_siblings
		#	find_previous_sibling / find_previous_siblings



from bs4 import BeautifulSoup
html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>First HTML Page</title>
</head>
<body>
  <div id="first">
    <h3 data-example="yes">hi</h3>
    <p>more text.</p>
  </div>
  <ol>
    <li class="special">This list item is special.</li>
    <li class="special">This list item is also special.</li>
    <li>This list item is not special.</li>
  </ol>
  <div data-example="yes">bye</div>
</body>
</html>
"""



#	Via Tags



soup = BeautifulSoup(html, "html.parser")
data = soup.body.contents[1].contents
print(data)
# ['\n', <h3 data-example="yes">hi</h3>, '\n', '<p> more text</p>', '\n']

#	This example requires to use .next_sibling two times, because in the list after <div> we have '\n'
data2 = soup.body.contents[1].next_sibling.next_sibling
print(data2)
# <ol>
# <li class="special">This list item is special.</li>
# <li class="special">This list item is also special.</li>
# <li>This list item is not special.</li>
# </ol>

data3 = soup.find(class_ = "special").parent.parent
print(data3)
#	this wil renturn whole
#	<body>
#	...
#	</body>



#	Via Searching



#	This method should skip all '\n' and return next object instance
data4 = soup.find(id = "first").find_next_sibling()
print("\n")
print(data4)
# <ol>
# <li class="special">This list item is special.</li>
# <li class="special">This list item is also special.</li>
# <li>This list item is not special.</li>
# </ol>

data5 = soup.find(id = "first").find_next_sibling().find_next_sibling()
print(data5)
# <div data-example="yes">bye</div>

data6 = soup.select("[data-example]")[1].find_previous_sibling()
print("\n")
print(data6)
# <ol>
# <li class="special">This list item is special.</li>
# <li class="special">This list item is also special.</li>
# <li>This list item is not special.</li>
# </ol>

data7 = soup.find(class_ = "special").find_next_sibling(class_ = "special")
print("\n")
print(data7)
# <li class = "special">This list item is also special</li>

data8 = soup.find("h3").find_parent()
print("\n")
print(data8)
# <div id="first">
# <h3 data-example="yes">hi</h3>
# <p>more text.</p>
# </div>

#	This example shous that you can passin argument here to
data9 = soup.find("h3").find_parent("html")
print("\n")
print(data9)
# <html lang="en">
# <head>
# <meta charset="UTF-8">
# <title>First HTML Page</title>
# </head>
# <body>
# <div id="first">
# <h3 data-example="yes">hi</h3>
# <p>more text.</p>
# </div>
# <ol>
# <li class="special">This list item is special.</li>
# <li class="special">This list item is also special.</li>
# <li>This list item is not special.</li>
# </ol>
# <div data-example="yes">bye</div>
# </body>
# </html>



#help(data)



#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 331. Our First Scraping Program \n")



#	331. Our First Scraping Program



#	Requests + Beautiful Soup Example

		#	Let's scape data into a CSV!
		#	Goal: Grab all links from Rithm School Blog
		#	Data: store URL, anchor tag text, and date



import requests
from bs4 import BeautifulSoup
from csv import writer


response = requests.get("https://www.rithmschool.com/blog")
soup = BeautifulSoup(response.text, "html.parser")
articles = soup.find_all("article")

with open("blog_data.csv", "w") as csv_file:
	csv_writer = writer(csv_file)
	csv_writer.writerow(["title", "link", "date"])

	for article in articles:
		a_tag = article.find("a")
		title = a_tag.get_text()
		url = a_tag["href"]
		date = article.find("time")["datetime"]
		csv_writer.writerow([title, url, date])
		print(title, url, date)





#	================================================================================================
#	================================================================================================
#	================================================================================================



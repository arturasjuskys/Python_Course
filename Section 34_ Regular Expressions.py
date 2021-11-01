


#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - Section 34: Regular Expressions \n")



#	Section 34: Regular Exressions



#	339. Intro To Regular Expressions
#	340. Writing Basic Regex
#	341. Regex Basics: Quantifiers
#	342. Regex Basics: Character Classes and Sets
#	343. Regex Basics: Anchors and Boundries
#	344. Regex Basics: Logical Or and Capture Groups
#	345. Introduction to the RE Module
#	346. Validating Phone Numbers With Python
#	348. Parsing URLs with Python
#	350. Symbolic Group Names
#	352. Regex Compilation Flags
#	353. Regex Substitution Basics
#	355. Swapping File Names



#	Coding Exercise 104: Time Validating
#	Coding Exrcise 105: Parsing Bytes Exercise
#	Coding Exercise 106: Date Parsing Exercise
#	Coding Exercise 107: Regex Profanity Filter



#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 339. Intro To Regular Expressions \n")



#	339. Intro To Regular Expressions



#	A way of describing patterns within search strings

#	Validating eMails
	#	Possibly Valid eMails
		#	colt@gmail.com
		#	carly.simon@yahoo.com
		#	rosa-98@meals.org
		#	shoe_queen91@hello.net
		#	david+lee+roth@hotmail.com

		#	Starts with 1 or more letter, number, +, _, -, . then
		#	A single @ sign then#
		#	1 or more teller, number, or - then
		#	A single dot then
		#	ends with 1 or more letter, number, -, or .
		
		#	(^[a-zA-Z0-9_.+-]+@[a-zA-z0-9-]+\.[a-zA-z0-9-.]+$)
		#	^^^^^^^              ^^^^^^^          ^^^^^^^
		#	this would not work on its own in python, and this is not a pyrthon specific code as well

#	Potential Use Cases
		#	Credit Card number validating
		#	Phone number validating
		#	Advanced find/replace in text
		#	Formating text/outup
		#	Syntax highlight



#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 340. Writing Basic Regex \n")



#	340. Writing Basic Regex



#	Regex have different flavours tailored for different programiong languages
#	To write any regex code you can use online regex editors for Python

#	Some Regex Syntax
		#	\d	digit 0-9
		#	\w	letter, digit, or underscore
		#	\s	whitespace character
		#	\D	not a digit
		#	\W	not a word character
		#	\S	not a whitespace character
		#	.	 any character except line break



#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 341. Regex Basics: Quantifiers \n")



#	341. Regex Basics: Quantifiers



#	Some Regex Syntax
		#	+	    One or more
		#	{3}	  Exactly times. {3} - 3 times
		#	{3,5}	Three to five times
		#	{4,}	 Four or more times
		#	*	    Zero or more times
		#	?	    Once or none (optional)



#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 342. Regex Basics: Character Classes and Sets \n")



#	342. Regex Basics: Character Classes and Sets



#	[]	used to define a range of any characters defined in then as a selector
		#	[a-z0-9A-z]	this will select all letters lower case and upper case and all the numbers form 0 to 9.



#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 343. Regex Basics: Anchors and Boundries \n")



#	343. Regex Basics: Anchors and Boundries



#	Some Regex Syntax
		#	^	 Start of string or line
		#	$	 End of string or line
		#	\b	Word boundry



#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 344. Regex Basics: Logical Or and Capture Groups \n")



#	344. Regex Basics: Logical Or and Capture Groups



#	Logical or
		#	|	(pipe character)
			#	"Mr|Mrs|Ms"



#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 345. Introduction to the RE Module \n")



#	345. Introduction to the RE Module



#	Using Regex with Python



import re

#	define our phone number regex
phone_regex = re.compile(r'\d{3} \d{3}-\d{4}')    #     this r before a regex tring is required to prevent python from using \ as an escape characted (without r you will have to use \\ of them to write a regex code)

print(phone_regex)
# re.compile('\\d{3} \\d{3}-\\d{4}')
print(type(phone_regex))
# <class 're.Pattern'>

# help(phone_regex)

#	search a string with our regex
result1 = phone_regex.search('Call me at 415 555-4242')

print(result1)
# <'re.Match object; span=(11, 23), match='415 555-4242'>
print(result1.group())
# 415 555 4242

result2 = phone_regex.search('Call me at 415 555-4242 or 310 234-9999')
print(result2.group())
# 415 555 4242    #    <<<===    search will return 1st match

result3 = phone_regex.findall('Call me at 415 555-4242 or 310 234-9999')
print(result3)
# ['425 555-4242', '310 234-9999']



#	Another way of using Regex is to define them in search line of code



print(re.search(r'\d{3} \d{3}-\d{4}', 'call me at 310 445-9876').group())
# 310 445-9876



#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 346. Validating Phone Numbers With Python \n")



#	346. Validating Phone Numbers With Python



import re

def extract_phone(input):
	phone_regex = re.compile(r'\b\d{3} \d{3}-\d{4}\b')
	match = phone_regex.search(input)
	if match:    #    <<<===    this is to catch error message
		return match.group()
	return None

print(extract_phone("my number is 432 567-8976"))
print(extract_phone("my number is 432 567-897654"))
print(extract_phone("432 567-8976 sdgsdh"))
print(extract_phone("432 567-8976"))
# 432567-8976
# None
# 432567-8976
# 432567-8976



def extract_all_phones(input):
	phone_regex = re.compile(r'\b\d{3} \d{3}-\d{4}\b')
	return phone_regex.findall(input)

print(extract_all_phones("my number is 432 567-8976 or call me at 345 666-7899"))
print(extract_all_phones("my number is 432 567-89766 or call me at 345 666-78999"))
# ['432 567-8976', '345 666-7899']
# []



def is_valid_phone1(input):
	phone_regex = re.compile(r'^\b\d{3} \d{3}-\d{4}\b$')    #    <<<===    need to define a start and finish point of the thing i want to validate
	match = phone_regex.search(input)
	if match:    #    <<<===    this is to catch error message
		return True
	return False


print("\nis_valid_phone1():")
print(is_valid_phone1("432 567-8976"))
print(is_valid_phone1("432 567-8976 asdasd"))
print(is_valid_phone1("dsf 432 567-8976"))
# True
# False
# False



def is_valid_phone2(input):
	phone_regex = re.compile(r'\b\d{3} \d{3}-\d{4}\b')
	match = phone_regex.fullmatch(input)    #    <<<===    here you dont need start and finish point in regex expresion
	if match:    #    <<<===    this is to catch error message
		return True
	return False

print("\nis_valid_phone2():")
print(is_valid_phone1("432 567-8976"))
print(is_valid_phone1("432 567-8976 asdasd"))
print(is_valid_phone1("dsf 432 567-8976"))
# True
# False
# False



#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - Coding Exercise 104: Time Validating \n")



#	Coding Exercise 104: Time Validating



import re

def is_valid_time(input):
	"""
	is_valid_time("10:45")       # True
	is_valid_time("1:23")        # True
	is_valid_time("10.45")       # False
	is_valid_time("1999")        # False
	is_valid_time("145:23")      # False

	In order to return True, the string should ONLY contain the time, and no other characters
	is_valid_time("it is 12:15") # False
	is_valid_time("12:15")       # True

	Don't worry about impossible times like 88:76, just focus on the formatting!
	is_valid_time("34:55")       # True
	"""
	result = re.compile(r'^\d\d?:\d{2}$')
	match = result.search(input)
	if match:
		return True
	return False



#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 348. Parsing URLs with Python \n")



#	348. Parsing URLs with Python



#	This is allows characters in a url, everything in Regex expresion:
		# re.compile(r'https?://www\.[A-Za-z-]{2,256}\.[a-z]{2,6}[-a-zA-Z0-9@:%_\+.~#?&//=]*')
		#    ^^^             ^^^^^^^^     ^^^^^      ^^^^^^^^^^^^^^^^^^^^^^^
		# optional https     domain        .com or .lt      /main or /search/?q=....
		

import re

url_regex = re.compile(r'https?://www\.[A-Za-z-]{2,256}\.[a-z]{2,6}[-a-zA-Z0-9@:%_\+.~#?&//=]*')
match1 = url_regex.search("http://www.youtube.com/videos")

print(match1.group())
# http://www.youtube.com/videos



url_regex = re.compile(r'(https?)://(www\.[A-Za-z-]{2,256}\.[a-z]{2,6})([-a-zA-Z0-9@:%_\+.~#?&//=]*)')
match2 = url_regex.search("http://www.youtube.com/videos")

print(match2.groups())
# ('http', 'www.youtube.com', '/videos')
print(match2.group(0))
print(match2.group(1))
print(match2.group(2))
print(match2.group(3))
# http://www.youtube.com
# http
# www.youtube.com
# /vidoes



#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - Coding Exrcise 105: Parsing Bytes Exercise \n")



#	Coding Exrcise 105: Parsing Bytes Exercise




import re
def parse_bytes(input):
	"""
	parse_bytes("11010101 101 323")                 # ['11010101']
	parse_bytes("my data is: 10101010 11100010")    # ['10101010', '11100010']
	parse_bytes("asdsa")                            # []
	"""
	result = re.compile(r'\b\d{8}\b')
	return result.findall(input)

print(parse_bytes("11010101 101 323"))
print(parse_bytes("my data is: 10101010 11100010"))
print(parse_bytes("asdsa"))


#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 350. Symbolic Group Names \n")



#	350. Symbolic Group Names



def parse_name1(input):
	name_regex = re.compile(r'^(Mr\.|Mrs\.|Ms\.|Mdme\.) ([A-Za-z]+) ([A-Za-z]+)$')
	matches = name_regex.search(input)
	print(matches.group(2))

parse_name1("Mrs. Tilda Swinton")



#	this example shows how you can use lables to mark things
def parse_name2(input):
	name_regex = re.compile(r'^(Mr\.|Mrs\.|Ms\.|Mdme\.) (?P<first>[A-Za-z]+) (?P<last>[A-Za-z]+)$')    #    <<<===    ?P<name>    'name'    is just a name you can use
	matches = name_regex.search(input)
	print(matches.group('first'))    #    <<<===
	print(matches.group('last'))
parse_name2("Mrs. Tilda Swinton")
# Tilda
# Swinton



#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - Coding Exercise 106: Date Parsing Exercise \n")



#	Coding Exercise 106: Date Parsing Exercise



def parse_date(input):
	"""
	parse_date("01/22/1999") # {'d': '01', 'm': '22', 'y': '1999'}

	Note: the string should be an EXACT match, containing the date and nothing else. If there is no match, return None
	parse_date("12,04,2003")  #{'d': '12', 'm': '04', 'y': '2003'}
	parse_date("12.11.2003")  #{'d': '12', 'm': '11', 'y': '2003'}
	parse_date("12.11.200312") #None
	"""
	result = re.compile(r'^(?P<day>\d{2})(/|\.|,)(?P<month>\d{2})(/|\.|,)(?P<year>\d{4})$')
	match = result.search(input)
	if match:
		return {
			'd': match.group('day'),
			'm': match.group('month'),
			'y': match.group('year')
		}
	None

print(parse_date("01/22/1999"))



#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 352. Regex Compilation Flags \n")



#	352. Regex Compilation Flags



#	re.VERBOSE

#	in this compilation flag, there is a method called VERBOSE, which allows you to make comments and write regex on multiple lines to make it more readable
pat = re.compile(r'^([a-z0-9_\.-]+)@([0-9a-z\.-]+)\.([a-z\.]{2,6})$')

pattern1 = re.compile(r"""
	^([a-z0-9_\.-]+)	#	first part of email
	@				   #	sinlge @ sign
	([0-9a-z\.-]+)	  #	email provider
	\.				  #	single period
	([a-z\.]{2,6})$	 #	com, org, net, ect.
""", re.VERBOSE)    #    <<<===    re.VERBOSE or re.X
match1 = pattern1.search("thomas123@yahoo.com")
print(match1.group())
print(match1.groups())
# thomas123@yahoo.com
# ('thomas123', 'yahoo', 'com')



#	re.IGNORECASE

pattern2 = re.compile(r"""
	^([a-z0-9_\.-]+)	#	first part of email
	@				   #	sinlge @ sign
	([0-9a-z\.-]+)	  #	email provider
	\.				  #	single period
	([a-z\.]{2,6})$	 #	com, org, net, ect.
""", re.VERBOSE | re.IGNORECASE)    #    to use multiple flags u need to use '|' sign
match2 = pattern2.search("Thomas123@yahoo.com")
print(match2.group())
print(match2.groups())
# Thomas123@yahoo.com
# ('Thomas123', 'yahoo', 'com')



#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 353. Regex Substitution Basics \n")



#	353. Regex Substitution Basics



import re

text = "Last night Mrs. Daisy and Mr. White murdered Ms. Chow"

pattern = re.compile(r'(Mr\.|Mrs\.|Ms\.) [a-z]+', re.IGNORECASE)
match1 = pattern.findall(text)
print(match1)
# ['Mr.', 'Mrs.', 'Ms.']
match2 = pattern.search(text).group()
print(match2)
# Mrs. Daisy
result1 = pattern.sub("REDACTED", text)
print(result1)
# Last night REDACTED and REDACTED murdered REDACTED



text = "Last night Mrs. Daisy and Mr. White murdered Ms. Chow"

pattern = re.compile(r'(Mr\.|Mrs\.|Ms\.) ([a-z])[a-z]+', re.IGNORECASE)    #    <<<===    grouping just one letter will allow to select it later in the code
match1 = pattern.findall(text)
result2 = pattern.sub("\g<1> \g<2>", text)    #    here im selecting the title and the 1st letter of the name which I grouped earlier in the code
print(result2)
# Last night Mrs. D and Mr. W murdered Ms. C



#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - Coding Exercise 107: Regex Profanity Filter \n")



#	Coding Exercise 107: Regex Profanity Filter




def censor(input):
	"""
	censor("Frack you")                #"CENSORED you"
	censor("I hope you fracking die")  #"I hope you CENSORED die"
	censor("you fracking Frack")       #"You CENSORED CENSORED"
	"""
	result = re.compile(r'(\bfrack\b|\bfracking\b)', re.IGNORECASE)
	match = result.sub('CENSORED', input)
	print(match)
censor("Frack you")
censor("I hope you fracking die")
censor("you fracking Frack")



#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 355. Swapping File Names \n")



#	355. Swapping File Names



import re

titles = [
	"Significant Others (1987)",
	"Tales of the City (1978)",
	"The Day of Ann Madrigal (2014)",
	"Mary Ann in Autumn (2010)",
	"Further Tales of the City (1982)",
	"Babycakes (1984)",
	"More Tales of the City (1980)",
	"Sure of You (1989)",
	"Michael Tolliver Lives (2007)"
]

fixed_titles = []
pattern = re.compile(r'(^[\w ]+) \((\d{4})\)')    #    <<<===    not to get () around the date group date digits before () of the original text
for book in titles:
	result = pattern.sub("\g<2> - \g<1>", book)
	fixed_titles.append(result)
fixed_titles.sort()
print(fixed_titles)
# [
#	'1978 - Tales of the City',
#	'1980 - More Tales of the City',
#	'1982 - Further Tales of the City',
#	'1984 - Babycakes',
#	'1987 - Sugnificant Others',
#	'1989 - Sure of You'
#	'2007 - Michael Tolliver Lives',
#	'2010 - Mary Ann in Autumn',
#	'2014 - The Day of Ann Madrigal'
# ]



#	================================================================================================
#	================================================================================================
#	================================================================================================



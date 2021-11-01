


#	================================================================================================
#	================================================================================================
#	================================================================================================



#	Section 22: Modules



#	214. Section Introduction
#	215. Working With Built-In Modules
#	218. Custom modules
#	220. Installing External Modules And TermColor
#	221. ASCII Art Exercise
#	222. Using The autopep8 Package to Clean Up Code
#	223. The Mysterious __name__ variable


#	Coding Exercise 73: Built In Modules Exercise
#	Coding Exercise 74: Built-In Modules: Slightly Tougher Challenge
#	Coding Exercise 75: Custom Module Exercise



#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n___   ___   ___   215. Working With Built-In Modules   ___   ___   ___\n")



#	215. Working With Built-In Modules



import random
random_choice = random.choice(["apple", "banana", "cherry", "durian"])
print(f"random shuffle {random_choice}")



import random as omg_so_random
so_random_choice = omg_so_random.choice(["apple", "banana", "cherry", "durian"])
print(f"random shuffle {so_random_choice}")



#	Importing Parts of a Module



#	The FROM keyword lets you import parts of a module
#	Handy rule of thumb: only import what you need!
#	If you still want to import everything, you can also use the from MODULE import * pattern



from random import choice, randint
print(choice(["apple", "banana", "cherry", "durian"]))
print(randint(1, 100))



from random import choice as gimme_one, randint as magic_number_chooser
print(gimme_one(["apple", "banana", "cherry", "durian"]))
print(magic_number_chooser(1, 100))



#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n___   ___   ___   218. Custom modules   ___   ___   ___\n")



#	218. Custom modules



import helper
helper.say_hi()    #    <<<===    importing function from external module



from helper import sing_happy_birthday as b_day

print(b_day())



#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n___   ___   ___   220. Installing External Modules And TermColor   ___   ___   ___\n")



#	220. Installing External Modules And TermColor



#	PIP
#	python3 -m pip install NAME_OF_PACKAGE
#	python3 -m pip install termcolor
#	python3 -m pip install colorama



import termcolor

print("\n            print(dir(termcolor))\n")
print(dir(termcolor))
# ['ATTRIBUTES', 'COLORS', 'HIGHLIGHTS', 'RESET', 'VERSION', '__ALL__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'colored', 'cprint', 'os', 'print_function']



print("\n\n\n            help(termcolor)\n\n\n")
help(termcolor)
# NAME
#     termcolor - ANSII Color formatting for output in terminal.

# # FUNCTIONS
#     colored(text, color=None, on_color=None, attrs=None)
#         Colorize text.
        
#         Available text colors:
#             red, green, yellow, blue, magenta, cyan, white.
        
#         Available text highlights:
#             on_red, on_green, on_yellow, on_blue, on_magenta, on_cyan, on_white.
        
#         Available attributes:
#             bold, dark, underline, blink, reverse, concealed.
        
#         Example:
#             colored('Hello, World!', 'red', 'on_grey', ['blue', 'blink'])
#             colored('Hello, World!', 'green')
    
#     cprint(text, color=None, on_color=None, attrs=None, **kwargs)
#         Print colorize text.
        
#         It accepts arguments of print function.

# DATA
#     ATTRIBUTES = {'blink': 5, 'bold': 1, 'concealed': 8, 'dark': 2, 'rever...
#     COLORS = {'blue': 34, 'cyan': 36, 'green': 32, 'grey': 30, 'magenta': ...
#     HIGHLIGHTS = {'on_blue': 44, 'on_cyan': 46, 'on_green': 42, 'on_grey':...
#     RESET = '\x1b[0m'
#     VERSION = (1, 1, 0)
#     __ALL__ = ['colored', 'cprint']
#     print_function = _Feature((2, 6, 0, 'alpha', 2), (3, 0, 0, 'alpha', 0)...

# FILE
#     c:\users\pc\appdata\local\programs\python\python38-32\lib\site-packages\termcolor.py



from termcolor import colored
from colorama import init

init()

text = colored("HI THERE!", color = "magenta", on_color = "on_cyan", attrs = ["blink"])
print(text)



#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n___   ___   ___   221. ASCII Art Excersice   ___   ___   ___\n")



#	221. ASCII Art Excersice



#	Use the pyfiglet package!



import pyfiglet
from termcolor import colored
from colorama import init
init()


valid_colors = ("red", "green", "yellow", "blue", "magenta", "cyan", "white")
msg = input("What would you like to print? ")
color = input("What color? ")

if color not in valid_colors:
	color = "green"

ascii_art = pyfiglet.figlet_format(msg)
colored_ascii = colored(ascii_art, color = color)
print(colored_ascii)



def ascii_art():
	import pyfiglet
	from termcolor import colored
	from colorama import init
	init()

	valid_colors = ("red", "green", "yellow", "blue", "magenta", "cyan", "white")

	msg = input("What would you like to print? ")
	color = input("What color? ")

	if color not in valid_colors:
		color = "green"

	ascii_art = pyfiglet.figlet_format(msg)
	colored_ascii = colored(ascii_art, color = color)
	print(colored_ascii)



#	================================================================================================
#	================================================================================================
#	================================================================================================



#	222. Using The autopep8 Package to Clean Up Code



#	python -m pip install autopep8



#	in powershell
#	autopep8 --in-place FILE_NAME    #    <<<===    this will change the original file
#	^^^    this will fix white spaces in the file    ^^^

#	autopep8 --in-place -aggressive
#	autopep8 --in-place -a
#	^^^    fixes unnecessary code such as
		#	if is_cat_owner == True:
		#	if is_cat_owner is True:



#	There is a Sublime Auto PEP8 Formating Package




#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n___   ___   ___   223. The Mysterious __name__ variable   ___   ___   ___\n")



#	223. The Mysterious __name__ variable



#	When run, every Python file has a __name__ variable
#	If the file is the main file being run, its value is "__main__"
#	Otherwise, its value is the file name



#	Ignoring Code on Import



#if __name__ == "__main__":
	# this code will only run
	# if the file is the main file!



from helper import say_hi
def say_sup():
	print(f"SUP! My __name__ is {__name__}")
if __name__ == "__main__":
	say_hi()
if __name__ == "__main__":
	say_sup()



#	================================================================================================
#	================================================================================================
#	================================================================================================



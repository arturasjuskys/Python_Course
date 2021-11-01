#	================================================================================================
#	================================================================================================
#	================================================================================================



#	146. Defining Functions



def say_hi():
	print(f"Hi! My __name__ is {__name__}")
if __name__ == "__main":
	say_hi()


def sing_happy_birthday():
	print("Happy Birthday To You")
	print("Happy Birthday To You")
	print("Happy Birthday Dear You")
	print("Happy Birthday To You")



#	================================================================================================
#	================================================================================================
#	================================================================================================



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

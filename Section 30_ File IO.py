


#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - Section 30: File IO \n")



#	Section 30: File IO



#	304. Section Introduction
#	306. Reading Files: Seek and Cursors
#	307. The With Statement
#	308. Writing to Text Files
#	309. File Modes



#	Coding Exercise 95: copy
#	Coding Exercise 96: copy_and_reverse
#	Coding Exercise 97: statistics
#	Coding Exercise 98: find_and_replace



#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 306. Reading Files: Seek and Cursors \n")



#	306. Reading Files: Seek and Cursors



		#	You can read a file with a open function
		#	open returns a file object to you
		#	You can rear a file object with the read method



file = open("story.txt")
print(file.read())
# This short story is really short.
print(file.read())
# ' '



#	Cursor Movement

		#	Python reads files by using cursor
		#	This is like the cursor you see when you're typing
		#	After a file is read, the cursor is at the end
		#	To move the cursor, use the seek method



#	.seek()
file = open("story.txt")
file.read()
# This short story is really short.
# Now it's a little longer
# The end.
file.read()
# ' '
file.seek(0)
# 0
file.read()
# This short story is really short.
# Now it's a little longer
# The end.
file.seek(1)
# 1
file.read()
# his short story is really short.
# Now it's a little longer
# The end.



#	.readline()
file.seek(0)
# 0
file.readline()
# This short story is really short.
file.read()
# Now it's a little longer
# The end.
file.seek(0)
# 0
file.readline()
# This short story is really short.
file.readline()
# Now it's a little longer
file.readline()
# The end.
file.readline()
# ' '



#	.readlines()
file.seek(0)
# 0
print(file.readlines())
# ["This short story is really short.\n", "Now it's a little longer\n", "The end\n."]
file.read()
# ' '



#	Closing a File
		#	You can close a file with the close method
		#	You can check if a file is closed with the close attribute
		#	Once closed, a file can't be read again
		#	Always close files - it frees up system resources!



file.read()
# ' '
file.closed
# False
file.close()
file.closed
# True
#file.read()
# ValueError: I/O operation on closed file.



#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 307. The With Statement \n")



#	307. The With Statement



#	with Blocks



#	Option 1
file = open("story.txt")
file.read()
file.close()
print(file.closed)
# True



#	Option 2
with open("story.txt") as file:    #    <<<===    file here is a variables name
	story_data = file.read()
print(file.closed)
# True
print(story_data)
# This short story is really short.
# Now it's a little longer
# The end.



#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 308. Writing to Text Files \n")



#	308. Writing to Text Files

		#	You can also use open to write to a file
		#	Need to specify the "w" (write) flag as the second argument



#	This will create a file if there is no file under that name, or overrides existing fileif it does exist
with open("story2.txt", "w") as file:
	file.write("Writing files is great\n")
	file.write("Here's another line of text\n")
	file.write("Closing now, goodbey!")
with open("story2.txt") as file:
	data = file.read()
	print(data)
# Writing files is great
# Here's another line of text
# Closing now, goodbey!



with open("story3.txt", "w") as file2:
	file2.write("haha " * 1000)



#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 309. File Modes \n")



#	309. File Modes



#	Modes for Opening Files

		#	"r" - open for reading (default)
		#	"w" - open for writing, truncating the file first
		#	"x" - open for exslusive creation, failing if the file already exists
		#	"a" - open for wrtiting, appending to the end of the file is exists
		#	"b" - binary mode
		#	"t" - text mode (default)
		#	"r+" - open a disk file for updating (reading and writing)
		#	"U" - universal newlines mode (deprecated)


#	Original content was:
		#	'I WAS HERE FIRST!'
with open("story4.txt", "r+") as file:
	file.write(":)")
	file.seek(10)
	file.write(":(")
	file.seek(0)
	print(file.read())
# :)WAS HERE:(IRST!



#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - Coding Exercise 95: copy \n")



#	Coding Exercise 95: copy



def copy(original_file, new_file):
	"""
	copy('story.txt', 'story_copy.txt') # None
	# expect the contents of story.txt and story_copy.txt to be the same
	"""
	with open(original_file) as file:
		data = file.read()
	with open(new_file, "w") as file:
		file.write(data)



#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - Coding Exercise 96: copy_and_reverse \n")



#	Coding Exercise 96: copy_and_reverse



def copy_and_replace(original_file, reversed_file):
	"""
	copy_and_reverse('story.txt', 'story_reversed.txt') # None
	# expect the contents of story_reversed.txt to be the reverse of the contents of story.txt
	"""
	with open(original_file) as file:
		data = file.read()[::-1]
	with open(reversed_file, "w") as file:
		file.write(data)



#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - Coding Exercise 97: statistics \n")



#	Coding Exercise 97: statistics



def statistics(file_name):
	"""
	statistics('story.txt') 
	# {'lines': 172, 'words': 2145, 'characters': 11227}
	"""
	with open(file_name) as file:
		lines = file.readlines()
	return {"lines": len(lines),
			"words": sum(len(line.split(" ")) for line in lines),
			"characters": sum(len(line) for line in lines)
	}



#	================================================================================================
#	================================================================================================
#	================================================================================================
print(f"\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - Coding Exercise 98: find_and_replace \n")



#	Coding Exercise 98: find_and_replace



def find_and_replace(file_name, old_word, new_word):
	"""
	find_and_replace('story.txt', 'Alice', 'Colt') 
	# story.txt now contains the first chapter of my new book,
	# Colt's Adventures in Wonderland
	"""
	with open(file_name, "r+") as file:
		text = file.read()
		new_text = text.replace(old_word, new_word)
		file.seek(0)
		file.write(new_text)
		file.truncate()



#	================================================================================================
#	================================================================================================
#	================================================================================================



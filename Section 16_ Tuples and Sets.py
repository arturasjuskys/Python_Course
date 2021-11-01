


#	================================================================================================
#	================================================================================================
#	================================================================================================



#	139. Section Introduction
#	140. Tuple Looping and Methods
#	141. Introduction to Sets
#	142. Set Methods and Set Math
#	144. Set Comprehension and Recap



#	Coding Exercise 36: Tuples and Sets Exercise



#	================================================================================================
#	================================================================================================
#	================================================================================================



#	139. Section Introduction



#	An orderd collection or grouping of items
#	numbers = (1, 2, 3, 4)
#	Tuple is immutable
#	Typles are faster than Lists



x= (1, 2, 3)
3 in x    # True
#x[0] = "change me!"    # TypeError: 'tuple' object does not support item assignment



#    Creating Tuples

numbers1 = (1, 2, 3, 4)
value = (1,)    #    to create tuple with one value you need to include comma at the back
numbers2 = ()
tuple()



months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
months[0]    # 'January'
months[-1]    # 'December'



nums = (1, 2, 3, 3, 3, (4, 5), 6, 7)
print(nums)
# (1, 2, 3, 3, 3, (4, 5), 6, 7)
nums[0]       # 1
nums[3]       # 3
nums[5][1]    # 5
nums[-1]      # 7
nums[-3]      # (4, 5)



#    In this example tuple is set as dictionaries first value

locations = {
	(35.6895, 39.6917): "Tokyo Office",
	(40.7128, 74.0060): "New York Office",
	(37.7749, 122.4194): "San Francisco Office"
}
locations[(37.7749, 122.4194)]    # 'San Francisco'



#	TypeError: unhashable type: 'list'
#locs = {[35, 39]: "Tokyo Office"}

#	in this instance its possible to use tuple instead
locs = {(35, 39): "Tokyo Office"}



#	Some dictionary methods like .items() return tuples
cat = {"name": "biscuit", "age": 0.5, "favorite_toy": "my chapstick"}
cat.items()
#	dict_items([('name', 'biscuit'), ('age': 0.5), ('favorite_toy', 'my chapstick')])
                   # tuple ^^^       # tuple ^^^            # tuple ^^^



#	================================================================================================
#	================================================================================================
#	================================================================================================



#	140. Tuple Looping and Methods



names = ('Colt', 'Blue', 'Rusty', 'Lassie')
for name in names:
	print(name)
# Colt
# Blue
# Rusty
# Lassie



months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
for month in months:
	print(month)
# January
# February
# March
# April
# May
# June
# Juny
# August
# September
# October
# November
# December



months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
i = len(months) -1
while i >= 0:
	print(months[i])
	i -= 1
# December
# November
# October
# September
# August
# July
# June
# May
# April
# March
# February
# January



#    .count()

x = (1, 2, 3, 3, 3)
x.count(1)    # 1
x.count(3)    # 3



#    .index()

t = (1, 2, 3, 3, 3)
t.index(1)    # 0
#t.index(5)    # ValueError: tuple.index(x): x not in tuple
t.index(3)    # 2    only the 1st matching index is returned



#	================================================================================================
#	================================================================================================
#	================================================================================================



#	141. Introduction to Sets



#	Sets are like formasl mathematical sets
#	Sets do not have dublicate values
#	Elements in sets aren't ordered
#	You cannot access items in a set by index
#	Sets can be useful if you need to keep track of a collection of elements, but don't care about ordering, keys or values and duplicates



#    Sets cannot have duplicates
creating_set = set({1, 2, 3, 4, 5, 5, 5})    # {1, 2, 3, 4, 5}
#    Creating new set
creating_new_set = set({1, 4, 5})
#    Alternative
new_set = {1, 4, 5}

4 in new_set   # True
8 in new_set    # False



numbers = {1, 2, 3, 4}
for number in numbers:
	print(number)
# 1
# 2
# 3
# 4



cities = {"Los Angeles", "Florence", "Boulder", "Oslo", "Tokyo", "Santiago", "Tokyo", "San Francisco", "Shanghai", "San Francisco", "Oslo", "Boulder"}
print(list(set(cities)))
# ['Los Angeles', 'Florence', 'Boulder', 'Oslo', 'Tokyo', 'Santiago', 'Shanghai', 'San Francisco']
print(len(set(cities)))
# 8



#	================================================================================================
#	================================================================================================
#	================================================================================================



#	142. Set Methods and Set Math



#    .add()

new_set = set({1, 2, 3})
new_set.add(4)
print(new_set)
# {1, 2, 3, 4}
new_set.add(4)    #    <<<=== adds nothing because there is a value 4 already
print(new_set)
# {1, 2, 3, 4}



#    .remove()

other_set = set({1, 2, 3, 4, 5, 6})
other_set.remove(3)
print(other_set)
# {1, 2, 4, 5, 6}
#other_set.remove(7)    # KeyError: '7'



#    .discard()
#    it will remove the value if it is there, but will not throw an error if the value is not in set

other_set = set({1, 2, 3, 4, 5, 6})
other_set.discard(7)    #    <<<===    removes notrhig because there is no value 7, but doesn't throw an error.
print(other_set)
# {1, 2, 3, 4, 5, 6}



#    .copy()

new_set = set({1, 2, 3})
another_new_set = new_set.copy()
print(another_new_set)
# {1 ,2, 3}
another_new_set is new_set    # False



#    .clear()

another_set = set({1, 2, 3})
another_set.clear()
print(another_set)
# set( )



#    Set Math



#    intersection

math_students = {"Matthew", "Helen", "Prashant", "James", "Aparna"}
biology_students = {"Jane", "Matthew", "Charlotte", "Mesut", "Oliver", "James"}
both_classes = math_students & biology_students
print(both_classes)
# {'James', 'Matthew'}



#    symmetric_difference



#    union

math_students = {"Matthew", "Helen", "Prashant", "James", "Aparna"}
biology_students = {"Jane", "Matthew", "Charlotte", "Mesut", "Oliver", "James"}
both_classes = math_students | biology_students
print(both_classes)
# {'Charlotte', 'Prashant', 'Jane', 'Oliver', 'Mesut', 'Helen', 'Aparna', 'Matthew'} 



#	================================================================================================
#	================================================================================================
#	================================================================================================



#	144. Set Comprehension and Recap
#	{ ___ for ___ in ___ }



#    to create set with set comprehension you need to specifie just one value not to like with dictionaries
value = {val ** 2 for val in range(10)}
print(value)
# {0, 1, 64, 4, 36, 9, 16, 49, 81, 25}



value2 = {char.upper() for char in "hello"}
print(value2)
# {'O', 'L', 'H', 'E'}



if len({char for char in "hello" if char in "aeiou"}) == 5:
	print("True Statment")
else:
	print("False Statment")



#	================================================================================================
#	================================================================================================
#	================================================================================================



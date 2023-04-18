"""
Args and Kwarks are features that allow multiple arguments to be passed to functions. Using the preceding characters of *args or 
**kwarks. They can be renamed to allow for better readability as long as it relates to the intended use. Like below

*args - is an immutable object, thus it cant be changed and will always stay the same. This is because it is a tuple. the '*' allows
the tuple to be unpacked and the values passed through.

**kwarks - acts like a dictionary. Allowing the data to be read easily. As long at the '**' is used preceding the name it allows the data
to be read and passed through to the function. 
"""

def addition(a, b):
    return a + b

print(addition(2,2))

def add_integers(list_integers): # Using a predefined list isn't ideal. Due to having to define the list before passing the argument 
	total = 0                   # to the function. 
	for x in list_integers:
		total += x
	return total

list_integers = [1, 2, 3, 4]
print(add_integers(list_integers))

def add_many_integers(*integers): # args renamed to integers to allow multiple arguments to be multiplied together 
	# Rename *args to something suitable
	total = 0
	for x in integers:
		# As it is a tuple you can use the in keyword to iterate 
		total += x # Simple way of adding all the values passed in from integers together to return the total number 
	return total

print(add_many_integers(1,2,3,4,5,6,7,8,9))

def concatenate_words(**words): # kwarks renamed to words. Allowing multiple words to be added together in a string. 
	result = ""
	# As **kwargs is a dict you need to iterate over .values()
	for arg in words.values():
		result += arg
		result += " "
	return result

print(concatenate_words(a='This', b="is", c="a", d="useful", e="feature"))

# CI Testing

def make_string(*strings):
    return ' '.join(strings) # Joins the string data together using the 'join' keyword.


my_string = make_string("Alderaan", "Coruscant", "Dagobah", "Endor", "Hoth") # Data passed into the function to be made into a string

print(my_string)

def get_age(**data):
    return data.get('age', 'no age provided') # returns tha age that was given to the function by the pats_age variable. By using the 
                                              # get keyword

pats_age = get_age(name="pat", level=4, age=33, occupation="postman")

print(pats_age)

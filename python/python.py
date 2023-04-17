# Same as console.log in JS. Using print statments throughout the code is a good way to catch errors and to see what is going on quickly

print('Hello World')

# System Exit cuts the code and exits the application safely. Just like powering down a pc using the correct process not pulling the plug out

raise SystemExit('Some error Message')
# The above pauses and exits the code based on the statement before its process. Allowing us to look at the errors/place it is at in the code to 
# help catch any bugs or errors 

# Errors

#print 'Hello, World!' Will throw an error as its not correct syntax for the python language. There mut be the brackets in the statment for it to 
# read the code and print the desired outcome

# Variables are defined differently to JS. They are also case sensitive. They can also contain spaces, by using an underscore. Meaning.

myvar = 5 
my_var = 5
# Is a different variable to 
myVar = 5
my_Var = 5
# all of the above variables are completely different despite essentially having the same names and values assigned to them

# True/False
# In Python Booleans are defined by using the true and false keywords. But the first letter of each must be capitalized

# Tuple is a list or item that is unchangeable and will always stay the same. The same concept as a const variable in JS

# Dictionaries are the same as objects and defined in the same way in the as objects in JS using the {":"}

# Accessing data from a dictionary 

data = {
    "first_name": "Arthur",
    "last_name": "Dent",
    "species": "Human"
}

# add your code here
name = data['first_name'] # Assigning a new variable and adding the data from the dictionary to that variable using [] notation

species = data['species']

data['age'] = 42 # Assigning a new key to the object of data. And adding in its value 

print(name)
print(species)

# this will print the data to the terminal
print(data)


# List comprehension 

letters = [i for i in 'Marvin'] # Instead of creating an entire for loop to loop through. This allows it to be compressed into a single line

print(letters)


"""
Multi line comments can be made and implemented into python by using three double quotation marks. At the beginning and ending of the
comment itself. Allowing for as much or as little space as needed. If writing a comment inside a function or a loop it should be 
indented the same amount as the current scope of the code. 
"""

# Single line comments are created by using the hash key symbol
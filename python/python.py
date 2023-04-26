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


# Random code


def multiply_numbers(num1, num2):
    sum = num1 * num2 # Multiplies the numbers given in the results variable 
    return sum
    
results = multiply_numbers(5, 4) #Calls the function and stores the inputs required to be multiplied together

print(results)


def object_1(name):
    print(f"hello World {name} ")
    
    
username = input("What is your name")    

object_1(username)

"""
Using the global keyword allows a variable from the global scope to be accessed and modified inside a function/in the local scope. 
Both examples below will output a different result. In the first one the global variable isn't redefined as it was defined as a local 
scope variable as well as the global scope variable. 

Ensuring to give access to the variable by declaring it at the start of the function by saying 'global some_var_name' before going 
on to use the variables data or modifying the data 
"""
can_access = False
	
def update_access():
    age = int(input('Enter your age: '))
    if age >= 18:
        # We may think this is updating the global variable can_access, but its not as it is now considered a local variable
        can_access = True
        return('You are old enough enter')
    else:
        return('You are too young, you may not enter');

update_access()

print(can_access) # will still print out False

can_access = False
	
def update_access():
    global can_access # Global allows a global scope variable to be accessed inside of the function which allows the modification
    age = int(input('Enter your age: '))
    if age >= 18:
        # The global keyword is used
        can_access = True
        return('You are old enough to enter')
    else:
        return('You are too young, you may not enter');

update_access()

print(can_access) # will now print True if an age >= 18 is entered

"""
The same is done with the 'nonlocal' scope keyword. Meaning that if there is a nested function inside a function we can use that keyword
to give the nested function access to the parents variable. Again making sure to define it at the start of the function before using it
"""

# This one will give an error as it doesn't have access to the parents variables 
def which_scope():
    my_age = 49 # local variable my_age
    def inner_scope():
        my_age += 1 # Issue when we try to run this line.
        print(my_age)
    inner_scope()

which_scope()

def which_scope():
    my_age = 49 # local variable my_age
    def inner_scope():
        nonlocal my_age # nonlocal allows the nested function to have access to the parents variables 
        my_age += 1 # Issue when we try to run this line.
        print(my_age)
    inner_scope()

which_scope()

"""
Python Decorators are special characters that allow functions to be modified by other functions.
"""

def add_author(func):
    """
    Decorator to add string with author information
    to print after decorated function runs
    """
    def wrapper(*args):
        r = func(*args)
        return f"{r}\nBy Code Institute"
    return wrapper
        
# write your code here

@add_author # The decorator adds in the title of the article to the function. 
def print_article_title(title):
    return f"Article Title {title}"
    
result = print_article_title("Python Decorators")

print(result)

numbers = [12, 45, 60, 87, 999, 200, 84, 42, 87, 77, 2, 3, 77, 99, 20]


def odd_numbers(list_of_nums): 
    new_list = []
    for nums in list_of_nums:
        if nums % 2 != 0: # Ensuring to check if it is equal or not equal to 0 to ensure that it is passed to the intended place
            new_list.append(nums) # Append method is adding the new nums list to the new_list variable allowing for a print method
        
    print(new_list) # prints the new_list to the console. Outside of the for loop.
        
odd_numbers(numbers)

"""
When creating a python program we divide and split our functions into different files to avoid repetition of code across the application.
This not only keeps the code looking cleaner and easier to read it also allows us to reusable code into different files. Or importing 
libraries of code to your code.  
"""

from division import divide 
# first is the file name and the second is the method/functions to import. Or for access to multiple functions/methods

import division
# gives access to everything inside the division file. meaning to use anything you'd need division.divide to access the divide method
# etc...

"""
Math - Gives us access to all the math functionality of pythons math module - Checking the docs for all information
import math
"""

math.pi
math.random
math.abs
math.floor
math.ceil
math.round
math.pow
math.sqrt
math.min
math.max

# Just a few of the functions we can access

"""
Date and time - Gives access to the date and time functionality of the datetime module. Allowing us to get the exact date and time
at any required place.
Remembering to check the docs for all relevant information
"""

from datetime import datetime

# write your code here

today = datetime.now().date()

print(today)


"""
Try and Except statements are code blocks that allow us to throw an error to allow us to determine what has gone wrong based on an input 
for example. They can be strung together like below. Or they can be a single try except. It also allows us to execute certain code based
on the error that was thrown. 
"""

while True:
    try:
        a = int(input("Please enter an integer as the numerator: "))
        b = int(input("Please enter an integer as the denominator: "))
        print(a / b)
    except ZeroDivisionError:
        print("Please enter a valid denominator.")
    except ValueError:
        print("Both values have to be integers.")
    except Exception:
        print('Another error has occurred')
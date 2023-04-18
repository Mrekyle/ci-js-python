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
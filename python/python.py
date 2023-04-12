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
# all of the above variables are compleatly different despite essentially having the same names and values assigned to them

# True/False
# In Python Booleans are defined by using the true and false keywords. But the first letter of each must be capataised

# Data types

print(type("Hello, World!")) # string
print(type(42)) # number/integer
print(type(3.145)) # float
print(type(1j)) # complex number
print(type(["egg", "bacon", "spam"])) # list
print(type(("egg", "bacon", "spam"))) # turple
print(type(range(6))) # range
print(type({"name" : "John", "age" : 80})) # dictionary
print(type({"egg", "bacon", "spam"})) # set
print(type(True)) # bool
print(isinstance(3.14, int)) # false - because that is a float not an integer


# Just like in Javascript you can interchange the quotation marks between double and single. Depending on what need the string has
# for different punctuation. Wrapping one inside the other allows different types of punctuation. "''" or '""'.

int() # Converts a string into an integer/Number
float() # Converts a string into a floating number (Decimal point number )
str() # Converts a number or a float into a string 

# This is also done with ther other datatypes that are avaliable in the Python language. Defined by the respective function

first_number = input("Input your first number:")
second_number = input("Input your second number:")

print(first_number + second_number) # Prints out the string from the variable and an input box into the terminal. Because in Python
# The '+' is used to concantenate the strings together resulting in the inputs being pushed together

first_number = int(input("Input your first number:")) # The int function converts the string that is receives into the integer to
second_number = int(input("Input your second number:")) # Multiply both inputs received

print(first_number + second_number) # resulting in the output being the sum of both user inputs

# Data type conversion 

result = 40 + float("2.2") # Type conversion is done on the variable data not in the call of the variable.
print(result)

result_two = "The answer to the ultimate question is " + str(42)
print(result_two)


print('rat' in 'crate') # in Checks if the word from the statment is in the other. Can be done with variables and all data types
print('ink' not in 'sink') # checks if 'ink' is in the string of 'sink' But as it is not specifically in the string - returns false 
print('robbie' in ['gary', 'howard', 'mark', 'jason']) # Checks if the name robbie is in the list of names - Returns false




# Defining functions in Python is different to JS. Firstly to define a function you use the def keyword and then the functions name.
# They can also take different paramaters like JS inside the brackets. Then by using indentation you tell the language that the code 
# belongs to the function above. 

def print_message():
    print('Hello World')

print_message() # Calls the function of print message. Similar to the way JS Functions are called

# Functions can be created in seperate files and imported into a different file calling them modules.
# For example we can create a file that contains all types of math calculations. Save it and import it into a different file. Allowing 
# Us to then call any of the functions inside the other file to use in our main file. Similar to the was we do in JS/CSS/HTML
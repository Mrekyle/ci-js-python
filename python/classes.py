"""
Classes are a lot like functions in the way they need to be defined by a certain keyword and called upon. They follow some rules such as
They must have a capital letter for the first letter of the name and must have docstring.

They allow us to hold large pieces of information such as multiple car objects.

Docstrings can br created with either the double quotation marks or the single quotation marks.
"""


class HelloWorld:
    '''A docstring must be created inside of the class. And must be indented in the same scope to be inside the defining area'''
    print('Hello World')


"""
When a class holds a function inside of it. It is referred to as a method of that class. 

Using the __init__() function allows us to create an object with certain parameters. Such as creating a car object.

"""

class Car:
	def __init__(self, color, make, model, fueltype): # Passing the self keyword allows it to be used inside the function. Same as the this keyword in JS
		self.color = color
		self.make = make
		self.model = model
		self.fueltype = fueltype

bullitt = Car('Green', 'Ford', 'Mustang', 'Gasoline') # Passing the different arguments allows a class to be created with the defined arguments

# write your code here
class Customer:
    '''Creates an instance of Customer'''
    def __init__(self, fname, lname, email, phone):
        self.fname = fname
        self.lname = lname # Ensuring to add arguments in the same order to line up with the inputted date from the variable
        self.email = email
        self.phone = phone


# The code below will use your class to print values to the terminal after
# it has been written. Comment the lines below back in to test it

customer_one = Customer("Theon", "Greyjoy", "t.gj@email.com", "123456789")
print(customer_one)
print(customer_one.fname) # Using '.' notation to access the fname inside the class object
print(customer_one.lname)
print(customer_one.email)
print(customer_one.phone)

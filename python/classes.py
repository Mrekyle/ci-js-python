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
        self.phone = phone # self keyword is the same as the 'this' keyword in JS. To be used must be passed as an argument


# The code below will use your class to print values to the terminal after
# it has been written. Comment the lines below back in to test it

customer_one = Customer("Theon", "Greyjoy", "t.gj@email.com", "123456789")
print(customer_one)
print(customer_one.fname) # Using '.' notation to access the fname inside the class object
print(customer_one.lname)
print(customer_one.email)
print(customer_one.phone)

'''
Code institute class coding challenge 
'''
       
# Write your code here
class OrderItem:
    '''Creates an instance of OrderItem'''
    def __init__(self, item, price, quantity):
        self.item = item
        self.price = price
        self.quantity = quantity
        
    def description(self):
        '''Describe the OrderItem'''
        return f"{self.quantity} x {self.item} at ${self.price} each" # Using an f string allows us to string multiple items from the object
                                                                      # together into a single string 


# The code below will use your class to print values to the terminal after 
# it has been written. Comment the lines below back in to test it  

order_item_one = OrderItem("bowtie", 10, 3) # Ensuring the list items are in the correct order for the init function to work correctly
print(order_item_one.description())

order_item_two = OrderItem("Fez", 25, 1)
print(order_item_two.description())


"""
The above class of Bird allow us to return a statement of saying that the kind of the owl makes a certain call. dependent on the variables 
"""


"""

In Python classes can have multiple instances of the same object. Allowing data to be overwritten and used but also have the previous
date still in memory. Such as below 

"""

class Bird:
   """
   Bird class
   """
   def __init__(self, kind, call):
      #properties
       self.kind = kind
       self.call = call

   #behaviour
   def description(self):
       """
       describe the bird
       """
       return f"A {self.kind} goes {self.call}" 
  
   def bird_call(self):
       print(self.call.upper()) # Transforming the firs letter of the word into uppercase text.

owl = Bird('Owl', 'Twit Twoo!')
print(owl.call)
print(owl.description())
crow = Bird('Crow', 'Caaaw!')
print(crow.description())
owl.call = 'screech'
print(owl.description())
del owl.call # The del keyword also allows us to delete certain data from the object. And re define it if wanted at a later date
# Any code below this will not execute as an error has been thrown. Causing the program to stop at the error
print(owl.description())

hawk = ('Hawk', 'Cawww')
print(hawk.description())

"""
With classes you can create subclasses of a certain class just by passing it as a parameter of the new class being created. Allowing the
use of all the data inside of the parent class inside of the sub class
"""

class Bird:
    """
    Bird class
    """
    # class attribute
    definition = "a warm-blooded egg-laying vertebrate animal distinguished by the possession of feathers, wings, a beak, and typically by being able to fly."

    def __init__(self, kind, call):
        # instance attribute
        self.kind = kind
        self.call = call

    def description(self):
        """
        describe the bird
        """
        return f"A {self.kind} goes {self.call} and is {self.definition}" 


class Parrot(Bird): # Subclass of the Bird class. By passing it as a argument of the class of parrot allowing the use of all the code in
    def __init__(self, color): # the parent class to be passed. Once data is passed it will use the parents class to use the data.
        Bird.__init__(self, 'Parrot', 'Kah!') # ensuring everything is in the correct order 
        self.color = color


parrot = Parrot('blue')
print(parrot.color)
print(parrot.description())

"""
Class composition uses the base concept of a subclass. In the way you can string multiple classes together by passing them in the same way
but if needed classes can be left out. Such as below. The VW has an internal combustion engine, so it needs them properties to have them
passed. Whereas the tesla doesn't need it.
"""

class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

class Engine:
    def __init__(self, capacity, fuel):
        self.capacity = capacity
        self.fuel = fuel
    
class InternalCombustion(Vehicle, Engine):
    def __init__(self, make, model, capacity, fuel):
        Vehicle.__init__(self, make, model)
        Engine.__init__(self, capacity, fuel)
        
class Electric(Vehicle):
    def __init__(self, make, model):
        Vehicle.__init__(self, make, model)
        
volkswagen = InternalCombustion("Volkswagen", "Golf", 1.7, "Diesel")
tesla = Electric("Tesla", "X")
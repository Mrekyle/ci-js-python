number = int(input("Please enter a number:"))

if number == 5:
    print(f"{number} is equal to 5")
else:
    print(f"{number} is not equal to 5")


# Similar to js if else statments. Just no curly braces involved all based upon the indentation of the statments below the if and the else
# Rememebing that the ending of the conditional statment is ended by a ':' meaning thatss the end of the condition and to carry on with the 
# intended code below

a = 10
b = 20
result = None

# Write your if statement here:
if a == b:
    result = 'a has the same value as b' # Displays if a is the same value as the b variable
else:
    result = 'a has not got the same value as b' # Displays when a is NOT the same as the b variable


print(result)

# Short hand if else statment in Python

my_boolean = False

my_string = "Hello" if my_boolean else "World"
# Evaluates the second conditional statment first. If that returns True then it will evaluate the first statment. If it returns false it will
# Evaluate the else statment
print(my_string)


# Simple else if statment - Checks if the inputted number is divisible by the set conditions and prints a result based on the answer
num = int(input('Whats your favourite number?')) # Takes a terminal input and converts it to an integer 
# For it to check if its divisible it needs to return 0 meaning that it is fully divisible. Using the and condition allows multiple conditions
if num % 3 == 0 and num % 5 == 0: # Divisible by 3 or 5
    print('FizzBuzz')
elif num % 3 == 0: # Divisible by 3
    print('Fizz')
elif num % 5 == 0: # Divisible by 5
    print('Buzz')
else: # If not divisible by either 3 or 5 
    print('Your number is not divisible by 3 or 5, your number is:', num)

# Else if done with comparing the data inside the variable using strings

day = 'Friday'

if day == 'Monday':
    print('Meeting at 9:00')
elif day == 'Wednesday':
    print('Meeting at 2:00')
elif day == 'Friday':
    print('Meeting at 4:00')
else:
    print('No meetings today')


# For Loops

languages = ["HTML", "CSS", "JavaScript"]
for language in languages: # Assigning each item in the list to the language variable and printing to the console. Until the list is finished
  print(language)


for character in "Python":
  print(character) #  Same concept here, Just each letter is being printed to the console as there is no list/arrary to iterate over
  # It iterates over the individual characters

users = ['anna', 'chris', 'brian']
for i in range(len(users)): # Loops over the users variable and assigns it to the 'i' Variable
    users[i] = users[i].capitalize() # Capitalizes the first letter of each name in the users list
    
print(users)

    




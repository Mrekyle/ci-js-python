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

# While loops

counter = 0

while counter < 10: # Checks if counter is less than 10
    print(counter) # prints out the current state of the counter variable
    counter += 1 # adds one to the count of the counter variable 

# The above while loop prints out the number 0 to 9 due to the counting method of the language. 

# break allows the loop to be stopped by an external condition if that condition has been met 
for number in range(10):
    if number == 5:
        break    # break here

    print(f'Number is  {number}') 

print('Left the loop') # Exits the loop at the break once the condition of number being 5 

# continue allows a specific part of a loop to be skipped over due to an external condition. But will restart the loop again when called 
for number in range(10):
    if number == 5:
        continue    # continue here

    print(f'Number is  {number}')

print('Left the loop') # Skips the number 5 as if the condition is met, it skips and continues on with the loop

# pass allows a part of the loop to be executed different based on an external condition and allow the rest of the loop to continue on
for number in range(10):
    if number == 5:
        pass    # pass here

    print(f'Number is  {number}')

print('Left the loop') # continues on as intended as there is no conditions to be met and is ignored. Typically used a a placeholder until
# the logic has been decided/figured out 

# Infinite loop - Without the break would go on infinitely 

x = 0

while True:
    if x == 8:
        break # breaks and exits the loop based on the condition of x == 8
    print(x)
    x += 1 # Adds 1 to x on each iteration of the while loop

x = 0

while x < 14: # if x is less than 14 the while loop will loop
    if x > 4 and x < 11: # when the value of x is between these value it will pass the steps and carry on with the loop until it meets
        # the conditions of the other statements 
        pass
    else:
        print(x)
    x += 1
    
# Above is also examples of nested iterations nesting different code blocks inside of each other

x = 0 

while x <= 3:
    y = 200
    while y <= 203:
        print(x, y) # Prints out both variables together
        y += 1
        
    x += 1

# Will print out each iteration 4 times. Due to the second while loops condition of y being less than 203
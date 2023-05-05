# # Operators and Conditional Statements

print("====Logical Operators====")
# # This is how we check for multiple conditions in one line of code

# # AND Operator
# # Both conditions have to be True to return a boolean value of "True"
# # In JS this looks like this: "&&"
print(True and True) # True
print(True and False) # False

# # OR Operator 
# # One or both conditions can be True to return a boolean value of "True", to return a boolean value of "False" than both conditions have to be false
# # In JS this looks like this: "||"
print(True or True) # True
print(True or False) # True
print(False or False) # False

# # NOT Operator
# # REVERSES a condition: True becomes False and False becomes True
# # In JS this the Bang or "!"
example = False
print(example) # False
print(not example) # True

print("====Comparison Operators====")
# # Almost all comparison operators are the same (ex: >, <, !=, ==)
# # However, there is no "===" comparison operator. So in Python you cannot get more strict that "=="
x = 14
comparison = x < 5 or x == 14
print(comparison)

print("====Membership Operators====")
# # Membership operators are used to test if a sequence is present in an object
# # These operators are "in" and "not in" and when used, return a value of True or False
letters = "xyz"
is_it = "a" not in letters
print(is_it)

print("====If/Else Statements====")
# # This is where indents become important

# # Syntax in Python
# # if condition:
# #   do this
# # else: 
# #   do this

# # An indent is classified as 4 spaces, if we want to put something inside of something else in Python we use indents
# # if condition:
# #    do this
# # else: 
# #                  this will not work

# # Errant indents will throw errors

# # We will set up a small little program for the following examples
print("Welcome to the rollercoaster!") # Welcomes the user to the program
height = int(input("What is your height in cm: ")) # Asks the user for their height in cm, and stores that to a variable (height)
# # Reminder that the int() function converts a different data type (i.e. String here) into an integer

print("====Example 1====")

# # JS version: 
# # if (height >= 120){
# #     alert("You can ride the rollercoaster")
# # } else {
# #     alert("Sorry you have to grow taller")
# # }

# # Python Version: 
if height >= 120:
    print("You can ride the rollercoaster")
else: 
    print("Sorry you have to grow taller")

print("====Example 2====")
# # Nesting Statements
# # We can nest if/else statements inside one another

# #JS version
# # if (height >= 120){
#     # alert("You can ride the rollercoaster!")
#     # age = prompt("Please enter your age: ")
#     # if (age < 12){
#         # alert("please pay $5")
#     # } else{
#         # alert("please pay $12")
#     # }
# # } else {
#     # alert("Sorry you have to grow taller")
# # }

# # Python Version
if height >= 120:
    print("you can ride roller coaster")
    age = int(input('Please enter your age: '))
    if age < 12:
        print ('pay 5 dollars')
    else:
        print("please pay 12 dollars")
else:
    print('Sorry you have to grow taller')
# # Checks height to see if you can ride. If height is greater than or equal two 120 cm, then asks for age. Compares age to next if/else statement and lets you know price to pay. 

print("====If/Else/Elif====")
# # Think of "elif" as standing for "else if"
# # Can use as many elif statements as you like within the if statements, same as in JavaScript

# # Syntax
# # if condition: 
# #     do this
# # elif condition:
# #     do this thing
# # else:
# #     do this last thing

# # Example

# # JS version
# # if (height >= 120){
#     # alert("You can ride the rollercoaster!")
#     # prompt("Please enter your age: ")
#     # if (age < 12){
#         # alert("please pay $5")
#     # } else if (age <= 18){
#         # alert("Please pay $7")
#     # } else{
#         # alert("please pay $12")
#     # }
# # } else {
#     # alert("Sorry you have to grow taller")
# # }

# # Python Version
if height >= 120:
    print('you can ride the roller coaster')
    age = int(input('please enter your name: '))
    if age < 12:
        print("please pay 5 dollars")
    elif age <= 18:
        print("please pay 7 dollars")
    else:
        print('pay 12 dollars yo')
else:
    print("u short yo")

print("====Output Below this Line will be the Full Program====")

bill = 0 # Value is to change based on user input within the program

if height >= 120:
    print('you can ride the roller coaster')
    age = int(input('please enter your name: '))
    if age < 12:
        print("please pay 5 dollars")
        bill = 5
    elif age <= 18:
        print("please pay 7 dollars")
        bill = 7
    elif age >= 45 and age >= 55: # midlife crisis level
        print('free ride on roller coaster')
        bill = 0
    else:
        print('pay 12 dollars yo')
        bill = 12
    wants_photo = input('Do you want a photo taken type "y" or "n" ').lower().strip()
    if wants_photo == 'y':
        bill += 3
    print(f"your bill is ${bill}")
else:
    print("u short yo")


print("====Bonus Fact: Python Ternary====")

# There is a Python equivalent to the Ternary also known as a "Conditional Expression"

# Syntax for Python
# if_condition_true if expression/condition else if_condition_false

a, b = 5, 20 # a different way to declare variables
print(f"{a} is less than {b}") if a < b else print(f"{a} is greater than {b}")



# # In JavaScript 
# let a = 10;
# let b = 10;
# let min = (a < b) ? console.log(a, "is greater") : console.log(b, "is greater");
# Functions

def bridge(text):
    print(f"\n===={text}====\n")
    
bridge("Functions basics")

# Syntax example
# To create a function...
def my_chicken():
    print('Hello Chicken')
    
# To call the function it is the same as JS
my_chicken()

bridge("Parameters")
# Functions with parameters are the same as they are in JS

bridge('Example 1')
my_name = input("whats your name: \n")
def new_function(name):
    print(f"Hello world my name is {name}")

new_function(my_name)

bridge("Example 2")
def the_shining(johnny):
    print(''.join(johnny))#note

no_work = ['A','L','L',' ','P','L','A','Y']

the_shining(no_work)

bridge("Example 3")

my_location = input('what is your location: \n')
def greet_with(name, location):
    print(f'Hello {name}')
    print(f'What is the weather like in {location}')
greet_with(my_name, my_location)

bridge('function scope')

def outer_func():
    def inner_func():
        print('sup world how we doin')
    inner_func()
outer_func()

bridge("return keyword")
#the return key word ahas the same functionality as it does in js

def return_keyword():
    simple = 1+1
    return simple

def return_keyword2():
    simple = 1+1
    return simple

not_simple = return_keyword() + return_keyword2()
print(not_simple)

# PYTHON DOESNT USE ARROW FUNCTIONS
# if you see an arrow in python it will be a return value annotations
#https://medium.com/@thomas_k_r/whats-this-weird-arrow-notation-in-python-53d9e293113#:~:text=Python%20doesn't%20use%20arrow,has%20been%20here%20since%203.0!

# higher order funcctions can be treated as an object or similar to js

def shout(text):
    return text.upper()
print(shout('hello'))

bridge("spread")

bridge("Spread Example 1")

def multiply(a,b):
    return a * b
numbers = [3,5]
multiplied = multiply(*numbers)
print(multiplied)

# Because there are two numbers in this list, we can pass them into the multiply function as arguments using spread. If there were more than two this would not work. 

print("====Spread Example 2====")
numbers = [1, 2, 3]
new_numbers = [0, *numbers, 4] #Spreads the list out with the other list
print(new_numbers)
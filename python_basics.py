# This is a Python Comment
# It is common practice to do multi-line comments one line at a time. There are no slippers here

# Python Basics 
# Python is a general purpose programming language used in scientific and specialized applications, first released in 1991. 
# Its design philosophy emphasizes code readability with the use of significant indentation.

# Fun Fact: 
# When Guido van Rossum, who created Python, began implementing the language, he was also reading the published scripts from "Monty Python's Flying Circus," so he decided to call the language Python. 

# Snake Case
# For Python we will use the naming convention called Snake Case, which is more common than Camel Case in Python. 
# It is notated by using the underscore "_" instead of a space between words
# Fun Fact: There was no name for this naming convention until 2004 even though it dates back to til the 1960's. Until then, even in the Python Style Guide, it was referred to as "lower_case_with_underscores"

# Print (Displays in the Console/Terminal)
print("====Python Basics====")
print("hello world")
print(42)

print("====Variables====")
# You do not have to declare a variable with a keyword (let, const, var)
# All you have to do is type in the variable name and what it is equal to
the_answer = 42
name = "gage"

# Display the variable in the console using print
print(the_answer)
print(name)

print("====Primitives====")
# Primitive Values are the same as in JavaScript with the exception to syntax of: 
# Primitive Values in JS: Number, Symbol, String, Boolean, Undefined, Null

# 1. Undefined/Null are now referred to as None
variable = None
print(variable)

# 2. Booleans are the same (i.e. true and false) However, in Python syntax they are capitalized
has_cookie = True
does_not_have_cookie = False
print(has_cookie)

# 3. Numbers are now referred as Integers

# We differentiate between Integers and Floats. Floats are Integers with decimals, allowing for more precision in data manipulation and more specific language. 
print("This is integer:", 123)
print("This is a float:", 3.123456)
# Note you can print two variables in the same print statement by separating them with a comma

# If you are ever unsure as to what data type you have, or are working with, we can use the type() function to return what type of Primitive a value is
unknown_data_type = 3.123456
print("This will be a float:", type(unknown_data_type))
print(type(has_cookie))

# We can also convert Primitives into other Primitive types using the following functions
# str() ---> converts to string
# int() ---> converts to integer
# float() ---> converts to float 
print(int(3.823456)) 
print(float(3))
print("I am going to type the number 3:" + " " + str(3) + "that was a 3")

print("====Operators====")
# All operators (=, -, /, *, **, %) are essentially the same, and so are order of operations
print(int((2+8/2)**7))

print("====Strings====")
# Strings operate the same except you cannot use backticks for strings, only "" or '' 
# print(`Hello there`)

# Concatenation uses the same principles with "+" sign
print("Hello" + " " + "my name is " + name)

print("====F Strings====")
# This is comparable to Template Literals
# Syntax example
my_name_is = f"Hello World my name is {name}"
print(my_name_is)
# We us "f" to notate that this string with have variables, and {} to notate where the variables are

print("====String Methods====")
# See this link for a full list of Python String methods: https://www.w3schools.com/python/python_ref_string.asp

# Some examples compared to what we learned in JavaScript

# trim() now becomes strip()
# Removes excess spaces
variable_trim_1 = "        Goodbye"
variable_trim_2 = "           See you later             "
print(variable_trim_1, variable_trim_2)
print(variable_trim_1.strip(), variable_trim_2.strip())

# toUpperCase() and toLowerCase() now become upper() and lower() 
# Changes string capitalization to all lowercase or all uppercase
text = "There are WORDS"
print(text.upper())
print(text.lower())

# indexOf() becomes index()
# Shows the location, or index, of the sought after variable, letter, etc.
letters = "abc"
print(letters.index("b")) # 1
# Index still starts at 0

# Some methods have the same name but different syntax, like slice()
# slice() would use this syntax
a = "this is the alphabet"
print(a[slice(8, 20)])
# You'd slice within the [] for index
# If a second number is NOT included, then the rest of the string will be included in the slice

# Certain methods that exist in JS may not exist in Python like repeat(), but there are other ways to accomplish the same goals
repeat = "abc "
repeat_three_times = repeat * 3
print(repeat_three_times)

# Note, not all methods exist in Python that may exist in JavaScript, like center()
# While the center method exist in JS for elements on a webpage, it does not exist for strings
centered = "This is centered in 100 characters"
print(centered.center(100))

print("====Inputs====")
# We store data inputted by the user using input()
# Syntax
# variable = input("This is a question for the user")

my_age = input("What is your age: ")
print(f"Jamie you are so old, I cannot believe you are {my_age}")
print(type(my_age))

# Inputs are always stored as STRINGs, so you can use any of the above methods on them. 
yelling = input("What do you want to yell: ")
print(yelling.upper().strip())

print("====Math Objects====")
# For math objects there is one Major Difference - import a module 
# Quick note: all imported modules should be placed at the top of the document. For this lesson we will put this here
import math

# Syntax difference: where in JS you capitalize ex: Math, in Python you use lowercase ex: math

# Constants are similar to JS Math constants, like pi
print(math.pi) # 3.14
print(math.nan) # nan

# Math.ceil() is the same, it rounds a float UP to nearest integer
number = 3.12345
print(math.ceil(number))

# Math.floor() still rounds a float DOWN to the nearest integer
print(math.floor(number))

# There is no Math.round, you have to specify with math.ceil or math.floor using the math module
# Note: you can use the round() function but it is separate from the math module
print(round(number))

# Full list of math module methods: https://www.w3schools.com/python/module_math.asp

# The random() method is another Major Difference between JavaScript and Python
# You have to import the random module 
import random

# To return a random number you would use either randrange() or randint(); compared to Math.random in JS
random_number = random.randrange(1, 10)
print(random_number)

# random_int = random.randint(start, stop+1)

# Full list of random module methods: https://www.w3schools.com/python/module_random.asp

# Be aware that the "++" and "--" incrementing/decrementing operators do not exist in Python
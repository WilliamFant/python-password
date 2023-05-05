# Loops 
# In Python there is no distinction between For and For Of loops as there is no different syntax

# Range Function
# The range() function creates a sequence of numbers and is typically used in for loops
# Syntax: range(start, stop, step)
# The stop number is NOT included in the range

print("====For Loops====")
# Syntax 
# for variable in range/list:
#   code the to be run here
# N0TE: INDENTS ARE IMPORTANT and the colon must be included

print("====Example 1====")
# Looping through a preset number of times 

# JS version: 
# for (i=1; i<=3; i++) {
#   console.log(i)
# }
# Output: 1 2 3

# Python Version: 
for number in range(1, 4):
    print(number)
# Loops UP to the last number in the range

print("====Example 2====")
# Looping through a preset number of times with steps

# JS Version: 
# for (i=0; i<=10; i+=2){
#   console.log(i)
# }
# Output: 0 2 4 6 8 10 

# Python Version
for number_by_two in range(0, 11, 2):
    print(number_by_two)
# runs up to but does NOT include 11, steps by 2

print("====Example 3====")
# Looping through a List (or Array)
# Note: We will go over Python Lists fully in an upcoming lesson
fruits = ["Apple", "Kiwi", "Grape Fruit"]
print(fruits)

# JS version: 
# for (fruitLoop of fruits) {
#   console.log(fruitLoop)
# }
# Output: Apple Kiwi Grape Fruit

# Python version 
for fruit_loop in fruits:
    print(fruit_loop)
# Note: there are other ways to loop through lists/arrays, but this is best practice because it is the "cleaner code"

print("====Nested Loop Example")
# Outer Loop (loop 2 times)
for i in range(1, 3):
    print("Outer Loop")
    # Nested (Inner) Loop (loop 4 times)
    for x in range(1, 5):
        print("Inner Loop")
    print(" ") # This makes it easier to read in the Terminal


print("====While Loops====")
# Syntax Example 
# while condition: 
#   code to run here
# N0TE: IDENTS ARE IMPORTANT and the colon must be included

print("====Example 1====")
# Run a while loop until a condition is met (or becomes False)

# JS version: 
# let number = 1; 
# while (number <= 3){
#   console.log(number);
#   number++;
# }
# Output: 1 2 3 

# Python version: 
number = 1
while number <= 3: 
    print(number)
    number += 1 # shorthand for number = number + 1
# Loop will run until the condition becomes false

print("====Example 2====")
# Run a loop wile a condition is NOT true until it becomes True
example = False 

# JS version:
# while (example != true){
#   shouldContinue = prompt("Continue? Type 'yes' or 'no'.");
#   if(shouldContinue == 'no'){
#       example = true;
#       }
# }

# Python Version: 
while not example:
    should_continue = input('Continue? Type "yes" or "no": ').strip()
    if should_continue == "no":
        example = True
    else:
        print("Okay I will keep going then")
# Loop will continue to run until user inputs 'no' (mind the spaces at the end)

# We do not use something comparable to the "===" in Python, this is because Python code typically uses Duck Typing: https://devopedia.org/duck-typing

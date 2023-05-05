# Python Lists
# Otherwise known as Arrays (sometimes you will hear them referred to as both)

print("====List Basics====")
# Similar to not having to declare variables with let, const, or var, we do not have to doe them here either
cryptids = [] # this is an empty list
print(cryptids)

# We can redeclare a list as many times as we would like
cryptids = ["Loveland Frogman", "Loch Ness Monster", "Bigfoot"]
print(cryptids)

cryptids = ["Fresno Nightcrawlers", "Moth Man"]
print(cryptids)

# We Can find the length of an array using the len() method
# JS Syntax would be cryptids.length() but in Python we would write:
cryptids_length = len(cryptids)
print(cryptids_length)

# Indexes are essentially the same in syntax and operation
# Reminder that indexes start at 0
print(cryptids[1])

# To change an item in a list we simply type
cryptids[0] = "Chupacabra"
print(cryptids)

# Note a difference between JS and Python is if we try to add a new list item to an index that does not yet exist it will not work. This WOULD work in JS and it would add empty list (array) up until that index to allow it. 
# We will instead get an IndexError 
# cryptids[9] = "Wendigo"
# print(cryptids)

print("====Main List Methods====")
teenage_turtles = ["Michaelangelo", "Donatello", "Raphael", "Leonardo"]
print(teenage_turtles)

# push() no becomes append()
# Adds an item to the end of a list
new_turtle = input("Type a new turtle: ")
teenage_turtles.append(new_turtle)
print(teenage_turtles)

# pop() still removes an item from the end of the list, same as in JS
teenage_turtles.pop()
print(teenage_turtles)

# shift() in JS can be accomplished with pop() in Python
# To do this we pass in arguments into the pop() method with this syntax: 
# list.pop(index)
# This also shifts the index of the list item, because it is not limited to the first item in the list like shift is in JS
print(teenage_turtles[1])
teenage_turtles.pop(0)
print(teenage_turtles[1])
print(teenage_turtles)

# unshift() in JS becomes insert() in Python
# insert() takes two arguments, an index and a value
teenage_turtles.insert(20, "Plato")
print(teenage_turtles)
# If we use insert() and type out an index of something that is Out of Index Range, it will just add it to the end of the list.

print("====Other List Methods====")

# index() method on a list, 
where_is_he = teenage_turtles.index("Donatello")
print(where_is_he)

# To add two lists together, there is no concat() method like there is JS
# Instead, we can do this: 
list_one = [1, 2, 3, 4]
list_two = [5, 6, 7, 8]
# We can use a For Loop to loop through all of list_two, and for each list item, we use append to add it to list_one
print("Below is our for loop to add two lists together")
for i in list_two:
    print(i)
    list_one.append(i)
print(list_one)

# To accomplish the same thing as the includes method in JS, which shows us if something is in an array (list), we would use the if keyword coupled with the "in" Membership Operator
if "Raphael" in teenage_turtles: # looks through the list for any item that matches
    print("He is in the list!")

# Note, it will only print it once, even if it is in the list twice because this is not a loop, it just looks for a instance using the "in" keyword
teenage_turtles.append("Raphael")
print(teenage_turtles)
if "Raphael" in teenage_turtles:
    print("He is in the list!")

new_list = ["item_one", "item_two"]
teenage_turtles.insert(10, new_list)
print(teenage_turtles[5])
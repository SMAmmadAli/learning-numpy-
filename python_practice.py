age = 24 # int
pi = 3.142 # double, float
name = "Ammad" # String
present = True # boolean

print(f"Student name is {name}, present in class {present}, age is {age} answer me the value of Pi is {pi}")

#  List ordered, changeable
my_list = [1,2,4,"Ammad"]
print(my_list)

# Tuple:  ordered, unchangeable
my_tuple = (1,2,3, "Ammad")
print(my_tuple)

# Set: unordered, unique values

my_set = {1,2,3,4}
print(my_set)

# Dictionary: key-value pairs
person = {"name": "Ammad", "age": 24}
print(person["name"])

# Conditional statements:
if age >= 25 and age < 50:
    print("You are young")
elif age >= 50:
    print("Your age is greater than or equal to 50")
else:
    print("You are under age")
    
fruits = ["mango", "apple", "banana"]

for fruit  in fruits:
    print(fruit )
    

# function
def greet(name):
    return f"Hello, {name}"

print(greet("Ammad"))

import math 

print(math.sqrt(9))


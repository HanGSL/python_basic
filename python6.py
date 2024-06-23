"""
#
# Part: Python Function
#
"""

def my_function ():
    print("hello World 1")
    print("hello World 2")

my_function()
my_function()

def my_name(fname):
    print("My name is", fname)

my_name("Han")

def my_name2(fname, Lname):
    print("My name is",fname, Lname)

my_name2("Han", "Patee")
my_name2(Lname = "Patee", fname = "Han")

def my_name3(Lname = "Patee"):
    print("My Last Name is ", Lname)

my_name3()
my_name3("Paul")

def my_fruits(fruit):
    for fruit in fruit:
        print(fruit)

fruit = ["Apple","Banana","Coconut"]
my_fruits(fruit)

def red_potion(hp):
    return hp + 50

print("HP:",red_potion(100))
print("HP:",red_potion(70))
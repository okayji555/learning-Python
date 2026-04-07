"""
From a function's perspective:

A parameter is the variable listed inside the parentheses in the function definition.

An argument is the actual value that is sent to the function when it is called.
"""

def func(fname): #here fname is parameter
    print(fname + "student") #"student" is argument

func("siva")
func("dev")
func("engineering")


def my_function(fruits):
  for fruit in fruits:
    print(fruit)

my_fruits = ["apple", "banana", "cherry"]
my_function(my_fruits)
"""
output:
apple
banana
cherry
"""


def my_function(greeting, *names):
  for name in names:
    print(greeting, name)

my_function("Hello", "Emil", "Tobias", "Linus")
"""
output:
Hello Emil
Hello Tobias
Hello Linus
"""

#using **kwargs
def my_function(**myvar):
  print("Type:", type(myvar))
  print("Name:", myvar["name"])
  print("Age:", myvar["age"])
  print("All data:", myvar)

my_function(name = "Tobias", age = 30, city = "Bergen")
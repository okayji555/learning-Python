"""
thistuple = ("apple",)
print(type(thistuple))

thistuple = ("apple")
print(type(thistuple))
"""

fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[1])
print(fruits[-1])
print(fruits[2:5])
if "apple" in fruits:
    print("Yes it is present")

#once added things to tuple then tuples items cannot be removed
#Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
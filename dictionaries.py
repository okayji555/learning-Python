thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)



for x in thisdict:
    print(x)
#and
for x in thisdict.keys():
    print(x)
#are same

#both give different values

for x in thisdict:
    print(thisdict[x])
#and
for x in thisdict.values():
    print(x)
#are same

#IF WANNA PRINT BOTH
for x,y in thisdict.items():
    print(x, y)




"""
Method	Description
clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary
"""

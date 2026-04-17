try:
    print(X)
except NameError:
    print("Variable x doesnt exist")
except:
    print("something else went wrong")
finally:
    print("The 'try except' is finished")

#The finally block, if specified, will be executed regardless if the try block raises an error or not.

try:
    print(X)
except:
    print("something else went wrong")
finally:
    print("The 'try except' is finished")



y = "hello"

if not type(y) is int:
  raise TypeError("Only integers are allowed")
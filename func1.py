
def my_function():
  print("Hello from a function")

my_function()


def fahrenheit_to_celsius(fahrenheit):
  return (fahrenheit - 32) * 5 / 9

print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50))


#function cannot be empty, so use pass statement

def my_func():
  pass



#finding max number
def my_function(*numbers):
  if len(numbers) == 0:
    return None
  max_num = numbers[0]
  for num in numbers:
    if num > max_num:
      max_num = num
  return max_num
print(my_function(3, 7, 2, 9, 1))




#LEGB RULE
"""
local
enclosing
global
built-in
"""
x = "global"

def outer():
  x = "enclosing"
  def inner():
    x = "local"
    print("Inner:", x)
  inner()
  print("Outer:", x)

outer()
print("Global:", x)
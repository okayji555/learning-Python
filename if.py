"""
a = 33
b = 33
if b>a:
    print("b is  greater than a")
elif b==a:
    print("b is equal to a")


age = 20
if age >= 18:
    print("You are eligible")
    print("you can vote")

"""

score = 86
if score >= 90:
  print("Grade: A")
elif score >= 80:
  print("Grade: B")
elif score >= 70:
  print("Grade: C")
elif score >= 60:
  print("Grade: D")


a = 2
b = 330
print("A") if a > b else print("B")


a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")




  score = 85
attendance = 90
submitted = True

if score >= 60:
  if attendance >= 80:
    if submitted:
      print("Pass with good standing")
    else:
      print("Pass but missing assignment")
  else:
    print("Pass but low attendance")
else:
  print("Fail")

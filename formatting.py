price = 45
txt = f"The final price is {price:.2f} dollars"
txt2 = f"The final price is {54:.2f} rupees"
print(txt)
print(txt2)


#adds comma
tet = 489000
ret = f"the price is {tet:,}"
print(ret)


print(f"the solution is {20 * 40}")

price1 = 59
tax = 0.25
txt = f"The price is {price1 + (price1 * tax)} dollars"
print(txt)


#also can use it in


def myconverter(x):
  return x * 0.3048

txt = f"The plane is flying at a {myconverter(30000)} meter altitude"
print(txt)



#another way
price = 49
txt = "The price is {} dollars"
print(txt.format(price))
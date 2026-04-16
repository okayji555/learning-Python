import re

txt = "There is pain in Spain"
x = re.search("^There.*Spain$", txt)

if x:
    print("Yes! we have a match")
else:
    print("No Match!")
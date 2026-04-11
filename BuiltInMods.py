import platform

print(platform.system())

print(dir(platform))


import datetime
x = datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))
# import naeme as friend
from platform import system
import datetime
# import json
import camelcase


# mycomputer=system()
# print(mycomputer)
# friend.greeting("Toledo")
# print(friend.person["name"])
# print(friend.person["age"])
# print(friend.person["Country"])

# print(dir(system))

x=datetime.datetime.now()
print(x.year)
print(x.strftime("%X"))
print(x.year)

c=camelcase.CamelCase()
text="hello world"
print(c.hump(text))


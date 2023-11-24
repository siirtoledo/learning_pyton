# x = "awesome"

def myfunc():
 global x
 x = "great"
 print("Python is " + x)

myfunc()
print("Python is " + x)
myList=["orange","pawpaw","mango"]
newList=[]

newList.append("apple")
print(newList)
newList=myList.copy()
newList.extend(myList)
print(newList)
newList.insert(1, "pineapple")
print(newList)
newList[2] = "pineapple"
print(newList)
newList.pop(4)
print(newList)
newList.remove("mango")
print(newList)
newList.sort()
print(newList)
print(" ".join(myList))
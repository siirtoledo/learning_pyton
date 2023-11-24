person={
"name" : "Toledo",
"Age" : 20,
"Occupation" :"Software Engineer"
}

print(person.get("name"))

a=person.keys()
b=person.values()
print(a)
print(b)
#to add
person ["Occupation"]="teacher"
print(person)
#if "Software Engineer" in person:
# print("Build a project for my company")
#else:
 #print("Thank you for coming")

if "teacher" in person.values():
 print("Come teach my students")
else:
 print("Thank you for coming")
 
 #to remove
person.pop("Age")
print(person)

person.popitem()
print(person)

del person["name"]
print(person)
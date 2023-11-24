# args
# def myFunction(*friends):
#     print(friends[2])

# myFunction("toledo", "chris","toledo","chris","lewis")



# kwargs
# def friends(**kids):
#     print("His last name is", kids["lname"])

# friends(fname="Caren", lname="Joe")

# def variable(amount,name="anonymous"):
#     print("The person who donated this", amount,"is",name)

# variable(50, "Toledo")

# def lists(*friends):
#     i=0
#     while i < len(friends):
#         print(friends[i])
#         i+=1

# lists("Chris","Alex","Rejoice")

# Return Values
# def returns(num1,num2):
#     return num1*num2
# print(returns(4,5))

# def passes():
#     pass

# Recursion
# def recall(num):
#     result=0
#     if num >0:
#         result= num + recall(num -1)
#         print(result)
#     else:
#         result=0

# recall(8)

def fuctorial(num):
    if num==0 or num==1:
        return 1
    else:
        return num*fuctorial(num-1)
    
print(fuctorial(7))
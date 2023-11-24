# def number(num):
#     return num +10

# print(number(3))

# x=lambda num:num+10
# print(x(4))

# age= lambda num: "My age is "+ str(num)
# # print("I am", age(20),"years old")
# print(age(6))

# multiply= lambda num1,num2: num1*num2
# print(multiply(3,4))

def func(num):
    return lambda a:a*num

number=func(6)(4)
# print(number(5))
print(number)




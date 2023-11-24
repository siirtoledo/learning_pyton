# for i in range(2,11, 2):
#     print(i)

# fruits=["orange","mango","pawpaw","pear"]

# for fruit in fruits:
#     if fruit=="orange":
#         continue
#     print(fruit)

# for i in range(0,100, 5):
#     print(i)

fruits=["orange","mango","pawpaw","pear"]
friends=["Kofi","Ama","Kojo","Kwame"]

# for fruit in fruits:
#     for friend in friends:
#         print("{} like {}".format(friend,fruit))


for i in range(len(fruits)):
    print(friends[i], " likes ", fruits[i])
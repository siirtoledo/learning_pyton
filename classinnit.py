# class Person:
#     classN =''
#     classA=''
#     def __init__(self,name,age):
#         self.classN=name
#         self.classA=age
#         print("welcome")
    
#     def __str__(self):
#         return "My name is {} and my age is {}".format(self.classN, self.classA)
    



# human=Person("Toledo",20)
# print(human.classN)
# print(human.classA)
# print(human)

class Animal:
    def __init__(self,name,sound):
        self.name=name
        self.sound=sound
    
    
    def makeSound(self):
        print(self.sound)
    
    def __str__(self):
        return "This {} make this sound {}".format(self.name,self.sound)
    

animal=Animal("Cow","moo")
# animals=Animal()
animal.makeSound()
print(animal)

class Phones:
    def __init__(self,name,model,sound):
        self.name=name
        self.model=model
        self.sound=sound
        

    def makeSound(self):
        print(self.sound)

    def __str__(self):
        return f"The name of this phone is {self.name} and model is {self.model}"
    
phone=Phones("Nokia","Nokia G12","Ring Ring")
phone.makeSound()
print(phone)
phone.makeSound()
phone.name="Iphone"
print(phone.name)
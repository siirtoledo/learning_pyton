class Animals:
    def __init__(self,eyes,legs,teeth):
        self.eyes=eyes
        self.legs=legs
        self.teeth=teeth
    
    def makeSound(self):
        print("the sound of the animal")

class Cats(Animals):
    def __init__(self,eyes,legs,teeth,name,sound):
        Animals.__init__(self,eyes,legs,teeth)
        self.name=name
        self.sound=sound
    
    def makeSound(self):
        print(self.sound)

class Goats(Animals):
    def __init__(self,eyes,legs,teeth,name,sound,run):
        Animals.__init__(self,eyes,legs,teeth)
        self.name=name
        self.sound=sound
        self.run=run
        

    def makeSound(self):
        print(self.sound)

class Dogs(Animals):
     def __init__(self,eyes,legs,teeth,name,sound,run):
        Animals.__init__(self,eyes,legs,teeth)
        self.name=name
        self.sound=sound
        self.run=run

     def makeSound(self):
        print(self.sound)


animals=Animals(2,2,42)
cats=Cats(2,2,42,"Keanu","meow")
goats=Goats(2,2,42,"NUNU","m333",True)
dogs=Dogs(2,2,42,"Keanu","woof",True)
cats.makeSound()
goats.makeSound()
dogs.makeSound()

print(dir(Cats))
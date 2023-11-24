class Person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    
    def getdetails(self):
        print("Person greeting")
    
    
class Student(Person):
    def __init__(self, fname, lname,level):
        Person.__init__(self,fname, lname)
        self.level=level
    
    def getname(self):
        print(self.fname)
        print(self.lname)
        print(self.level)
    
    def getdetails(self):
        print("I am a student")

student=Student("Francisco","Toledo",400)
student.getname()
student.getdetails()
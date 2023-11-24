class Employees:
    names=["Toledo","Manuella","Alex"]
    salaries=[5000,2000,7000]
    ids=[333,222,444]
    departments=["IT","HR","Logistics"]

    def getName(self):
        print("Names of employees are:")
        for name in range(len(self.names)):
            print(self.names[name])
    
    def getSalary(self):
        print("Employee salaries are:")
        for salary in range(len(self.salaries)):
            print(self.salaries[salary])

    def getId(self):
        print("Employee Ids are:")
        for id in range(len(self.ids)):
            print(self.ids[id])

    def getDepartment(self):
        print("Employee departments are:")
        for department in range(len(self.departments)):
            print(self.departments[department])

    def __str__(self):
       result = ""
       for i in range(len(self.names)):
            result += f"{self.names[i]} as an employee receives {self.salaries[i]} as salary, has the ID {self.ids[i]}, and is in the {self.departments[i]} department\n"
       return result
        


employees=Employees()
employees.getName()
employees.getSalary()
employees.getId()
employees.getDepartment()
print(employees)
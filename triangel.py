class Triangle:
    base= None
    height=None
    
    def area(self):
        return 1/2* self.base* self.height

  
    
triangle=Triangle()
triangle.base=5
triangle.height=4
print(triangle.area())


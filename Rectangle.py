class Rectangle():
    def __init__(self,length, width):
        self.length= length
        self.width = width
        
    
    def area(self):
        return self.length*self.width
    

newRec = Rectangle(10,5)
print (newRec.area())
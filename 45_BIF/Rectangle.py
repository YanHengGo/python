class Rectangle:
    def __init__(self,width=0,height=0):
        self.width=width
        self.height=height
    def __setattr__(self,name,value):
        if name=='square':
            self.width=value
            self.height=value
        else:
            super().__setattr__(name,value)
    def getArea(self):
        return self.width*self.height

r=Rectangle(4,5)
print(r.getArea())
r.square=10
print(r.getArea())
print(r.__dict__)


        

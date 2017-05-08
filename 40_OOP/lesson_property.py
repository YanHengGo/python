class C:
    def __init__(self,value=100):
        self.size=value
    def getSize(self):
        return self.size
    def setSize(self,value):
        self.size=value
    def delSize(self):
        del self.size
    x=property(getSize,setSize,delSize)

c=C()
print(c.getSize())
print(c.x)

c.x=18
print(c.x)
print(c.size)

del c.x
#print(c.x)

c.x=20
print(c.x)

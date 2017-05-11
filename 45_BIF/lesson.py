class C:
    def __init__(self,size=10):
        self.size=size
    def getSize(self):
        return self.size
    def setSize(self,size):
        self.size=size
    def delSize(self):
        del self.size
    x=property(getSize,setSize,delSize)

c=C()
print(c.x)

print('x=',getattr(c,'x','木有！'))
print('y=',getattr(c,'y','木有！'))


print('attr属性')
class D:
    def __getattribute__(self,name):
        print('getattribute')
        return super().__getattribute__(name)
    def __getattr__(self,name):
        print('getattr')
    def __setattr__(self,name,value):
        print('setattr')
        super().__setattr__(name,value)
    def __delattr__(self,name):
        print('delattr')
        super().__delattr__(name)


d=D()
print(d.x)
print('----')
d.x=10
print('----')
print(d.x)
print('----')
del d.x



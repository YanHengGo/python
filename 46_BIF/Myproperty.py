class Myproperty:
    def __init__(self,fget=None,fset=None,fdel=None):
        print('init----')
        self.fget=fget
        self.fset=fset
        self.fdel=fdel

    def __get__(self,instance,owner):
        print("gettting",self)
        print("gettting",instance)
        print("gettting",owner)
        return self.fget(instance)
    def __set__(self,instance,value):
        print("settting",self)
        print("settting",instance)
        print("settting",value)
        self.fset(instance,value)
    def __delete__(self,instance):
        print('delete',self)
        print('delete',instance)
        self.fdel(instance)

class C:
    def __init__(self):
        self._x=None
    def getX(self):
        return self._x
    def setX(self,value):
        self._x=value
    def delX(self):
        del self._x

    x=Myproperty(getX,setX,delX)

c=C()
c.x='x-man'
print(c.x)
print(c._x)
del c.x

        

#三角形函数
class Rectangle:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def getPeri(self):
        return (self.x+self.y)*2
    def getArea(self):
        return self.x*self.y

rect=Rectangle(3,4)
print(rect.getPeri())
print(rect.getArea())
#一个不可以实例化的函数
class A:
    def __init__(self):
        return "A for a-cup"
#TypeError __init__() should return none not str
#a=A()

#一个实用的变大写类
class Capstr(str):
    def __new__(cls,string):
        string=string.upper()
        return str.__new__(cls,string)
a=Capstr("I love FishC.com")

print(a)
        
#
class C:
    def __init__(self):
        print("FishC call __init__")
    def __del__(self):
        print("FishC call __del__")
print("---c1=C()---")
c1=C()
print("-------")
c2=c1
c3=c2


del c1
del c2

print("---del c3---")
del c3
print("-------")


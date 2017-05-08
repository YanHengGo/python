#判断是否子类issubclass
class A:
    pass
class B(A):
    pass

print(issubclass(B,A))
print(issubclass(A,object))

print(issubclass(A,A))
print(issubclass(B,B))

print('-----------------')
#判断是否实例化isinstance
b1=B()
print(isinstance(b1,B))
print(isinstance(b1,A))
print(isinstance(b1,(A,B)))

print('-----------------')
#判断是否有属性hasattr,getattr,setattr,delattr
class C:
    def __init__(self,x=0):
        self.x=x
c=C()
print(hasattr(c,'x'))

#getattr
print(getattr(c,'x'))
print(getattr(c,'y','not found'))
#setattr
setattr(c,'y','FishC')
print(getattr(c,'y','not found'))
#delattr
delattr(c,'y')
print(getattr(c,'y','not found'))
    

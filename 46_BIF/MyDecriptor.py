class MyDecriptor:
    def __get__(self,instance,owner):
        print("gettting",self)
        print("gettting",instance)
        print("gettting",owner)

    def __set__(self,instance,value):
        print("settting",self)
        print("settting",instance)
        print("settting",value)

    def __delete__(self,instance):
        print('delete',self)
        print('delete',instance)
        
class Test:
    x=MyDecriptor()

test=Test()
print('call test.x-----')
test.x
print('call test.x=xman-----')
test.x='X-man'
print('call del x-----')
del test.x



        

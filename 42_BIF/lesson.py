#BIF: build in function or method
print(type(len))
print(type(dir))
#class
print(type(int))
print(type(list))
class C:
    pass
print(type(C))
#int类
a=int("123")
b=int("456")
print(a+b)

#封装int 重写加法定义
class New_int(int):
    def __add__(self,other):
        return int.__sub__(self,other)
    def __sub__(self,other):
        return int.__add__(self,other)

a=New_int(3)
b=New_int(5)
print("a+b=",a+b)
print("a-b=",a-b)

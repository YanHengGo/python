#加载类
from Turtle import *

tu=Turtle()
tu.eat()

#封装 例子:list
list1=[2,1,3,7,5]
list1.sort()
print(list1)
list1.append(9)
print(list1)

#继承
class Mylist(list):
    pass
list2=Mylist()
list2.append(5)
list2.append(3)
list2.append(8)
list2.sort()
print(list2)

#多态
class A:
    def fun(self):
        print("a")
class B:
    def fun(self):
        print("b")

a=A()
b=B()
a.fun()
b.fun()

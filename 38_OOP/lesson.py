class Parent:
    def hello(self):
        print('父类')
class Child1(Parent):
    pass
class Child2(Parent):
    def hello(self):
        print('子类2')

p=Parent()
c1=Child1()
c2=Child2()
p.hello()
c1.hello()
c2.hello()

#多继承
class Base1:
    def func1(self):
        print('base1 func1')
class Base2:
    def func2(self):
        print('base2 func2')

class Child(Base1,Base2):
    pass

c=Child()
c.func1()
c.func2()

#类方法被覆盖(TypeError)
class C:
    def x(self):
        print('x func')

c=C()
c.x()
c.x=1
print(c.x)
#x()被覆盖发生TypeError
#c.x()


#共有类方法(public static)
class BB:
    def printBB():
        print('abcdefg')

BB.printBB()
bb=BB()
#发生TypeError
#bb.printBB()



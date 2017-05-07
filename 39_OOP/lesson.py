#类的共有方法
#类的私有变量
class CC:
    def setXY(self,x,y):
        self.x=x
        self.y=y
    def printXY(self):
        print(self.x,self.y)

dd=CC()
print(dd.__dict__)
print(CC.__dict__)

print('----------')
dd.setXY(4,5)
print(dd.__dict__)
print(CC.__dict__)

print('删除CC后printXY方法同样被调用----------')
del CC
dd.printXY()
print(dd.__dict__)



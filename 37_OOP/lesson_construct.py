class Ball:
    def __init__(self,name='球球'):
        self.name=name
    def kick(self):
        print("我叫%s,该死的，谁踢我" % self.name)

a=Ball('球A')
b=Ball('球B')
c=Ball('土豆')
d=Ball()
a.kick()
b.kick()
c.kick()
d.kick()


class Person:
    publicname='小甲鱼'
    __privatename='小鱿鱼'
    def getName(self):
        return self.__privatename

p=Person()
print(p.publicname)
#AttributeError
#print(p.__privatename)
print(p.getName())
print(p._Person__privatename)

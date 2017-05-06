class Ball:
    def setName(self,name):
        self.name=name
    def kick(self):
        print("我叫%s,该死的，谁踢我" % self.name)

a=Ball()
a.setName('球A')
b=Ball()
b.setName('球B')
c=Ball()
c.setName('土豆')
a.kick()
b.kick()
c.kick()


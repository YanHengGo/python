class Turtle:
    def __init__(self,x):
        self.num=x
class Fish:
    def __init__(self,x):
        self.num=x
class Pool:
    def __init__(self,x,y):
        self.turtle=Turtle(x)
        self.fish=Fish(y)
    def print_num(self):
        print('turtle=%d,fish=%d' % (self.turtle.num,self.fish.num))

p=Pool(3,5)
p.print_num()



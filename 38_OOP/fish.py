import random as r

class Fish:
    def __init__(self):
        self.x=r.randint(0,10)
        self.y=r.randint(0,10)
    def move(self):
        self.x-=1
        print("我的位置是:",self.x,self.y)
class Goldfish(Fish):
    name='gold fish'
class Carp(Fish):
    pass
class Salmon(Fish):
    pass
class Shark(Fish):
    def __init__(self):
        super().__init__()
#        Fish.__init__(self)
        self.isHungry=True
    def eat(self):
        if self.isHungry:
            print('吃货，想吃就吃')
            self.isHungry=False
        else:
            print("吃饱了，想溜达溜达")


    
sh=Shark()
sh.move()

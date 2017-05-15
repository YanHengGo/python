for i in "FishC":
    print(i)

links={'鱼C工作室':'http://www.fishc.com',
       '鱼C论坛':'http://bbs.fishc.com'}

for each in links:
    print("%s -> %s" % (each , links[each]))

#iter() next()

string='FishC'


it=iter(string)
print(next(it))

for each in string:
    print(each)


class Fibs:
    def __init__(self,n=10):
        self.a=0
        self.b=1
        self.n=n
    def __iter__(self):
        return self
    def __next__(self):
        self.a , self.b = self.b , self.a+self.b
        if self.a > self.n:
            raise StopIteration
        
        return self.a

fibs=Fibs(100)
for each in fibs:
    if each <20:
        print(each)
    else:
        break
    

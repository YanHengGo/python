def ds(x):
    return 2*x+1
print(ds(5))

g=lambda x : x*2+1
print(g(5))

def add(x,y):
    return x+y
print(add(3,4))

ga=lambda x,y : x+y
print(ga(3,4))

print(list(filter(None,[1,0,False,True])))

def odd(x):
    return x%2
temp =range(10)
show =filter(odd,temp)
print(list(show))

print(list(filter(lambda x:x%2,range(10))))

#help(filter)

print(list(map(lambda x:x*2,range(10))))


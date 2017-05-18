def myGen():
    print('生成器!')
    yield 1
    yield 2
    yield 3

m=myGen()

next(m)

def fib():
    a=0
    b=1
    while True:
        a,b=b,a+b
        yield b

for each in fib():
    if each > 100:
        break
    print(each,end=' ')
print('')

#列表推导式
a=[i for i in range(100) if not(i%2) and i%3]
print(a)

#字典推导式
b={i:i%2==0 for i in range(10)}
print(b)

#集合推导式
c={i for i in [7,2,3,6,4,3,2,5,6,1,3]}
print(c)

#字符串推导式 木有

#生成器推导式
e=(i for i in range(10))

print(next(e))
print(next(e))

#生成器推导式 加法
print(sum(i for i in range(100) if i%2))


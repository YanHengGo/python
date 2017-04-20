def fun1():
    print('in the fun1')
    def fun2():
        print('in the fun2')

    fun2()

fun1()

def funx(x):
    def funy(y):
        return x*y
    return funy

print(funx(5))

fn=funx(8)

print(type(fn))

print(fn(5))

print(funx(8)(5))

def fun3():
    x=[5]
    def fun2():
        x[0]*=x[0]
        return x[0]
    return fun2()

print(fun3())

def fun4():
    x=5
    def fun2():
        nonlocal x
        x*=x
        return x
    return fun2()

print(fun3())


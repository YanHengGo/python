def foo():
    func_list=[]
    for i in range(3):
        def inner(x=i):
            return x*x
        func_list.append(inner)
    return func_list

f=foo()

for each in f:
    print(each)
    print(each())
    


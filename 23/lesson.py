def factorial(n):
    if n==1 :
        return 1
    if n==2 :
        return 1
    return factorial(n-1)+factorial(n-2)

num=factorial(20)
print(num)

def fab(n):
    n1=1
    n2=1
    n3=1

    while n>2:
        n3=n2+n1
        n1=n2
        n2=n3
        n-=1
    return n3

print(fab(20))
        

def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)

print(factorial(5))

def factorial1(n):
    result=n
    for i in range(1,n):
        result *= i

    return result

num=int(input("please enter a num:"))
result=factorial(num)
print("%d 的阶乘是 %d" % (num,result))

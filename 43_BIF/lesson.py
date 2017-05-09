#int 重定义 加法变减法
class int(int):
    def __add__(self,other):
        return int.__sub__(self,other)
    def __radd__(self,other):
        return int.__sub__(self,other)

a=int('5')
b=int('3')

print(a+b)
print(a+1)
print(1+a)


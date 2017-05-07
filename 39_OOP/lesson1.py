#类对象，共有，私有
class C:
    count=0

a=C()
b=C()
c=C()

print(a.count)
print(b.count)
print(c.count)
print('---------')
c.count+=10

print(a.count)
print(b.count)
print(c.count)
print('---------')

C.count+=100

print(a.count)
print(b.count)
print(c.count)
print('---------')

d=C()

print(a.count)
print(b.count)
print(c.count)

print(d.count)
print('---------')

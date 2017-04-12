#0
old = [1, 2, 3, 4, 5]
new = old
old = [6]
print(new)
#1
list1 = [1, [1, 2, ['小甲鱼']], 3, 5, 8, 13, 18]
list1[1][2][0]='小鱿鱼'
print(list1)
#2
list2=[2,1,4,6,4,7]
list2.sort()
print(list2)
#3
list2.sort(reverse=True)
print(list2)
#4
list3=[4,5,6]
list4=list3.copy()
print(list4)
list4.clear()
print(list4)
#5
list5=[i*i for i in range(10)]
print(list5)
list6 = [(x, y) for x in range(10) for y in range(10) if x%2==0 if y%2!=0]
print(list6)
list7=[]
for x in range(10):
    for y in range(10):
        if x%2==0:
            if y%2!=0:
                list7.append((x,y))

print(list7)
#6 not yet


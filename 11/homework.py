#0
list1=[1,3,2,9,7,8]
print(list1[2:5])
#1 一样
#2
temp=list1.pop()
list1.insert(0,temp)
print(list1)
#3
list1=[1,3,2,9,7,8]
print(list1[-3:-1])
#4
print(list1[0:6:2])
#5
list=list1
print(list)
list2=list[:]
print(list2)
#6 del remove pop slice

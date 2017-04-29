import copy
#字典 fromkeys 只有一个参数
dict1={}
dict1.fromkeys((1,2,3))
print(dict1)
dict1.fromkeys((1,2,3),'Number')
print(dict1)
dict2=dict1.fromkeys(range(32),'赞')
print(dict1)
print(dict2)

#字典遍历 keys,values,items方法
'''
for eachkey in dict2.keys():
    print(eachkey,dict2[eachkey])
for eachvalue in dict2.values():
    print(eachvalue)
for eachitem in dict2.items():
    print(eachitem)
'''

#字典查找 报错对应 get方法
print(dict2[31])
#print(dict2[32])
print(dict2.get(32))
print(dict2.get(32,'木有！'))

#字典查找 in方法
print(31 in dict2)
print(32 in dict2)

#字典清空 clear方法
dict2.clear()
print(dict2)

#区别 赋值(id一样)，浅拷贝(子id一样)，深拷贝(全部是新地)
a={1:'one',2:'two',3:['three','san']}
b=a
c=copy.copy(a)
d=copy.deepcopy(a)
print('a',id(a))
print('b',id(b))
print('c',id(c))
print('d',id(d))
a[2]='er' #赋值被改变
print(a,b,c,d) 
a[4]='four' #赋值被改变
print(a,b,c,d) 
a[3].append('fishC') #赋值，浅拷贝被改变
print(a,b,c,d) 
#字典 pop,popitem,setdefault方法
a.pop(1)
print(a)
a.popitem()
print(a)
a.setdefault('小白')
print(a)
a.setdefault(5,'five')
print(a)
#字典 update方法
b={'小白':'狗'}
a.update(b)
print(a)




#创建 空字典
num={}
print(type(num))
#生成 集合 没有重复元素
num={1,2,3,4,5,5}
print(type(num))
print(num)
#添加成员变量
num.add(8)
print(num)
#没有顺序 下面报错
#num[2]
#生成 集合 用列表
set1=set([1,2,3,4,5,5,5])
print(set1)
#去掉列表里的重复元素 用for
num1=[1,2,3,4,5,5,3,1,0]
temp=[]
for item in num1:
    if item not in temp:
        temp.append(item)
print(temp)
#去掉列表里的重复元素 用集合
temp=list(set(num1))
print(temp)
#查看集合的成员
print(1 in num)
#创建不可变的集合 final
num3=frozenset([1,2,3,4,5])
#num3.add(8)





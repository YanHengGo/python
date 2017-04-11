member=['小甲鱼','aa','bb','cc','dd']

member.append(88)

member.insert(4,90)
member.insert(3,85)
member.insert(2,90)
member.insert(1,88)


print(member)

for i in member:
    print(i)
    


name=0
for j in member:
    if name==0 :
        name=j
    else:
        print(str(name)+' '+str(j))
        name=0



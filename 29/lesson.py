def savefile(name,list1):
    f1=open(name,'w')
    for eachitem in list1:
        f1.write(eachitem)
    f1.close()


f=open('aa.txt','r',encoding='UTF-8')
#print(f.read())
#f.seek(0,0)

boy=[]
girl=[]
count=1

for eachline in f:
    if eachline[:6] != '======':
        (role,line_context)=eachline.split(':',1)
        if role=='小甲鱼':
            boy.append(line_context)
        if role =='小客服':
            girl.append(line_context)
    else :
        print("-----------")
        savefile('boy_'+str(count)+'.txt',boy)
        savefile('girl_'+str(count)+'.txt',girl)
        boy=[]
        girl=[]
        count+=1

f.close()


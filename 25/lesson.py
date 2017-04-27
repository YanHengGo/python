#列表
brand=['李宁','耐克','阿迪达斯','鱼c工作室']
slogan=['一切皆有可能','Just do it','Impossible is nothing','让编程改变世界']
print('鱼C工作室的口号是:',slogan[brand.index('鱼c工作室')])
#字典 生成
dict1={'李宁':'一切皆有可能','耐克':'Just do it','阿迪达斯':'Impossible is nothing','鱼c工作室':'让编程改变世界'}
print('鱼C工作室的口号是:',dict1['鱼c工作室'])
#字典 生成
dict2={1:'one',2:'two',3:'three'}
print(dict2)
print(dict2[2])
#空字典 生成
dict3={}
print(dict3)
#用元祖 生成字典 注意参数只有一个
dict4=dict((('F',70),('i',105),('s',115),('h',104),('C',67)))
print(dict4)
#字典的修改
dict2[2]='er'
print(dict2)
#字典的追加
dict2[4]='four'
print(dict2)

#print(help(open))
#打开文件夹
f=open('E:\\workspace\\06_python\\01_20170411\\python\\28\\aaaa.txt')
print(f.read())
#移动指针 0是开始位置 1是当前位置 2是末尾
f.seek(0,0)
#文件内容边字符串
list1=list(f)
print(list1)
#查看当前指针位置
print(f.tell())
f.seek(0,0)
print(f.tell())
#读取一行
print(f.readline())
print(f.tell())
#迭代读取内容
for eachline in list1:
    print(eachline)
#迭代读取内容 用指针
f.seek(0,0)
for eachline in f:
    print(eachline)
f.close()
#文件写入
f1=open('E:\\workspace\\06_python\\01_20170411\\python\\28\\b.txt','b')
f1.write('fjaljfls')
#文件的行写入
f1.close()

#文件打开形式
#r 文件存在:只读     文件不存在:异常报错
#w 文件存在:覆盖写入 文件不存在:生成
#x 文件存在:异常报错 文件不存在:生成
#w 文件存在:末尾写入 文件不存在:生成




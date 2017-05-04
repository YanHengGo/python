#AssertionError
#assertion:主张，明确肯定
my_list=['aa']
assert len(my_list)>0
my_list.pop()
#assert len(my_list)>0

#AttributeError
#attribute:属性
#my_list.fishc()

#IndexError
my_list=[1,2,3]
my_list[2]
#my_list[3]

#keyError
my_dic={1:'one',2:'two',3:'three'}
print(my_dic[1])
#print(my_dic[4])
#可以用get方法,没有的话啥也不返回
my_dic.get(4)

#NameError 
#print(abc)

#OSError(FileNotFoundError)
#f=open('abcd')

#SyntaxError
#print 'fishc'

#TypeError
#aaa=1+'1'

#ZeroDivisionError
#aaa=1/0



#1
print("{{1}}".format("print","no print"))
#2
print("{a} love {b}.{c}".format(a='I',b='FishC',c='com'))
#3
print("{0} love {1}.{2}".format('I','FishC','com'))
#4
print("{0}{1:.2f}".format('Pi = ',3.1415))

#
istr=input('please enter a num :')

while 1:
    if istr.isdecimal():
        iput=int(istr)
        print("十进制 -> 十六进制 : %d -> %#x" % (iput,iput))
        print("十进制 -> 八进制 : %d -> %#o" % (iput,iput))
        print("十进制 -> 二进制 : %d -> " % iput,bin(iput))
    else:
        if istr == 'Q':
            break
    istr=input('please enter a num Q to quit :')

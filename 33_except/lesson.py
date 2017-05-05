#可以捕获所有异常，但不推荐
try:
    int('abc')
    sum=1+'1'
    f=open('abc.txt')
    print(f.read())
    f.close()
except :
    print('出错了T_T')

#分别捕获异常
try:
    sum=1+'1'
    f=open('abc.txt')
    print(f.read())
    f.close()
except OSError as reason:
    print('文件出错了T_T',reason)
except TypeError as reason:
    print('类型出错了T_T',reason)

#同时捕获异常
try:
    sum=1+'1'
    f=open('abc.txt')
    print(f.read())
    f.close()
except (OSError,TypeError) as reason:
    print('出错了T_T',reason)

#关于finally
try:
    f=open('abc.txt','w')
    f.write('write sth')
    sum=1+'1'
except OSError as reason:
    print('文件出错了T_T',reason)
except TypeError as reason:
    print('类型出错了T_T',reason)
finally:
    f.close()

#抛出异常 关于raise 可以有参数
raise ZeroDivisionError('除数为0')

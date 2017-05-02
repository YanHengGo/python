#使用random模块
import random
secret=random.randint(1,10)
print(secret)
#使用os模块
import os
mypath=os.getcwd()
print(mypath)
print(os.listdir(mypath))
#os.mkdir(mypath+'\\A')
#os.makedirs(mypath+'\\C\\B')
#os.rmdir(mypath+'\\A')
#os.removedirs(mypath+'\\C\\B')
#os.system('cmd')
#os.system('calc')
print(os.listdir(os.curdir))
print(os.sep)
print(os.linesep)
print(os.name)
#使用os.path模块
import os.path
testfile='E:\\workspace\\06_python\\01_20170411\\python\\30\\lesson.py'
print(os.path.basename(testfile))
print(os.path.dirname(testfile))
print(os.path.join('E:\\','A','B','C'))
print(os.path.split(testfile))
print(os.path.splitext(testfile))
print(os.path.getatime(testfile))
print(os.path.getctime(testfile))
print(os.path.getmtime(testfile))
import time
print(time.gmtime(os.path.getatime(testfile)))
print(time.gmtime(os.path.getctime(testfile)))
print(time.gmtime(os.path.getmtime(testfile)))
print(os.path.ismount('E:\\'))
print(os.path.ismount('E:\\A'))


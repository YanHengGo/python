import sys
import Mypackage.TemperatureConversion as tc

for each in sys.path:
    print(each)

#添加搜索路径
#sys.path.append("C:\\abc")


#导入包
print("32摄氏度 = %.2f华氏度" % tc.c2f(32))
print("100华氏度 = %.2f摄氏度" % tc.f2c(100))

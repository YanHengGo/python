def searchnum(num):
    unit=num%10
    decade=(int)((num-unit)/10%10)
    hundreds=(int)(num/100)
#    print(unit,decade,hundreds)
    if unit**3 + decade**3 + hundreds**3 == num :
        print(num)


for num in range(100,999):
    searchnum(num)

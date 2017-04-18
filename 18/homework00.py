def timebasefn(*param,base=3):
    m_len=len(param)
    sum=0
    for i in param:
        sum+=i
    print(base*sum)

timebasefn(1,2,3)

timebasefn(1,2,3,base=5)

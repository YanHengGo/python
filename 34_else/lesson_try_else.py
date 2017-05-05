def changeToNum(str):
    try:
        num=int(str)
    except ValueError as reason:
        print(str,'error not number ',reason)
    else:
        print(str,'nothing wrong')

str=input('please enter a number:')
changeToNum(str)

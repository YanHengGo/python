try:
    with open('data.txt','w') as f:
        for each_line in f:
            print(each_line)
except OSError as reason:
    print('error',reason)
    
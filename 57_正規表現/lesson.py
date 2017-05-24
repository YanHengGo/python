import re
tar='I love FishC.com!'
ip1='192.168.168.168'
ip2='192.168.1.1'
ip3='1.1.1.1'
ip4='1.1.1.0'
print('---find---')
print(tar.find('Fish'))

print('---search---')
a=re.search(r'Fish',tar)
print(a)
print(a.group())
print(a.start())
print(a.end())

print('---\.---')
print(re.search(r'.',tar))
print(re.search(r'\.',tar))
print(re.search(r'\d',tar+'123'))
print(re.search(r'\d\d\d',tar+'123'))

print('---[]---')
print(re.search(r'[aiueo]',tar))
print(re.search(r'[aiueoAIUEO]',tar))
print(re.search(r'[a-z]',tar))
print(re.search(r'[0-9]',ip1))
print(re.search(r'[2-9]',ip1))
print('---{}---')
print(re.search(r'ab{3}c',"abbbc"))
print(re.search(r'ab{3}c',"abbbbbc"))
print(re.search(r'ab{3,6}c',"abbbbbc"))

print('---ip---')
print(re.search(r'\d\d\d.\d\d\d.\d\d\d.\d\d\d',ip1))
print(re.search(r'\d\d\d.\d\d\d.\d\d\d.\d\d\d',ip2))

print(re.search(r'(([01]\d\d|2[0-4]\d|25[0-5])\.){3}([01]\d\d|2[0-4]\d|25[0-5])',ip1))
print(re.search(r'(([01]\d\d|2[0-4]\d|25[0-5])\.){3}([01]\d\d|2[0-4]\d|25[0-5])',ip2))

print(re.search(r'(([01]{0,1}\d{0,1}\d|2{0,1}[0-4]\d|25[0-5])\.){3}([01]{0,1}\d{0,1}\d|2{0,1}[0-4]\d|25[0-5])',ip2))
print(re.search(r'(([01]{0,1}\d{0,1}\d|2{0,1}[0-4]\d|25[0-5])\.){3}([01]{0,1}\d{0,1}\d|2{0,1}[0-4]\d|25[0-5])',ip3))
print(re.search(r'(([01]{0,1}\d{0,1}\d|2{0,1}[0-4]\d|25[0-5])\.){3}([01]{0,1}\d{0,1}\d|2{0,1}[0-4]\d|25[0-5])',ip4))

search_key=r'(([01]{0,1}\d{0,1}\d|2{0,1}[0-4]\d|25[0-5])\.){3}([01]{0,1}\d{0,1}\d|2{0,1}[0-4]\d|25[0-5])'
print(re.search(search_key,ip4))
print(re.search(search_key,'1.1.12.1'))



import urllib.request
ad='http://www.fishc.com'
myformat='utf-8'
response=urllib.request.urlopen(ad)
html=response.read().decode(myformat)
print(html)



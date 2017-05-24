import re
a1=re.search(r"Fish(C|D)","FishC")
print(a1)
print(type(a1))
print(a1.group())
print(a1.start())
print(a1.end())
a2=re.search(r"Fish(C|D)","FishD")
print(a2)
a3=re.search(r"Fish(C|D)","FishE")
print(a3)

print("--^ $--")
print(re.search(r"^FishC","I love FishC.com"))
print(re.search(r"^FishC","FishC.com"))
print(re.search(r"FishC$","FishC.com"))
print(re.search(r"FishC$","loveFishC"))

print("--\--")
print(re.search(r"(FishC)\1","loveFishC"))
print(re.search(r"(FishC)\1","loveFishCFishC"))
print("--\ 060--")
print(re.search(r"(FishC)\060","loveFishCFishC"))
print(re.search(r"(FishC)\060","loveFishC0FishCa"))
print(re.search(r"(FishC)\141","loveFishC0FishCa"))
print("--.--")
print(re.search(r".","loveFishC0FishCa"))
print(re.search(r"\.","loveFishC0FishCa"))
print(re.search(r"\.","I love FishC.com"))

print("--[]--")
print(re.search(r"[.]","I love FishC.com"))
print(re.search(r"[a-z]","I love FishC.com"))

print("--{}--")
print(re.search(r"FishC{3}","I love FishC.com"))
print(re.search(r"FishC{3}","I love FishCCCCC.com"))
print(re.search(r"(FishC){3}","I love FishCCCCC.com"))
print(re.search(r"(FishC){3}","I love FishCFishCFishC.com"))
print(re.search(r"(FishC){1,5}","I love FishCFishCFishC.com"))
print("--+ ?--")
s="<html><title>I love FishC.com</title></html>"
print(re.search(r"<.+>",s))
print(re.search(r"<.+?>",s))

      

print("--findall--")
print(re.findall(r"[a-z]","I love FishC.com"))
print(re.findall(r"[\n]","I love FishC.com\n"))
print(re.findall(r"[^a-z]","I love FishC.com\n"))







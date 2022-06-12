
string=input()
set1=set()
for i in range(len(string)):
    if string[i]=="{" or string[i]=="}" or string[i]==","or string[i]==" ":
        continue
    else:
        set1.add(string[i])
print(len(set1))


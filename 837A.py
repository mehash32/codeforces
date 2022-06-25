n= int(input())
string = input()
count=0
mx=0
for i in range(len(string)):
    if string[i].isupper()== True:
        count=count+1
        mx= max(count,mx)
        
    if string[i]==" ":
        count=0
print(mx)
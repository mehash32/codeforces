str= input()
str2= input()
rev_str=""
for i in str:
    rev_str=i+rev_str
if(str2==rev_str):
    print("YES")
else:
    print("NO")
n=int(input())
string=input()
string=string.lower()
lst=list(string)
lst.sort()
count=1
for i in range(n-1):
    if lst[i]!=lst[i+1]:
        count+=1  
print(count)     
if count==26:
    print("YES")
else:
    print("NO")

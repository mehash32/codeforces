n=int(input())
c=0
num=0
even=0
odd=0
lst=list(map(int,input().strip().split()))
for i in range(len(lst)):
    if lst[i]%2==0:
        even+=1
    else:
        odd+=1
if even>1:
    for i in range(len(lst)):
        if lst[i]%2!=0:
            print(i+1)
else:
    for i in range(len(lst)):
        if lst[i]%2==0:
            print(i+1)
        
    
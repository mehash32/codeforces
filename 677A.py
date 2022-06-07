a,b= map(int,input().strip().split())
lst=list(map(int,input().strip().split()))
count=0
for i in range(len(lst)):
    if lst[i]<=b:
        count=count+1
    else:
        count+=2
print(count)
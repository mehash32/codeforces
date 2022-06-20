n=int(input())
lst=list(map(int,input().strip().split()))
sum=0
count=0
for i in range(n):
    if lst[i]==-1:
        if sum>0:
            sum=sum-1
        else:
            count=count+1
    else:
        sum=sum+lst[i]
print(count)
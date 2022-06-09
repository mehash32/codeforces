n=int(input())
lst=list(map(int,input().strip().split()))
c=0
max_count=1
count=[]
if n>1:
    for i in range(n-1):
        if lst[i]<=lst[i+1]:
            c=c+1
        else:
            c=0
        count.append(c)
    max_count=max(count)+1
    print(max_count)
else:
    print(max_count)

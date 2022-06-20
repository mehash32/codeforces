n=int(input())
lst=list(map(int, input().split()))
count=0
mx=lst[0]
mi=lst[0]
for i in range(len(lst)):
    if lst[i]>mx:
        mx=lst[i]
        count=count+1
    if lst[i]<mi:
        mi=lst[i]
        count=count+1
print(count)

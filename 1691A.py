n=int(input())
for i in range(n):
    a=int(input())
    count1=0
    count2=0
    lst=list(map(int,input().strip().split()))
    for j in range(len(lst)):
        if lst[j]%2==0:
            count1=count1+1
        else:
            count2=count2+1   
    print(min(count1,count2))
            
n=int(input())
while n>0:
    n=n-1
    a,b=map(int,input().strip().split())
    lst1=list(map(int,input().strip().split()))
    lst2=list(map(int,input().strip().split()))
    lst1.sort()
    lst2.sort(reverse=True)
    if b==0:
        suum=sum(lst1)
    else:
        k=0
    for j in range(b):
        if lst1[k]<lst2[j]:
            lst1[k]=lst2[j]
            k=k+1
        suum=sum(lst1)
    
    print(suum)

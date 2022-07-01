n=int(input())
for i in range(n):
    a=int(input())
    lst=list(map(int,input().strip().split()))
    lst.sort()
    flag=0
    for j in range(len(lst)-1):
        if abs(lst[j]-lst[j+1])>1:
            flag=1
            
    if flag==0:
            print("YES")
    else:
            print("NO")
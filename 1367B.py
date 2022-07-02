n=int(input())
while n>0:
    n=n-1
    a=int(input())
    lst=list(map(int,input().strip().split()))
    lst1=[]
    lst2=[]
    for i in range(len(lst)):
        if i%2==0:
             if lst[i]%2!=0:
                lst1.append(i)
                
        if i%2!=0:
            if lst[i]%2==0:
                lst2.append(i)
        
    if len(lst1)!= len(lst2):
        print("-1")
    else:
        print(len(lst1))

n=int(input())
for i in range(n):
    a=int(input())
    lst=[]
    i=len(str(a))
    k=0
    while a!=0:        
        if a%pow(10,i)==0:
            break    
        rem=a%10
        a=int(a/10)
        if rem*pow(10,k)!=0:
            lst.append(rem*pow(10,k))
        i=i-1
        k=k+1
    print(len(lst))
    print(' '.join(map(str,lst)))

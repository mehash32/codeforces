a,b =map(int,input().strip().split())
count=0
temp=0
mi=min(a,b)
if a>mi:
    a=a-mi
    if a%2==0:
        count=int(a/2)
    else:
        temp=a%2
        a=a-temp
        count=int(a/2)
if b>mi:
    b=b-mi
    if b%2==0:
        count=int(b/2)
    else:
        temp=b%2
        b=b-temp
        count=int(b/2)
print(mi,count)
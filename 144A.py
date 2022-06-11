n=int(input())
count=0
flag=0
lst=list(map(int,input().strip().split()))
maximum= max(lst)
minimum= min(lst)
a=lst.index(maximum)
b=lst.index(minimum)
for index in range(len(lst)):
        if lst[index] == maximum:
            c=index
        if lst[index] == minimum:
            d=index
a=min(a,c)
b=max(b,d)
if a==0 and b==n-1:
    print(count)
else:
    if b>a:
        count=a+((n-1)-b)
    else:
        count=a+((n-1)-b)-1
    print(count)


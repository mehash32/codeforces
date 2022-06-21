
lst=list(map(int,input().strip().split()))
lst.sort()
c=lst[-1]-lst[0]
b=lst[-1]-lst[1]
a=lst[-1]-lst[2]
print(b,a,c)
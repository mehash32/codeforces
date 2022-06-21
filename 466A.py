n,m,a,b =map(int,input().strip().split())
if m*a<=b:
    print(n*a)
else:
    print(int(n/m)*b+min((n%m)*a,b))
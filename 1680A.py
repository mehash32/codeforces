n=int(input())
for i in range(n):
    l1,r1,l2,r2= map(int, input().strip().split())
    mx=max(l1,l2)
    mi=min(r1,r2)
    if mx<=mi:
        print(mx)
    else:
        print(l1+l2)

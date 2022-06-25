n=int(input())
for i in range(n):
    a,b,c,x,y=map(int,input().strip().split())
    mx=max(0,x-a)
    mx2=max(0,y-b)
    if mx+mx2<=c:
        print("YES")
    else:
        print("NO")
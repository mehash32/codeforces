from re import T


t=int(input())
for i in range(t):
    n,m= map(int,input().strip().split())
    if n==1:
        print("0")
    if n==2:
        print(m)
    if n>2:
        print(2*m)
    
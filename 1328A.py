n=int(input())
for i in range(n):
    count=0
    a,b=map(int,input().strip().split())
    if a%b==0:
        print(count)
    else:
        q=a%b
        count=b-q
        print(count)
n=int(input())
for i in range(n):
    a,b=map(int,input().strip().split())
    ans=(min(max(2*b,a),max(2*a,b)))
    print(ans*ans)
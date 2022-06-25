t =int (input())
for j in range(t):
    UpDownMoves=0
    n,m=map(int,input().strip().split())
    temp=m
    UpDownMoves=int((m*(m+1))/2)
    
    for i in range(2,n+1):
        temp=temp+m
        UpDownMoves=UpDownMoves+temp
    
    print(UpDownMoves)

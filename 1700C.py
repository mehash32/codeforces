t=int(input())
while t>0:
    n=int(input())
    moves=0
    lst=list(map(int,input().strip().split()))
    for i in range(len(lst)-1):
        moves=moves+ abs(lst[i+1]-lst[i])
        if lst[i]>lst[i+1]:
            lst[0]=lst[0]+lst[i+1]-lst[i]
    moves=moves+abs(lst[0])
    t=t-1
    print(moves)
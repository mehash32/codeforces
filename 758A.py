n=int(input())
for i in range(n):
    lst=list(map(int,input().strip().split()))
    mx=max(lst)
    count=0
    for j in range(len(lst)):
        count=count+abs(mx-lst[j])
    print(count)
    quit()
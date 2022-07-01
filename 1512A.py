n=int(input())
for i in range(n):
    a=int(input())
    lst=list(map(int,input().strip().split()))
    for j in range(len(lst)-2):
        if lst[j]!=lst[j+1] and lst[j]!=lst[j+2]:
            print(j+1)
            break
        if lst[j]!=lst[j+1] and lst[j]==lst[j+2]:
            print(j+2)
            break
        if lst[j]==lst[j+1] and lst[j]!=lst[j+2]:
            print(j+3)
            break
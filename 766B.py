
n= int(input())
lst = list(map(int,input().strip().split()))
lst.sort()
for i in range(n-2):
    if (lst[i]+lst[i+1])> lst[i+2]:
        print('YES')
        quit()
print('NO')


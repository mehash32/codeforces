n= int(input())
lst = list(map(int,input().strip().split()))
count=0
for i in range(n):
    count= count+lst[i]
print(count)
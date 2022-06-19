a, b = map(int, input().split())
lst= list(map(int, input().strip().split()))
count=lst[0]-1
for i in range(len(lst)-1):
    if lst[i]> lst[i+1]:
        count= count+(a-(lst[i]-lst[i+1]))
    elif lst[i]<lst[i+1]:
        count= count+ (lst[i+1]-lst[i])
print(count)
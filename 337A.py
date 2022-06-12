a,b = map(int,input().strip().split())
lst = list(map(int,input().strip().split()))
lst.sort()
calculation = lst[a-1]-lst[0]
for i in range(0,b-a+1):
    if lst[i+a-1]-lst[i] < calculation:
        calculation = lst[i+a-1]-lst[i]
print(calculation)
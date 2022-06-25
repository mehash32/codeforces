a,b=map(int,input().strip().split())
lst=list(map(int,input().strip().split()))
count=0
diff=0
for i in range(a):
    diff=(86400-lst[i])+diff
    count=count+1
    if diff>=b:
        break               
print(count)
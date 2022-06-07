n=int(input())
count=0
for i in range(n):
    #a = list(map(int,input().strip().split()))
    a,b= map(int,input().strip().split())
    if b-a>=2:
        count+=1
    else:
        continue       
print(count)
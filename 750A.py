a,b =map(int,input().strip().split())
aa=0
count=0
for i in range(1,a+1):
    aa=aa+i*5
    if aa+b<=240:
        count=count+1   
print(count)

n=int(input())
a=[]
count=0
count2=0
count3=0
for i in range(n):
    a = list(map(int,input().strip().split()))
    if i==0:
        count= abs(a[i]-a[i+1])
    else:
        if count>count3:
            count3=count

        count2= abs(count-a[0])
        count=abs(count2)+a[1] 
        
print(count3)
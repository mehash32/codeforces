a,b=map(int,input().strip().split())
count=a
for i in range(b):    
    if count%10==0:
        count=count/10
    else: count-=1
print(int(count))
    
    
    #print(count)
    
#print(count)
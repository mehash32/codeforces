n=int(input())
for i in range(n):
    x,y,n=map(int,input().strip().split())
    if (n-n%x+y)<=n:
        print(n-n%x+y)
    else:
        print(n-n%x-(x-y))
    
            
   
   
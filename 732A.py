a,b =map(int,input().strip().split())
for i in range(1,10):
    if i*a%10==0 or i*a%10==b:
        print(i)
        quit()
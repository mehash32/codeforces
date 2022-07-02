n=int(input())
count1=0
count2=0
for i in range(n):
    a,b=map(int,input().strip().split())
    if a>b:
        count1=count1+1
    if b>a:
        count2=count2+1
if count1>count2:
    print("Mishka")
if count2>count1:
    print("Chris")
if (count1==count2):
    print("Friendship is magic!^^")

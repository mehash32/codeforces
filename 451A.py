a,b =map(int,input().strip().split())
temp=0
if a>b:
    temp=a
    a=b
    b=temp
if a%2==0:
    print("Malvika")
else:
    print("Akshat")
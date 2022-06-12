b=int(input())
if b%2==0:
    if b>=2 and b<5:
        print("Not Weird")
    elif b>=6 and b<=20:
        print("Weird")
    elif b>20:
        print("Not Weird")
else:
    print("Weird")
n=int(input())
for i in range(n):
    a=int(input())
    b=input()
    if int(b[0])==9:
        c=int("1"*(a+1))-int(b)
        print(int(c))
    else:
        c= int("9"*a)-int(b)
        print(c)
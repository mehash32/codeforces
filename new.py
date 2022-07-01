n= int(input())
while n>0:
    if n==1:
        print(n)
        break
    else:
        if n%2==0:
            print(n)
            n=int(n/2)
        
        else:
            print(n)
            n=n*3+1
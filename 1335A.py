n=int(input())
for i in range(n):
    count=0
    n1=int(input())
    if n1<=2:
        print("0")
    else:
        count=int((n1-1)/2)
        print(count)
    # b=n1
    # c=0
    # count=0
    # while(b>c):
    #     b=b-1
    #     c=c+1
    #     count=count+1
    # print(count-1)
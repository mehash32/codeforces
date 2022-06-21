n=int(input())
for i in range(n):
    count=0
    c=0
    a,b =map(int,input().strip().split())
    c=int((abs(a-b)+9)/10)
    print(c)
    # if a==b:
    #     print(count)
    # if a<b:
    #     c=b-a
    #     count=int(c/10)
    #     if count%10==0:
    #         print(count)
    #     else:
    #         print(count+1)
    # if a>b:
    #     c=a-b
    #     count=int(c/10)
    #     if count%10==0:
    #         print(count)
    #     else:
    #         print(count+1)
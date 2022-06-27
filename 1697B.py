a,b = map(int, input().strip().split())
lst= list(map(int, input().strip().split()))
lst.sort(reverse=True)
for i in range(b):
    c,d = map(int, input().strip().split())
    s=0
    lst1=lst[:c]
    #print(lst1)
    s=sum(lst1[-d:])
    #print(lst1[-d:])
    # for j in range(d):
    #     sum= sum + lst[c-1]
    #     c=c-1
    print(s)
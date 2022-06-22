n=int(input())
for j in range(n):
    #lst=list(map(input().strip().split()))
    lst=[]
    s=input()
    lst.append(s[0])
    for i in range(1,len(s)-1,2):
        if s[i]==s[i+1]:
            lst.append(s[i])
    lst.append(s[-1])
    print(''.join(lst))
    



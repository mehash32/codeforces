n=int(input())
lst=list(map(int,input().strip().split()))
lst.sort()
# for i in range(len(lst)-1):
#     if lst[i+1]-lst[i]>1:
#         print(lst[i]+1)
suum=sum(lst)
suum2= int(n*(n+1)/2)
print(suum2-suum)
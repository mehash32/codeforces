n=int(input())
lst=list(map(int,input().strip().split()))
ls1=[]
ls2=[]
ls3=[]
for i in range(n):
    if lst[i]==1:
        ls1.append(i+1)
    if lst[i]==2:
        ls2.append(i+1)
    if lst[i]==3:
        ls3.append(i+1)
mi=0
mi=min(len(ls1),min(len(ls2),len(ls3)))
print(mi)
for j in range(int(mi)):
    print(ls1[j],ls2[j],ls3[j])

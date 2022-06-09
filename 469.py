n=int(input())
lst1= list(map(int,input().strip().split()))
lst2= list(map(int,input().strip().split()))
s1=set()
for i in range(0,len(lst2)):
    if i==0:
        lst1.remove(lst1[i])
    else:
        lst1.append(lst2[i])
for i in range(1,n+1):
    s1.add(i)
s=set(lst1)
if s==s1:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")

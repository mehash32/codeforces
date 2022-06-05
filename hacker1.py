
count1=0
count2=0
lst1= list(map(int,input().strip().split()))
lst2= list(map(int,input().strip().split()))
for i in range(0,len(lst1)):
    if lst1[i]> lst2[i]:
        count1=count1+1
    elif lst1[i]< lst2[i]:
         count2=count2+1      
print(count1, count2)
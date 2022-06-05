from itertools import count
import numpy as np

#line = list(map(int, input().split()))
n = int(input())
 
#a = list((int, input().split())map(int,input().strip().split()))[:n] 
#n= 
n= int(input())
for i in range(n):
    #n1=(int, input().split())

for i in range(n):
    n1=int(input())
    if(n1%4==0):
        
        a=[]
        a1=[]
        a2=[]    
        for i1 in range(2,n1+1,2):
            a1.append(i1)
        for i2 in range(1,n1,2):
            a2.append(i2)
        s1= sum(a1)
        s2= sum(a2)
        diff=s1-s2
        diff1=a2[-1]+diff
        a2[-1]=diff1
        s22= sum(a2)
        if(s1==s22):
            print("YES")
            a=a1+a2
            a=np.asarray(a)
            print(a)
    else:
        print("NO")


    


    






# for i in list(a):
#     if i<=4:
#         taxi=taxi+1
# sum= sum(a)
# if sum%2==0:
#     numoftaxi=round(sum/4)
# else:
#     numoftaxi=round((sum/4)+0.5)
# print(numoftaxi)
n=int(input())
for i in range(n):   
    #a,b,c,d=map(int,input().strip().split())
     lst=list(map(int,input().strip().split()))
     mx=max(lst[0],lst[1]) 
     secondmax=min(lst[0],lst[1])
     for j in range(2,4):
          if lst[j]>mx:
             secondmax=mx
             mx= lst[j]
          elif lst[j]>secondmax:
                 secondmax=lst[j]
     index1= lst.index(mx)
     index2=lst.index(secondmax)
     if(index1 <2 and index2<2):
         print('NO')
     elif index1 >=2 and index2 >=2:
         print('NO')
     else:
          print('YES')

    
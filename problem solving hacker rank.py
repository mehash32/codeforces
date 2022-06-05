n= int(input())
for i in range(0,n):
    a,b =  map(int,input().strip().split())
    lst = list(map(int,input().strip().split()))
    count=1
    for j in range(0,a-1):
         if abs(lst[j+1]-lst[j])<(b):
             if lst[j+1]<lst[j]:
                 count=count+1
             elif lst[j+1]==lst[j]:
                 continue
             else:
                  continue
         else: 
                  continue
    print(count)
         
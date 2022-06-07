n=int(input())
magnetLst=[]
count=1
for i in range(n):
    magnet=input()
    magnetLst.append(magnet)
for j in range(0,n-1):
    if magnetLst[j]!=magnetLst[j+1]:
        count+=1
    else:
        continue
print(count)
    
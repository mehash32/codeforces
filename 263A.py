a=[] 
for i in range(0,5):
 a.append([int(j) for j in input().split()])
for i in range(5):
    for j in range(5):
        if a[i][j]==1:
            a1=i
            a2=j
            break
a3,a4=abs(a1-2),abs(a2-2)
print(a3+a4)



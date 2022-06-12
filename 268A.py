n=int(input())
matt1=[]
matt2=[]
for i in range(n):
    mat1,mat2=map(int, input().split())
    matt1.append(mat1)
    matt2.append(mat2)
cnt=0
for i in range(n):
    for j in range(n):
        if matt1[i]==matt2[j]:
            cnt+=1
print(cnt)

a,b= map(int,input().strip().split())
s= input()
s=list(s)
for i in range(b):
    k=0
    for j in range(a-1):
        j=k
        if k< len(s)-1:
            if s[j]=="B" and s[j+1]=="G":
                s[j], s[j+1] = s[j+1], s[j]
                k+=2           
            else:
                k+=1
                continue
print(s)
print(''.join(s))
    
    
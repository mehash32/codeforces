n=input()
n1=input()
lst=[]
for i in range(len(n)):
    if n[i]==n1[i]:
        lst.append(0)
    else:
        lst.append(1)
print(''.join(map(str,lst)))
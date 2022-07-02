n=int(input())
for i in range(n):
    k=int(input())
    j=1
    while True:
        j=j+1
        k=k-1
        if j%3==0 or int(j/10)==3:
            continue
        if k==0:
            print(j)
        j=j+1
        k=k-1
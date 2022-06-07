from itertools import count


n=int(input())
for i in range(n):
    a=int(input())
    for j in count (0):

        if a & j >0 and a ^ j >0:
            print(j)
            break
        else:
            continue
    
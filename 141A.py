lst1=list(input())
lst2=list(input())
lst=lst1+lst2
lst.sort()
lst3=list(input())
lst3.sort()
if len(lst)==len(lst3):
    for i in range(len(lst)-1):
        if lst[i]!=lst3[i]:
            print("NO")
            quit()
        else:
            continue
    print("YES")
else:
    print("NO")



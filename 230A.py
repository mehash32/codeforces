
a,b = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(b)]
lst.sort()
for i, j in (lst):
    if a > i:
        a=a+j
    else:
        print("NO")
        quit()
        
print ("YES")

















"""
a,b=map(int,input().strip().split())
lst=[[]]
lst1=[]
lst2=[]
for i in range(b):
    c,d=map(int,input().strip().split())
    lst1.append(c,d)
    #lst2.append(d)
print(lst1)
lst1.sort()
lst2.sort()
print(lst1)
print(lst2)
for i in range(b):
    print(lst1[i])
    if lst1[i]>a:
        print("NO")
        quit()
    else:
        a=a+lst2[i]
        continue
print("YES")
#     if c>a:
#         print("NO")
#         quit()
#     else:
#         a=a+d
#         continue
# print("YES")
    """

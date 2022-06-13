#from math import ceil
n= int (input())
lst=list(map(int,input().strip().split()))
one=lst.count(1)
two= lst.count(2)
three=lst.count(3)
four= lst.count(4)
lst.sort(reverse=True)
count=four
if three>=one:
    three=three-one
    count= count+one+three
    one=0
else:
    one= one-three
    count= count+three
    three=0
num=two*2+one
celi=-(-num//4)
count=count+ celi
print(count)


from math import ceil


n= int (input())
lst=list(map(int,input().strip().split()))
one=lst.count(1)
two= lst.count(2)
three=lst.count(3)
four= lst.count(4)
print(four)
print(three)
print(two)
print(one)
lst.sort(reverse=True)
count=four
res = list(filter((4).__ne__, lst))
if three>=one:
    three=three-one
    count= count+one+three
    one=0
    print("ahdfoaf",count)
    res = list(filter((3).__ne__, res))
    res = list(filter((1).__ne__, res))
    #print(res)
else:
    one= one-three
    count= count+three
    three=0
    print("ahhhhh")
    #res = list(filter((1).__ne__, lst))
    for i in range(three):
        res.remove(1)
# elif two%4==0:
#     count=count+two/2
#     res = list(filter((2).__ne__, lst))

num=two*2+one
print(num)

# celi function without math
##celi=-(-num//2)
# floor function without math
##floor=(num//2)

count=count+ceil(num/4)   
#print(res)
print(count)
# print(lst)
# print(four)
# print(three)
# print(two)
# print(one)
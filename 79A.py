from posixpath import split


a,b=map(int,input().strip().split())
count=0
while a<=b:
    a=a*3
    b=b*2
    count=count+1
print(count)
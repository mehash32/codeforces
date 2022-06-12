
n=int(input())
count=0
 
left=0
count=int(n/100)
left=n%100

count+= int(left/20)
left= left%20

count+= int(left/10)
left= left%10

count+= int(left/5)
left= left%5

count+= int(left/1)
print(count)


"""
Alternative solution

n=int(input())
c1=0
c2=0
c3=0
c4=0
c5=0
if n>=100:
    c1=int(n/100)
    n=n-100*c1

if n>=20:
    c2=int(n/20)
    n=n-20*c2
    

if n>=10:
    c3=int(n/10)
    n=n-10*c3

if n>=5:
    c4=int(n/5)
    n=n-5*c4

if n>=1:
    c5=int(n/1)
    n=n-1*c5
  
print(c1+c2+c3+c4+c5)

"""
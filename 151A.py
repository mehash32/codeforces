n,k,l,c,d,p,nl,np=map(int,input().strip().split())
count1=0
count2=0
count3=0
count1=int(k*l/nl)
count2=c*d
count3= int(p/np)
mi=0
mi=min(count1,count2)
mi=int(min(mi,count3)/n)
print(mi)
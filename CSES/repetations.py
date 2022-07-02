s=input()
count=1
count1=1
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        count=count+1
        if count1<count:
            count1=count
    else:
        count=1
print(count1)
    


    

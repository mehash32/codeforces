string= input()
up=0
lo=0
flag=0
count=1
string=list(string)
if string[0].islower():
    for i in range(1,len(string)):
        if string[i].isupper():
            up+=1
        else:
            lo+=1   
    if lo>0 and up>0:
        flag=1
    elif lo==len(string) or lo>0:
        if lo==1:
            string[0]=string[0].upper()
        else:
            for i in range(1,len(string)):
                string[i]=string[i].lower()
    elif up==len(string)-1:
        string[0]=string[0].upper()
        for j in range(1,len(string)):
            string[j]=string[j].lower()
else:
    for i in range(1,len(string)):
        if string[i].isupper():
            count+=1
            continue
        else:
            break
    if count==len(string):
        for i in range(0,len(string)):
            string[i]=string[i].lower()
if flag==1:
    print(''.join(string))
else:
     print(''.join(string))   

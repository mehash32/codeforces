s=input()
count=0
sub="hello"
for i in range(len(s)):
    if s[i]==sub[count]:
        count+=1
        if count==5:
            break
if count==5:
    print("YES")
else:
    print("NO")
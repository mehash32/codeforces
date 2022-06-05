str=input()
count = 0
for elem in str:
    if elem.isupper():
        count += 1
lower=len(str)-count
if count>lower:
    str=str.upper()
else:
    str=str.lower()
print(str)

line= input()
if ord(line[0])>=97 and ord(line[0])<=122:
    output_line= chr(ord(line[0])-32)+line[1:]
    print(output_line)
else:
    print(line)


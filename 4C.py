n = int(input())
dict = {}
for i in range( n):
    string = input()
    if string in dict:
        print(string+str(dict[string]))
        dict[string] += 1
    else:
        print("OK")
        dict[string] = 1
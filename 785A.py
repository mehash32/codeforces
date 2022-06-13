n=int(input())
count=0
for i in range(n):
    string=input()
    if string=="Icosahedron":
        count=count+ 20
    elif string=="Dodecahedron":
        count=count+ 12
    elif string=="Octahedron":
        count=count+ 8
    elif string=="Cube":
        count=count+ 6
    elif string=="Tetrahedron":
        count=count+ 4
print(count)
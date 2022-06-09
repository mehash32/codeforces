n= int(input())
lst=list(map(int,input().strip().split()))
new_list = []
while lst:
    min = lst[0]  
    for x in lst: 
        if x < min:
            min = x
    new_list.append(str(min))
    lst.remove(min)    
print(' '.join(new_list))


#alterbate sorting
'''
n= int(input())
lst1=[]
lst=list(map(int,input().strip().split()))
lst.sort()
list_string = map(str, lst)
print(' '.join(list_string))

'''
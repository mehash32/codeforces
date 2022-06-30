
n=int(input())
quant=int((-1)*n/pow(10,1))
rem1=(-1)*n%10
rem2=quant%10
if n>0:
    print(n)
else:
    if rem1>rem2:
        op1=int(n/10)
        print(op1)
    else:
        op2=int(-1*n/100)*10+rem1
        print(-1*op2)

# print("rem2",rem2)
# print("rem1",rem1)
# print(quant)


# n1=str(n)
# lst=list(n1)
# mx=0
# print(lst[-1])
# print(lst[-2])
# if int(n)>=0:
#     print(n)
# else:
#     if int(lst[-1])>int(lst[-2]):
#         lst.remove(lst.index(lst[-1]))
#     else:
#         lst.remove(lst.index(lst[-2]))
#     print(lst)
#     # if int(lst[-2])>=1:
#     #     lst.remove(lst[-2])
#     #     if lst[0]=="-" and lst[1]=="0":
#     #         lst.remove(lst[0])
#     #     print("".join(lst))
#     # else:
#     #     if int(lst[-2])==0 and int(lst[-1])>0:
#     #         lst.remove(lst[-1])
#     #         print("".join(lst))


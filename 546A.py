from re import I
price,balance,amount=map(int,input().strip().split())
cost=0
for i in range(1,amount+1):
    cost= cost+(price*i)
if cost>balance:
    need= abs(cost-balance)
else:
    need=0
print(need)
    
import random
print("How many dice to roll?")
a=int(input())
s=0
i=1
for i in range(1, a):
    d=random.randint(1,6)
    i=i+1
    s+=d
print(s)


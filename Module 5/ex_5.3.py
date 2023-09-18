a=int(input())
b=0
for i in range(2, a//2+1):
    if (a%i)==0:
        b=b+1
if b<=0:
    print(a,"is a prime number")
else:
    print(a,"isn't a prime number")

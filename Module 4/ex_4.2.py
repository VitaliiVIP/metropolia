inches=int(input())
centi=inches*2.54
while inches>=0:
    print(inches, centi)
    inches = int(input())
    centi = inches * 2.54
    if inches<0:
        break
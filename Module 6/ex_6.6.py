d1=int(input("Pizza 1 diam:"))
p1=int(input("Pizza 1 price:"))
d2=int(input("Pizza 2 diam:"))
p2=int(input("Pizza 2 price:"))
def fun():
    s1=3.1416*(d1/2)**2
    s2=3.1416*(d2/2)**2
    dif1=p1/s1*10000
    dif2=p2/s2*10000
    if dif1>dif2:
        print("The first pizza is better")
    elif dif1 < dif2:
        print("The second pizza is better")
    elif dif1==dif2:
        print("No difference")
fun()
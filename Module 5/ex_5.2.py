a=input()
list=[]
while a!="":
    list.append(a)
    print(a)
    a=input()
s=list.sort(reverse=True)
if a=="":
    print(list)
    print(s)


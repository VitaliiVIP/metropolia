a=input()
list=[]
while a!="":
    list.append(a)
    print(a)
    a=input()
max=max(list)
min=min(list)
if a=="":
    print(list)
    print(max)
    print(min)
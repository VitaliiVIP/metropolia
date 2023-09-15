a=1
logint=input()
passint=input()
while logint!="vitaliivip" and passint!="2307":
    logint = input()
    passint = input()
    a+=1
    if a==5:
        print("Access denied, fuck you")
        break
if logint=="vitaliivip" and passint=="2307":
    print("Welcome")

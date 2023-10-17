names = []
icaos = []
while 1:
    menu="1.New airport\n2.Existing airport\n3.Exit"
    print(menu)
    choice=int(input())
    if choice==1:
        name=input("Enter the name: ")
        icao=input("Enter the ICAO: ")
        names.append(name)
        icaos.append(icao)
    if choice == 2:
        icao = input("Enter the ICAO: ")
        if icao in icaos:
            index=icaos.index(icao)
            print(names[index])
    if choice==3:
        break




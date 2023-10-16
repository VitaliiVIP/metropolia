names = set()
while 1:
    name = input()
    if name == "":
        break
    if name in names:
        print("Existing name")
    else:
        print("New name")
        names.add(name)
for name in names:
    print(name)

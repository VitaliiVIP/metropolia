print("a")
print("b")
print("c")

x=int(input("How much cash you have?\n"))
str = "You have {} cash"
print(str.format(x))
print(f"you said that you have {x}")


if (x>1000):
        print("You are rich")
elif x > 10:
    print("You have more than 10 euros")
else: print("You have less than 10 euros")
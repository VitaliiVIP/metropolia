import random
side=int(input())
def roll():
    a=random.randint(1, side)
    print(a)
    if a == side:
        print("The end")
    else:
        roll()
    return
roll()

import random
def roll():
    times=0
    while True:
        a = random.randint(1, 6)
        result = a
        times += 1
        print(f"Roll {times}: {result}")
        if result == 6:
            break
roll()
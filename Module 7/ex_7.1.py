month=int(input())
seasons=("winter", "spring", "summer", "autumn")
if month == 1 or 2 or 12:
    print(seasons[0])
elif month == 3 or 4 or 5:
    print(seasons[1])
elif month == 6 or 7 or 8:
    print(seasons[2])
elif month == 9 or 10 or 11:
    print(seasons[3])
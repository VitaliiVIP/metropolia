talents=float(input("Enter talents:\n"))
pounds=float(input("Enter pounds:\n"))
lots=float(input("Enter lots:\n"))
kilo=talents*20*32*13.3/1000+pounds*32*13.3/1000+lots*13.3/1000
kilograms=kilo//1
grams=kilo%1
print("The weight in modern units:\n", kilograms, "kilograms and", grams*1000, "grams")
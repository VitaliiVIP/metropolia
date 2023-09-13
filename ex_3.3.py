gn=str(input("Your biological gender:\n"))
gl=int(input("Hemoglobin value\n"))
if gn=="Male" and gl<134:
    print("low")
elif gn=="Male" and gl>167:
    print("high")
elif gn=="Male" and 167>=gl>=134:
    print("normal")
if gn=="Female" and gl<117:
    print("low")
elif gn=="Female" and gl>155:
    print("high")
elif gn=="Female" and 155>=gl>=117:
    print("normal")

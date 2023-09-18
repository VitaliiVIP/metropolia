k=1
city_list=[]
for i in range(5):
    a=input("Enter name of the city: ")
    city_list.append(a)
k=1
for c in city_list:
    print(f"{c}","-",k,"city")
    k=k+1

listt = [1, 2, 3, 4, 5, 6, 8, 10]
def fun():
    list_2=[]
    for i in listt:
        if i%2 == 0:
            list_2.append(i)
    print("New list:", list_2)
    return(i)
fun()

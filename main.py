pi: float=3.141592656
formatPI="value of PI: {:.5f}".format(pi)
print(formatPI)
radius=float(input("Enter the radius"))
area=pi*radius**2
print(f"Are of circle area {area:.2f}")
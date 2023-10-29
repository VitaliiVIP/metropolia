class Car:
    def __init__(self, reg_number, max_speed, cur_speed, distance):
        self.reg_number=reg_number
        self.max_speed=max_speed
        self.cur_speed=cur_speed
        self.distance=distance

cartype=input("New or old car?\n")
car=Car("l456OH", 230, 120, 1000)
if cartype=="New":
    car=Car("ABC-123", 142, 0, 0)
else:
    car = Car("l456OH", 230, 120, 1000)
print(f"{car.reg_number:} max speed is {car.max_speed:d}, current speed is {car.cur_speed:}, distance is {car.distance:}" )
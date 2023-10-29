n=0
while n!=10:
    class Car:
        def __init__(self, reg_number, max_speed, cur_speed, distance):
            self.reg_number=reg_number
            self.max_speed=max_speed
            self.cur_speed=cur_speed
            self.distance=distance
        def drive(self, hours):
            self.distance=self.distance+hours*self.cur_speed
    r=randomize(100, 201)
    m=
    c=
    d=
    car = Car("ABC", 142, 60, 2000)
    car.drive(1.5)
    print(
        f"{car.reg_number:} max speed is {car.max_speed:d}, current speed is {car.cur_speed:}, distance is {car.distance:}")
    n+=1

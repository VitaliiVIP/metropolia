class Car:
    def __init__(self, reg_number, max_speed, cur_speed, distance):
        self.reg_number=reg_number
        self.max_speed=max_speed
        self.cur_speed=0
        self.distance=0
    def acceleration(self, accel):
        self.cur_speed += accel
        if self.cur_speed>=self.max_speed:
            self.cur_speed=self.max_speed
        elif self.cur_speed<0:
            self.cur_speed=0
car=Car("ABC123", 142, 0, 0)
car.acceleration(143)
print(f"{car.reg_number:} max speed is {car.max_speed:d}, current speed is {car.cur_speed:}, distance is {car.distance:}" )
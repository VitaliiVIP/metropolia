import random

class Car:
    def __init__(self, reg_number, max_speed, cur_speed, distance):
        self.reg_number=reg_number
        self.max_speed=max_speed
        self.cur_speed=cur_speed
        self.distance=0
    def acceleration(self, accel):
        self.cur_speed += accel
        if self.cur_speed>=self.max_speed:
            self.cur_speed=self.max_speed
        elif self.cur_speed<0:
            self.cur_speed=0

    def drive(self, hours):
        self.distance = self.distance + hours * self.cur_speed


def fun():
    while True:
        for car in cars:
            a = random.randint(-10, 15)
            car.acceleration(a)
            car.drive(1)
            if car.distance>=10000:
                return


# create cars
cars=[]
for i in range (1, 11):
    m = random.randint(100, 200)
    d = 0
    c = 0
    car=Car("ABC-" + str(i), m, c, d)
    car.max_speed=random.randint(100, 200)
    cars.append(car)

# drive cars
fun()

# print result
for car in cars:
    print(f"{car.reg_number:} max speed is {car.max_speed:d}, distance is {car.distance:}")

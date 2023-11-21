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

class Race:
    def __init__(self, name, distance, listcars):
        self.name=name
        self.distance=distance
        self.listcars=listcars

    def hour_passes(self):
        for car in self.listcars:
            a = random.randint(-10, 15)
            car.acceleration(a)
            car.drive(1)

    def print_status(self):
        print(f"{self.name}")
        print(f"{'Car'}\t{'Max Speed'}\t{'Distance'}")
        for car in self.listcars:
            print(f"{car.reg_number}\t{car.max_speed}\t\t{car.distance}")

    def race_finished(self):
        for car in self.listcars:
            if car.distance>=self.distance:
                return True
        return False

listcars=[]
for i in range (1, 11):
    m = random.randint(100, 200)
    d = 0
    c = 0
    car=Car("ABC-" + str(i), m, c, d)
    car.max_speed=random.randint(100, 200)
    listcars.append(car)

derby=Race("Grand Demolition Derby", 8000, listcars)
hour_counter=0
while not derby.race_finished():
    hour_counter+=1
    derby.hour_passes()
    if hour_counter%10==0:
        derby.print_status()

derby.print_status()

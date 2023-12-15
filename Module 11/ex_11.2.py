import random
class Car:
    def __init__(self, reg_number, max_speed, cur_speed, distance):
        self.reg_number = reg_number
        self.max_speed = max_speed
        self.cur_speed = cur_speed
        self.distance = distance

    def acceleration(self, accel):
        self.cur_speed += accel
        if self.cur_speed >= self.max_speed:
            self.cur_speed = self.max_speed
        elif self.cur_speed < 0:
            self.cur_speed = 0

    def drive(self, hours):
        self.distance = self.distance + hours * self.cur_speed

class ElectricCar(Car):
    def __init__(self, reg_number, max_speed, cur_speed, distance, battery_capacity):
        super().__init__(reg_number, max_speed, cur_speed, distance)
        self.battery_capacity = battery_capacity

class GasolineCar(Car):
    def __init__(self, reg_number, max_speed, cur_speed, distance, tank_volume):
        super().__init__(reg_number, max_speed, cur_speed, distance)
        self.tank_volume = tank_volume

electric_car = ElectricCar("ABC-15", 180, 0, 0, 52.5)
gasoline_car = GasolineCar("ACD-123", 165, 0, 0, 32.3)
electric_car.cur_speed = random.randint(0, electric_car.max_speed)
gasoline_car.cur_speed = random.randint(0, gasoline_car.max_speed)
for i in range(3):
    electric_car.drive(1)
    gasoline_car.drive(1)
print(f"Electric car distance: {electric_car.distance} km")
print(f"Gasoline car distance: {gasoline_car.distance} km")

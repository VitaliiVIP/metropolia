class Elevator:
    def __init__(self, current_floor, bottom_floor, top_floor):
        self.current_floor = current_floor
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor

    def floor_up(self):
            self.current_floor+=1
            if self.current_floor==1:
                print(f"Elevator is now on {self.current_floor}" + "st" + " floor")
            elif self.current_floor==2 or self.current_floor==3:
                print(f"Elevator is now on {self.current_floor}"+"d"+" floor")
            else:
                print(f"Elevator is now on {self.current_floor}" + "th" + " floor")

    def floor_down(self):
            self.current_floor-=1
            print(f"Elevator is now on floor {self.current_floor}")

    def go_to_floor(self, floor):
        while self.current_floor != floor:
            if floor==self.current_floor:
                print("Here we go")
            if floor>self.current_floor:
                self.floor_up()
            if floor<self.current_floor:
                self.floor_down()
            print(f"{self.current_floor}")
        else:
            print("Here we go")
class Building:
    def __init__(self, bottom_floor, top_floor, elevators):
        self.bottom_floor=bottom_floor
        self.top_floor=top_floor
        self.elevators=[Elevator(bottom_floor, bottom_floor, top_floor) for i in range(elevators+1)]

    def run_elevator(self, elevator, destination_floor ):
        if 0<=elevator<len(self.elevators):
            elevator=self.elevators[elevator]
            elevator.go_to_floor(destination_floor)

building=Building(0, 12, 4)
building.run_elevator(1, 12)
class Elevator:
    def __init__(self, current_floor, bottom_floor, top_floor):
        self.current_floor = current_floor
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor

    def floor_up(self):
            self.current_floor+=1
            print(f"Elevator is now on floor {self.current_floor}")

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

elevator=Elevator(1, 1, 12)
elevator.go_to_floor(6)

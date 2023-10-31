class Animal:
    def __init__(self, name):
        self.name=name
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("Woof woof")
dog=Dog("Snowy")
print(f"My dog name is: {dog.name}")
dog.speak()

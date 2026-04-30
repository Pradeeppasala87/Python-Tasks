class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

class Car(Vehicle):
    def show(self):
        print(f"Car Brand: {self.brand}, Speed: {self.speed}")

class Bike(Vehicle):
    def show(self):
        print(f"Bike Brand: {self.brand}, Speed: {self.speed}")

c = Car("Toyota", 120)
b = Bike("Yamaha", 90)

c.show()
b.show()

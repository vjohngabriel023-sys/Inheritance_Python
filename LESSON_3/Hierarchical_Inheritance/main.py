print(" ~~Hierarchical Inheritance~~ ")

class Vehicle:
    """Parent Class"""
    def __init__(self, brand):
        self.brand = brand
    
    def start(self):
        return f"{self.brand} is starting."

class Car(Vehicle):
    def honk(self):
        return f"{self.brand} honks loudly."

class Motorcycle(Vehicle):
    def rev(self):
        return f"{self.brand} revs its engine."

car = Car("Toyota")
motorcycle = Motorcycle("Honda")

print(car.start())
print(car.honk())
print(motorcycle.start())
print(motorcycle.rev())
print("-" * 30)

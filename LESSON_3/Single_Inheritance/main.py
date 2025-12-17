print(" ~~Single Inheritance~~ ")

class Vehicle:
    def __init__(self, model):
        self.model = model
    
    def display_model(self):
        return f"Vehicle Model: {self.model}"

class Car(Vehicle):
    def __init__(self, model, car_id):
        super().__init__(model)
        self.car_id = car_id
    
    def car_info(self):
        return f"{self.display_model()}, Car ID: {self.car_id}"

car = Car("Honda Civic", "C123")
print(car.car_info())
print("-" * 30)
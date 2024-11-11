class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car Details: {self.year} {self.make} {self.model}")

# Creating an instance and calling display_info
car1 = Car("Toyota", "Corolla", 2020)
car1.display_info()

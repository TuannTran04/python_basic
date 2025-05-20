from car import Car

car1 = Car("Toyota", 2020, "Red", True)
car2 = Car("Mecx", 2022, "Pink", False)

print(car1.model)
print(car1.year)
car1.drive()
car1.stop()

print(Car.num_cars)

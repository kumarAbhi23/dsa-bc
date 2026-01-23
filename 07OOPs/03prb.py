'''
static methods
# static methods are methods that belong to the class rather than any specific instance
# they do not have access to instance (self) or class (cls) variables
# they are defined using @staticmethod decorator    

# why static methods?
# 1. utility functions that do not need access to instance or class variables
# lets understand with a simple real world example


i wanted to create a function to convert miles to kilometers
# this function does not need access to any instance or class variables
# so we can define it as a static method inside a class


'''
# add a static method to Car class that return general info about cars

class Car:
    @staticmethod
    def general_info():
        return "Cars are vehicles that run on roads and are used for transportation. it has 4 Wheels"
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year    
    def display_info(self):
        print(f"Car Make: {self.make}, Model: {self.model}, Year: {self.year}")    
    
    
    
# calling static method without creating object of class
#print(Car.general_info())

# let's see if we crate an object of Car class and call static method using object
my_car = Car("Toyota", "Camry", 2020)
my_car.display_info()
print(my_car.general_info())  # static method can be called using object but not recommended

# static methods are also known as decorator methods as they are defined using @staticmethod decorator

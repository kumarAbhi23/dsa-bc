#polymorphism in OOPs
# ability to use same method name in different classes


# lets see car and electric car classes again with same method name start_engine
class Car:
    # class varaible 
    total_cars = 0
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        Car.total_cars+=1
        
   
    def fuel_type(self):
        print("Fuel type: Gasoline")   
      
        

class ElectricCar(Car):
    def __init__(self, make, model, year, battery_capacity):
        super().__init__(make, model, year)
        self.battery_capacity = battery_capacity

    def fuel_type(self):
        print("Fuel type: Electric as it is an electric car")


# create objects of both classes
my_car = Car("Toyota", "Camry", 2020)
my_electric_car = ElectricCar("Tesla", "Model S", 2022, 100)

# call fuel_type method on both objects
my_car.fuel_type()            # Output: Fuel type: Gasoline
my_electric_car.fuel_type()   # Output: Fuel type: Electric as it is        

# we call same method name fuel_type on different classes and get different behavior


# 2.add a class varaible  to car class to keep track of number of cars created
# basically we need keep track of how many objects of car class are created

# class variable is shared among all objects of the class and it declared inside the class but outside any method

# we can access class variable using class name or using self keyword inside methods but use class name to avoid confusion 

my_car1 = Car("Honda", "Civic", 2019)
my_electric_car1 = ElectricCar("Nissan", "Leaf", 2021, 40)
print("Total cars created:", Car.total_cars)  # Output: Total cars created: 2


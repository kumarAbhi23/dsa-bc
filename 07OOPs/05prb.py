'''


class Inheritance and isinstance() function

demonstration the use of inheritance() to check my_tesla is instance of ElectricCar and Car classes
'''


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        
    def display_info(self):
        print(f"Car Make: {self.make}, Model: {self.model}, Year: {self.year}") 

      
class ElectricCar(Car):
    def __init__(self, make, model, year, batterySize):
         super().__init__(make, model, year)
         self.batterySize = batterySize

    def display_info(self):
        print(f"Car Make:{self.make} car model: {self.model} year:{self.year},battery size:{self.batterySize}kWh")
        

my_tesla=ElectricCar("Tesla","Model S",2022,100)
my_tesla.display_info()

# now we will use isinstance() function to check if my_tesla is instance of ElectricCar and Car classes
# syntax:isinstance(object, classinfo) it will return True if object is instance of classinfo otherwise False

print(isinstance(my_tesla, ElectricCar))  # True
print(isinstance(my_tesla, Car))          # True


# multipe inheritance is possible 
# lets see an example of multiple inheritance
# both multiple and multilevel inheritance is possible in python 


''' 
make two class battery and engine and make an electric car class that inherits from both battery and engine classes


'''

class Battery:
    def __init__(self,battery_capacity):
        self.battery_capacity = battery_capacity  
    
    def display_battery(self):
        print(f"Battery Capacity: {self.battery_capacity}kWh")      
        
class Engine:
    def __init__(self,engine_type):
        self.engine_type = engine_type
        
    def display_engine(self):
        print(f"Engine Type: {self.engine_type}")    

class EvCar(Battery,Engine):    
    def __init__(self,make,model,year,battery_capacity,engine_type):
        Battery.__init__(self,battery_capacity)
        Engine.__init__(self,engine_type)
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car Make:{self.make}, Model:{self.model}, Year:{self.year}, Battery Capacity:{self.battery_capacity}kWh, Engine Type:{self.engine_type}")
        
    
my_new_ev = EvCar("Nissan","Leaf",2021,40,"Electric")
my_new_ev.display_engine()
my_new_ev.display_battery()          

'''

use a property decorator in Car class to make model attribute read-only
# property decorator is used to define getter method for an attribute
# it allows us to access the attribute like a normal attribute but we cannot set its value directly
'''


# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model   # private attribute with single underscore
#         self.year = year
     
#     def display_info(self):
#         print(f"Car make: {self.make}, Model: {self.model}, Year: {self.year}")


# # lets  create an object of Car class and access model
# my_car = Car("Toyota", "Camry", 2020)

# (my_car.display_info())  # Car make: Toyota, Model: Camry, Year: 2020

 
# # lets update model directly
# my_car.model = "Corolla"  # updating model directly
# my_car.display_info()  # Car make: Toyota, Model: Corolla, Year: 2020

# now we will make restict access to model attribute to read only using property decorator

 # first make model attribute private by adding double underscore
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.__model = model   # private attribute with double underscore but we will provide read access using property decorator
        self.year = year
     
    def display_info(self):
        print(f"Car make: {self.make}, Model: {self.__model}, Year: {self.year}")
     # add property decorator to make model read-only   
    @property
    def model(self):
        return self.__model 
    #@property: use to define getter method for model attribute which allows read access 
    
# lets  create an object of Car class and access model
my_car = Car("Toyota", "Camry", 2020)
my_car.display_info()  # Car make: Toyota, Model: Camry, Year: 2020

# lets try to update model directly
my_car.model = "Corolla"  # trying to update model directly will raise AttributeError:can't set attribute
 
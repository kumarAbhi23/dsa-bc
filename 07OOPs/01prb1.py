'''
 basic structure of OOPs in python
    class : blueprint
    object : instance of class
    attributes : variables in class
    methods : functions in class
    constructor : __init__() : special method to initialize object attributes
    self : reference to current instance of class
    inheritance : mechanism to derive new class from existing class
    polymorphism : ability to use same method name in different classes
    encapsulation : restricting access to methods and attributes
    abstraction : hiding complex implementation details and showing only essential features
    
'''

# syntax of class and object
class Car:
    # attributes we need to define while creating object
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        
        # --init-- : constructor to initialize object attributes
        # self : reference to current instance of class and used to access attributes and methods of class
        
    def display_info(self):
        print(f"Car Make: {self.make}, Model: {self.model}, Year: {self.year}")
         

# creating object of class Car
my_car = Car("Toyota", "Camry", 2020)
my_car.display_info()  



# inheritance example
# inheritance : mechanism to derive new class from existing class
# crate an electic car class derived from car class and has an additional attribute battery_size
  
class ElectricCar(Car):
    # we need add additional attribute battery_size
    def __init__(self, make, model, year, battery_size):
        # call parent class constructor
        self.battery_size = battery_size
        super().__init__(make, model, year)  # calling parent class constructor using super()
        
 
my_tesla = ElectricCar("Tesla", "Model S", 2022, 100)  
my_tesla.display_info()  



# Encapsulation example
# restricting access to methods and attributes using private attributes and methods
# private attributes and methods are prefixed with double underscore __
# use getter and setter methods to access private attributes


class BankAccount:
    def __init__(self, account, balance):
       self.__account = account   # private attribute wrapped with double underscore
       self.__balance = balance   # private attribute  w

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Invalid deposit amount") 
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: {amount}")
        else:
            print("Invalid withdraw amount or insufficient funds")
    def get_balance(self):
        return self.__balance        
    
my_account = BankAccount("123456789", 1000)
my_account.deposit(500)
my_account.withdraw(200)
print("Current balance:", my_account.get_balance())
         
         
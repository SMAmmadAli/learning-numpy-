# Classes & Objects

# A class is a blueprint; an object is an instance.

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
my_car = Car("Toyota", "Corolla")


# Attributes & Methods

# Attributes = variables in a class

# Methods = functions inside a class

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def detail(self):
        print(self.model, self.brand)
        

new_car = Car("Toyota", "Corolla")

new_car.detail()

# Encapsulation (hiding data)

# Use _protected or __private naming convention

class Account:
    def __init__(self, balance):
        self.__balance = balance  # private

    def get_balance(self):
        return self.__balance


# Inheritance (reuse & extend classes)
class Animal:
    def speak(self):
        print("Some sound")

class Cat(Animal):   # inherits Animal
    def speak(self):
        print("Meow")

kitty = Cat()
kitty.speak()  # Meow

# Polymorphism (same method, different behavior)
for animal in [Cat(), Animal()]:
    animal.speak()

# Abstraction (blueprint methods, must be implemented)

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        return 3.14 * self.r * self.r
    
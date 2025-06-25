#### OOPs 

'''
It is a way to design programs using objects,Where objects contain data as attributes and functions as method.

Class is a blue print for creating object. it deines attributes and methods.

Object is an instance of a class.(a class can be only called using object)

'''
class person:
    def __init__(self, name , age):# __init__ means to initialize the object and it is always executed when an object is created 
        self.name = name # self it points to your current object and it is used to store data inside the object.
        self.age = age
    def wish(self):
        print(f"Hello {self.name}")

p = person("Aadi",20)
# p.wish()

class Animal:
    def __init__(self,eyes,sound):
        self.eyes=eyes
        self.sounds=sound
    def sound(self):
        print(f"sound: {self.sounds}")

o=Animal("black","mooo")
# o.sound()

class Car:
    def __init__(self,color,name,speed,yearOfManufactre) :
        self.color=color
        self.name=name
        self.speed=speed
        self.yom=yearOfManufactre

    def details(self):
        print(f"""
        NAME = {self.name}
        COLOR = {self.color}
        TOP SPEED =  {self.speed}
        YEAR OF PRODUCTION = {self.yom}
                """)

car = Car("Red", "Mazda", 200 , 2025)
# car.details()
# print(p.name)

# p.name = "Aadi"
# print(p.name)

# Pillers of OOPs

''' 
1. Inheritance
2. Encapsulation
4. Abstraction
5. Polymorphism
'''

######## Inheritance #########
''' 
It allows one class to inherit attributes and methods, from other class (child class and parent class or sub class or super class) child class inherit properties from parent class and can have properties of there own 
'''

class Father:# parent class
    def fatherMethod(self):# parent Method
        print("parent")
    
class child(Father):# child class
    def salary(self):# child property
        print("Own ")

# aadi=child()
# aadi.fatherMethod()
# aadi.salary()

# father=Father()
# father.fatherMethod()
# father.salary() # not callable as it is method of child class and object is of parent class

'''
Types of inheritance
1: Single inheritance - (Single parent single child)
2: Multiple inheritace - (multiple parent single child)
3: Multilevel inheritance - (multiple levels of inheritance grandparent to parent to child)
4: Hierarchical inheritance - (single parent multiple child)
5: Hybrid inheritance - (combination of different inheritances)
'''

class Father:
    def father(self):
        print("Father")
    
class Mother:
    def mother(self):
        print("Mother")

class child(Father,Mother):
    def myself(self):
        print("Own ")

aadi = child()
# aadi.father()
# aadi.mother()
# aadi.myself()




########### Encapsulation ##########

''' 
It hides internal object details and exposes only what is necessary
can be done using access specfiers

Acces specifiers:
1. Public - 
2. Protected - (will only be accessed in the class and its subclass) (add underscore before the attribute, ex: _name)
3. Private - (cannot access outside the class)( are identified with a __(doubble undersore) and cannot be accessed directly from outside the class, Trying to access private attribute directly will result in attribute error )
'''

class Protected:
    def __init__(self) :
        self._age = 30

class sub(Protected):
    def displayAge(self):
        print(f"Age = {self._age}")

obj = sub()
obj.displayAge()


class private:
    def __init__(self):
        self.__slary=2000000000
    def sal(self):
        print(f"Salary: {self.__slary}")

obj= private()
obj.sal()


########### Abstraction ##########

'''
abstraction means hiding internal implimentation and showing only the necessary details.
It helps to reduce complexity and increase security, by exposing only essential methods and hiding background logic.
Python uses abstract base classes to impliment abstraction
abstract method in the parent class should be implimented in the child class
'''
from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
class Car(Vehicle):
    def start(self):
        print("Car Starterd")

class Bike(Vehicle):
    def start(self):
        print("Bike Started!!")
    
V1= Car()
V2 = Bike()
V1.start()
V2.start()


class PaymentMethod(ABC):
    @abstractmethod
    def pay(self):
        pass
class Upi(PaymentMethod):
    def pay(self):
        print("Pay using upi")
class card(PaymentMethod):
    def pay(self):
        print("Pay using credit card.")


######## Polymorphism #########
'''
It allows different classes to define methods with the same name that behave differently 

Types of polymorphism:
1) Runtime polymorphism -- Method Overriding (method name same but the implementation would be different in parent and child class)
2) 

'''



class Bird:
    def sound(self):
        print("Chirp")
class Cat:
    def sound(self):
        print("Meow")
def make_sound(animal):
    animal.sound()

b=Bird()
c=Cat()
make_sound(b)
make_sound(c)

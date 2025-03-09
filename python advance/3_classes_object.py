# Python Classes and Objects

#         What Are Classes and Objects?
#         In Python, everything is an object—even numbers, strings, and lists.
#
#         A Class is a blueprint for creating objects (like a cookie cutter).
#         An Object is an actual instance created from the class (like a real cookie).
#         For example, if we think of a car:
#
#         The Class → A blueprint defining car properties (brand, color, speed).
#         The Object → A real car like a red Ferrari or a blue Tesla.


# ----------------------------------Creating a Class and an Object---------------------------------
# A class is defined using the class keyword, and an object is created from that class.
#
# Example: Creating a Class (Blueprint)

class Car:
    def __init__(self, brand, color, speed):  # Constructor
        self.brand = brand  # Attribute
        self.color = color  # Attribute
        self.speed = speed  # Attribute

    def drive(self):  # Method (Behavior)
        print(f"The {self.color} {self.brand} is driving at {self.speed} km/h")

# Creating objects from the Car class
car1 = Car("Toyota", "Red", 60)
car2 = Car("BMW", "Blue", 80)

car1.drive()  # The Red Toyota is driving at 60 km/h
car2.drive()  # The Blue BMW is driving at 80 km/h


# Breakdown of This Example:
    # Car class → Defines a template for creating car objects.
    # __init__() method → A special method called a constructor that runs when a new object is created.
    # Attributes (brand, color, speed) → Data stored inside the object.
    # Methods (drive) → Actions the object can perform.

# ------------------------------------The __init__ Method (Constructor)------------------------------------
    # The __init__() method is a special method that is automatically called when an object is created.
    # It initializes object attributes.
# Example: How __init__ Works
#

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

# Creating objects
student1 = Student("Alice", 12, "7th Grade")
student2 = Student("Bob", 14, "9th Grade")

print(student1.name)  # Alice
print(student2.age)   # 14
# Key Points:
    # Self (self) → Refers to the current object.
    # The __init__() method runs automatically when an object is created.



# ----------------------------------------Class vs. Instance Variables---------------------------------
    # Class Variables → Shared among all objects.
    # Instance Variables → Unique to each object.
    # Example: Class and Instance Variables

class School:
    school_name = "Greenwood High"  # Class variable (same for all students)

    def __init__(self, student_name):
        self.student_name = student_name  # Instance variable (unique for each student)

student1 = School("Alice")
student2 = School("Bob")

print(student1.student_name)  # Alice (Instance variable)
print(student2.student_name)  # Bob (Instance variable)

print(student1.school_name)   # Greenwood High (Class variable)
print(student2.school_name)   # Greenwood High (Class variable)
# Key Points:
    # Class variables are shared among all instances.
    # Instance variables are unique to each object.



#  ---------------------------------------Instance Methods vs. Class Methods vs. Static Methods-------------------------
# -------------------------------------(A) Instance Methods → Work with object attributes

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):  # Instance method
        print(f"{self.name} is barking! ")

dog1 = Dog("Buddy", 3)
dog1.bark()  # Buddy is barking!
# Instance methods use self and work on individual objects.
#
# -------------------------------------------(B) Class Methods → Work with class variables

class Dog:
    species = "Canine"  # Class variable

    @classmethod
    def get_species(cls):  # Class method
        return cls.species

print(Dog.get_species())  # Canine
# Class methods use cls and work with class variables.


# ------------------------------------(C) Static Methods → Work independently (don’t need self or cls)

class MathOperations:
    @staticmethod
    def add(a, b):
        return a + b

print(MathOperations.add(5, 3))  # 8
# Static methods don’t access instance or class variables.


# -----------------------------------------Understanding self------------------------------
# The self keyword refers to the current object instance.
# It helps in accessing the attributes and methods of the same object.
#
# Example: The Role of self

class Person:
    def __init__(self, name):
        self.name = name  # `self.name` refers to this object's name

    def greet(self):
        print(f"Hello, my name is {self.name}!")

p1 = Person("Alice")
p2 = Person("Bob")

p1.greet()  # Hello, my name is Alice!
p2.greet()  # Hello, my name is Bob!
# Without self, Python wouldn’t know which object's name to use.


# -----------------------------------Getters and Setters (Encapsulation)--------------------------------------
# Sometimes, we want to restrict direct access to an attribute.
# We use getters (to read data) and setters (to modify data).
#
# Example: Using Getters and Setters

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private variable (cannot be accessed directly)

    def get_balance(self):  # Getter
        return self.__balance

    def set_balance(self, amount):  # Setter
        if amount > 0:
            self.__balance = amount
        else:
            print("Invalid amount!")

# Creating an account
account = BankAccount(1000)
print(account.get_balance())  # 1000

account.set_balance(5000)  # Updating balance
print(account.get_balance())  # 5000

# Private variables (__balance) can only be accessed through getters and setters.



# --------------------------------------------Destroying Objects (del)-----------------------------------
#
# When an object is no longer needed, Python automatically deletes it.
# We can also manually delete an object using del.
#
# Example: Deleting an Object

class Car:
    def __init__(self, brand):
        self.brand = brand

    def __del__(self):
        print(f"The {self.brand} car is being deleted!")

car1 = Car("Tesla")
del car1  # The Tesla car is being deleted!

# The __del__ method runs when an object is deleted.


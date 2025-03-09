# Object-Oriented Programming (OOP)
#
#
#     Think of Object-Oriented Programming (OOP) like a real-world system where things (objects) have
#     characteristics (attributes) and can perform actions (methods).
#
#     For example, a car has:
#
#     Attributes: Color, brand, speed.
#     Methods: Start, stop, accelerate.
#     OOP helps us write structured, reusable, and easy-to-maintain code.

# ------------------------------Understanding Objects & Classes (The Blueprint & The Products)---------------------
    # What is a Class?
    #     A class is like a blueprint for creating objects.
    #     Just like an architect designs a house blueprint, but the real houses are built from it.
    #
    # What is an Object?
    #     An object is an actual instance of a class, like the real houses built from the blueprint.
    #
    # Example: Creating a Car Class



class Car:  # Class (Blueprint)
    def __init__(self, brand, color, speed):
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
#     Class (Blueprint) → Car
#     Attributes (Properties of the Object) → brand, color, speed
#     Methods (Actions the Object Can Perform) → drive()
#     Objects (Real-world instances created from the blueprint) → car1 and car2

# ------------------------------------Encapsulation – Keeping Things Private---------------------------

# What is Encapsulation?
# Encapsulation means hiding important details so that no one can change them directly.

# Example: A Smartphone
#     When you use a smartphone, you can make calls, send messages, and use apps, but you cannot access the
#     internal system files directly. The operating system hides critical files so that users don’t accidentally
#     modify or delete them.
#
# Encapsulation in action:
#
#     The phone’s internal system is private, just like private variables in a class.
#     You can only access certain features through predefined methods (settings, apps), just like getter & setter
#     methods in OOP.

# Just like a piggy bank, where you cannot take out money directly—you need to use a special withdraw function.

# Example: Piggy Bank


class PiggyBank:
    def __init__(self, balance):
        self.__balance = balance  # Private variable (cannot be accessed directly)

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited ₹{amount}, New Balance: ₹{self.__balance}")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ₹{amount}, Remaining Balance: ₹{self.__balance}")
        else:
            print("Not enough money! 💰")

    def check_balance(self):
        return self.__balance  # Access through a method

# Creating a Piggy Bank
my_bank = PiggyBank(500)
my_bank.deposit(200)      # Deposited ₹200, New Balance: ₹700
my_bank.withdraw(100)     # Withdrew ₹100, Remaining Balance: ₹600
print(my_bank.check_balance())  # ₹600
print(my_bank.__balance)  #  ERROR! Cannot access private balance directly

# Why Encapsulation
    # Protects sensitive data (like the bank balance).
    # Only specific functions can modify the data, preventing accidental changes.


# ---------------------------------Inheritance – Getting Features from Parents----------------------------
# What is Inheritance?
# # Inheritance means a child class can use all the features of a parent class.

#  Example: Family Traits
#
# A child inherits traits (eye color, height, hair type) from their parents, just like how a child class
# inherits properties from a parent class.
#
# Inheritance in action:
#
# A child gets their father’s nose and mother’s smile → A child class gets features from both parents.
# A child can also develop unique characteristics → A child class can add new features or override inherited
# ones.

# # For example, a baby lion  learns to roar like its parents.

# Example: Animals

class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print(f"{self.name} is making a sound!")

# Dog is a type of Animal (inherits properties)
class Dog(Animal):
    def make_sound(self):
        print(f"{self.name} says Woof!")

# Cat is a type of Animal
class Cat(Animal):
    def make_sound(self):
        print(f"{self.name} says Meow!")

dog = Dog("Buddy")
cat = Cat("Whiskers")

dog.make_sound()  # Buddy says Woof!
cat.make_sound()  # Whiskers says Meow!


# What’s Happening Here?
#     Parent Class (Animal) → Provides basic behavior.
#     Child Classes (Dog, Cat) → Inherit and modify the behavior.
#     Method Overriding → make_sound() changes behavior in each child class.

# ----------------------------------Polymorphism – Same Action, Different Results-----------------------
# What is Polymorphism?
    # Polymorphism means the same function can work in different ways for different objects.
    #
    # For example, a TV remote’s volume button works for different TV brands but adjusts volume in each
    # one differently.
    #
# Example: Animals Making Sounds
    # Different animals make different sounds:
        #
        # A dog barks
        # A cat meows
        # A lion roars
    # Even though the action (making a sound) is the same, the outcome is different for each animal.
    #
    # Polymorphism in action:
    #
        # The same function (make_sound) behaves differently based on which animal is calling it.
        # You can call the same function name for all animals, and each will respond in its own way.


# Example: Animals Making Sounds

class Animal:
    def make_sound(self):
        print("Some generic animal sound ")

class Dog(Animal):
    def make_sound(self):
        print("Woof Woof! ")

class Cat(Animal):
    def make_sound(self):
        print("Meow Meow! ")

def play_sound(animal):
    animal.make_sound()  # Calls the correct method based on the object

dog = Dog()
cat = Cat()

play_sound(dog)  # Woof Woof!
play_sound(cat)  # Meow Meow!
# Why is Polymorphism Useful?
#     We can use the same function (play_sound) for different objects (Dog, Cat).
#     The behavior changes dynamically based on the object.



# --------------------------------------Abstraction – Hiding Complex Details----------------------------

# What is Abstraction?
    # Abstraction means hiding unnecessary details and showing only what’s important.
    #
    # For example, when you drive a car, you just turn the key—you don’t need to know how the engine works.
    #
    # Example: ATM Machine

# Example: Driving a Car
    # When you press the accelerator, the car moves faster. You don’t need to know how the engine works
    # internally—you just press the pedal.
    #
    # Abstraction in action:
    #
        # You only see the controls (steering wheel, brake, accelerator) but don’t see the complex internal mechanics.
        # The car manufacturer hides the complex engine system, just like a class hides unnecessary details.

from abc import ABC, abstractmethod

class ATM(ABC):  # Abstract Class (Blueprint)
    @abstractmethod
    def withdraw(self, amount):
        pass

class MyBankATM(ATM):  # Child Class
    def withdraw(self, amount):
        print(f"Withdrawing ₹{amount} from MyBank ATM")

class OtherBankATM(ATM):  # Another Child Class
    def withdraw(self, amount):
        print(f"Withdrawing ₹{amount} from OtherBank ATM")

atm1 = MyBankATM()
atm2 = OtherBankATM()

atm1.withdraw(1000)  # Withdrawing ₹1000 from MyBank ATM
atm2.withdraw(500)   # Withdrawing ₹500 from OtherBank ATM

# Why is Abstraction Useful?
    # Hides complexity (You don’t need to know how withdraw() works internally).
    # Forces consistency (Every ATM class must have a withdraw() method).


# Why Use OOP?
#     Reusability → Write once, use many times.
#     Security → Protect important data with encapsulation.
#     Easy Maintenance → Modify code without breaking everything.
#     Scalability → Ideal for large projects.
#
# Would you like me to explain with more real-world examples?
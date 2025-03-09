# What is Single Inheritance?
#     Single Inheritance is when one class (child) inherits from another class (parent).
#
#     The child class gets all the attributes and methods of the parent class.
#     It does not need to redefine common functionalities, making the code reusable and organized.
# Real-Life Analogy
#     Father and Son Example
#     Imagine a father who is a doctor.
#
#     His son does not need to study medicine from scratch—he inherits knowledge from his father.
#     However, the son can also develop his own skills (e.g., coding).
# In Python:
#
#     Father class → Has a method called heal() (doctor skills).
#     Son class → Inherits heal() but can also have a new method code().
# --------------------------------------Basic Syntax of Single Inheritance---------------------------

class Parent:  # Parent Class
    def parent_method(self):
        print("This is a method from the Parent class.")

class Child(Parent):  # Child Class inheriting from Parent
    def child_method(self):
        print("This is a method from the Child class.")

# Creating an object of the Child class
obj = Child()
obj.parent_method()  # Inherited from Parent class
obj.child_method()   # Child class's own method

# Explanation:
#
#     Parent is the base class (superclass).
#     Child is the derived class (subclass) that inherits from Parent.
#     The child automatically gains access to the parent_method().
#     The child can also have its own methods like child_method().


# --------------------------------------Accessing Parent Class Methods in Child Class-------------------------
#
# We can directly use parent class methods in the child class.


class Animal:
    def speak(self):
        print("Animals make sounds.")

class Dog(Animal):
    def bark(self):
        print("Dog says Woof! Woof!")

# Creating object
dog1 = Dog()
dog1.speak()  # Inherited from Animal
dog1.bark()   # Child class method

    # The Dog class inherits the speak() method from Animal.
    # bark() is specific to the Dog class.
    #

#  --------------------------------Using super() to Call Parent Class Methods-------------------------------
# Sometimes, we want to keep the parent’s method but also add extra functionality.

class Animal:
    def speak(self):
        print("Animals make sounds.")

class Dog(Animal):
    def speak(self):
        super().speak()  # Calls Parent's speak()
        print("Dog says Woof! Woof!")

dog1 = Dog()
dog1.speak()

# Explanation
#     super().speak() calls speak() from the Animal (parent) class.
#     Then, the Dog class adds its own behavior.
# Output:
#     Animals make sounds.
#     Dog says Woof! Woof!
#
#
# The child class extends functionality without removing the parent’s method.


# -------------------------------------Parent Class with __init__() Constructor-------------------------------
#
# If the parent class has an __init__ constructor, the child does not automatically inherit it.
# You must call it explicitly using super().


class Person:
    def __init__(self, name):
        self.name = name  # Parent attribute
        print(f"Person Constructor: {name}")

class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name)  # Calling Parent Constructor
        self.grade = grade
        print(f"Student Constructor: {name} is in {grade} grade.")

# Creating an object of Student
s1 = Student("Alice", "10th Grade")

# Output:
#     Person Constructor: Alice
#     Student Constructor: Alice is in 10th Grade.
# Explanation
#     Parent class (Person) has an __init__() constructor.
#     Child class (Student) overrides it but calls super().__init__(name) to keep parent behavior.



# --------------------------------------Private Variables in Inheritance-----------------------------------
# If a parent class has private attributes (__varname), they cannot be directly accessed in the child class.
#

class Parent:
    def __init__(self):
        self.__secret = "This is a private variable"

class Child(Parent):
    def show_secret(self):
        print(self.__secret)  #  ERROR: Cannot access private variable

c = Child()
c.show_secret()  # AttributeError


# Solution: Use getter methods to access private variables.

class Parent:
    def __init__(self):
        self.__secret = "This is a private variable"

    def get_secret(self):  # Getter method
        return self.__secret

class Child(Parent):
    pass

c = Child()
print(c.get_secret())  #  Works fine



# ---------------------------Checking the issubclass() and isinstance()--------------------------------
# Python provides two built-in functions for checking inheritance.


class Animal:
    pass

class Dog(Animal):
    pass

d = Dog()

print(issubclass(Dog, Animal))  # True (Dog inherits from Animal)
print(isinstance(d, Dog))       # True (d is an instance of Dog)
print(isinstance(d, Animal))    # True (d is an instance of Animal because Dog inherits from Animal)
print(isinstance(d, object))    # True (Everything in Python is an object)
# issubclass(A, B) → Checks if A is a subclass of B.
# isinstance(obj, Class) → Checks if obj is an instance of Class or its parent.




# What is Hierarchical Inheritance?
    # Hierarchical inheritance occurs when multiple child classes inherit from a single parent class.
    # It allows different child classes to reuse common functionality from the parent while having their own unique features.
    #
    # Hierarchy:
    #                      Parent
    #                    /    |   \
    #             Child1  Child2   Child3


# All child classes share the same parent but function independently.
#
    # Real-Life Analogy
    # Imagine a vehicle manufacturing company:
    #
# Vehicle (Parent class) → Defines common features like engine, wheels, and fuel().
# Car (Child class) → Inherits fuel() but adds air_conditioning().
# Bike (Child class) → Inherits fuel() but adds helmet_requirement().
# Truck (Child class) → Inherits fuel() but adds cargo_capacity().
# Example:
                # Class 	:   Common Feature (Inherited)	:   Unique Feature
                # Car 		:   fuel()		                :   air_conditioning()
                # Bike 		:   fuel()	                	:   helmet_requirement()
                # Truck 	:   fuel()	               	:   cargo_capacity()
# Each child class has unique methods but shares common ones from the parent.
#
# ----------------------------------------Basic Syntax of Hierarchical Inheritance--------------------------


class Parent:
    def common_method(self):
        print("This method is inherited by all child classes.")

class Child1(Parent):
    def child1_method(self):
        print("This is a method from Child1.")

class Child2(Parent):
    def child2_method(self):
        print("This is a method from Child2.")

class Child3(Parent):
    def child3_method(self):
        print("This is a method from Child3.")

# Creating objects of child classes
c1 = Child1()
c2 = Child2()
c3 = Child3()

c1.common_method()  # Inherited from Parent
c1.child1_method()  # Child1's own method

c2.common_method()  # Inherited from Parent
c2.child2_method()  # Child2's own method

c3.common_method()  # Inherited from Parent
c3.child3_method()  # Child3's own method


#
# Each child class gets common_method() from Parent but also has its own methods.
# Objects of child classes can only access their own methods and the inherited ones.
#
#
#
#
# -------------------------------------------------Hierarchical Inheritance with Constructor (__init__())----------------------------------------------
# Each child class can call the parent constructor using super().


class Parent:
    def __init__(self):
        print("Parent Constructor")

class Child1(Parent):
    def __init__(self):
        super().__init__()  # Calls Parent constructor
        print("Child1 Constructor")

class Child2(Parent):
    def __init__(self):
        super().__init__()  # Calls Parent constructor
        print("Child2 Constructor")

# Creating objects
c1 = Child1()
c2 = Child2()


# Output:

#         Parent Constructor
#         Child1 Constructor
#         Parent Constructor
#         Child2 Constructor
# Each child class calls the parent constructor before executing its own.



# ---------------------------------Overriding Parent Methods in Child Classes------------------------------------
# Each child class can modify the inherited methods if needed.


class Parent:
    def show(self):
        print("This is Parent's method.")

class Child1(Parent):
    def show(self):  # Overriding Parent's method
        print("This is Child1's version of the method.")

class Child2(Parent):
    def show(self):  # Overriding Parent's method
        print("This is Child2's version of the method.")

# Creating objects
c1 = Child1()
c2 = Child2()

c1.show()  # Calls Child1's overridden method
c2.show()  # Calls Child2's overridden method



# Each child provides its own version of the inherited method.
# The parent method is replaced (overridden) in the child class.

# -----------------------------Checking Inheritance with issubclass() and isinstance()-------------------------------
# We can check if a class is inherited from another using issubclass().


print(issubclass(Child1, Parent))  #  True
print(issubclass(Child2, Parent))  #  True
print(issubclass(Child1, Child2))  #  False (They are siblings, not parents)


# We can check if an object belongs to a class using isinstance().

c1 = Child1()
print(isinstance(c1, Child1))  #  True
print(isinstance(c1, Parent))  #  True (Because Child1 inherits from Parent)
print(isinstance(c1, Child2))  #  False (Child1 and Child2 are separate)


# Each child class is an instance of the parent class but not its siblings.
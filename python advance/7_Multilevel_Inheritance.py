# Multilevel Inheritance in Python
    # What is Multilevel Inheritance?
        # Multilevel inheritance is when a class inherits from another class, which itself is inheriting from another class.
        # It forms a chain of inheritance, where a child class becomes a parent class for another child class.
        #
    #  ------------------------------Hierarchy:
        # Grandparent → Parent → Child
        #  The child class inherits from the parent class, and the parent inherits from the grandparent class.
        #
    # ️ ----------------------------------------Real-Life Analogy--------------------------------
        # Imagine a family business:
        #
        # The Grandfather was a farmer .
        # The Father inherited farming skills but started a dairy farm .
        # The Son inherited both farming and dairy skills but started selling products online .
        #  Family Business Example
        # Grandfather class → Has farming() method.
        # Father class → Inherits farming() and adds dairy_farming().
        # Son class → Inherits both and adds sell_online().
        # The Son class automatically gets the skills of both his father and grandfather.
    #
    #-----------------------------------Basic Syntax of Multilevel Inheritance-------------------------------

class Grandparent:
    def grandparent_method(self):
        print("This is a method from the Grandparent class.")

class Parent(Grandparent):
    def parent_method(self):
        print("This is a method from the Parent class.")

class Child(Parent):
    def child_method(self):
        print("This is a method from the Child class.")

# Creating an object of Child class
obj = Child()
obj.grandparent_method()  # Inherited from Grandparent
obj.parent_method()  # Inherited from Parent
obj.child_method()  # Child class's own method


# The Child class inherits from Parent, and Parent inherits from Grandparent.
# The Child class can access methods from all ancestor classes.
#
# ------------------------------------Accessing Grandparent and Parent Methods in Child Class
# Since the Child class is the last in the hierarchy, it can access all methods from both Grandparent and
# Parent.

class Animal:
    def breathe(self):
        print("Animals breathe.")

class Mammal(Animal):
    def feed_milk(self):
        print("Mammals feed their young with milk.")

class Dog(Mammal):
    def bark(self):
        print("Dog says Woof! Woof!")

# Creating an object of Dog
dog1 = Dog()
dog1.breathe()  # Inherited from Animal
dog1.feed_milk()  # Inherited from Mammal
dog1.bark()  # Dog's own method


# Dog inherits the breathe() method from Animal.
# Dog inherits the feed_milk() method from Mammal.
# Dog has its own method bark().

# ----------------------------------------Overriding Parent Class Methods in Child Class---------------------------------
# If the Parent and Grandparent have the same method name, the Child overrides it.


class Grandparent:
    def show(self):
        print("This is Grandparent's method.")

class Parent(Grandparent):
    def show(self):
        print("This is Parent's method.")

class Child(Parent):
    def show(self):
        print("This is Child's method.")

# Creating an object of Child
obj = Child()
obj.show()  # Calls Child's method

# Even though Grandparent and Parent have a show() method, the Child's method is executed.
# Method Overriding allows the Child to modify inherited methods.

#
# ----------------------------------------Using super() in Multilevel Inheritance----------------------------
# The super() function calls the immediate parent class method.
#


class Grandparent:
    def show(self):
        print("Grandparent's method")

class Parent(Grandparent):
    def show(self):
        super().show()  # Calls Grandparent's show()
        print("Parent's method")

class Child(Parent):
    def show(self):
        super().show()  # Calls Parent's show()
        print("Child's method")

# Creating an object of Child
obj = Child()
obj.show()

# Output:
#     Grandparent's method
#     Parent's method
#     Child's method

# Explanation
    # super().show() in Child calls Parent's method.
    # super().show() in Parent calls Grandparent's method.
    # This maintains the method execution hierarchy.



# -----------------------------Constructor (__init__()) in Multilevel Inheritance-----------------------------
# If each class has a constructor (__init__()), we must use super() to call all parent constructors.

class Grandparent:
    def __init__(self):
        print("Grandparent Constructor")

class Parent(Grandparent):
    def __init__(self):
        super().__init__()  # Calls Grandparent's constructor
        print("Parent Constructor")

class Child(Parent):
    def __init__(self):
        super().__init__()  # Calls Parent's constructor
        print("Child Constructor")

# Creating an object of Child
obj = Child()


# Output:
#     Grandparent Constructor
#     Parent Constructor
#     Child Constructor
#




#----------------------------- Checking Inheritance with issubclass() and isinstance()-------------------------
# We can check the inheritance hierarchy using issubclass() and isinstance().


class Grandparent:
    pass

class Parent(Grandparent):
    pass

class Child(Parent):
    pass

print(issubclass(Child, Parent))  # True
print(issubclass(Child, Grandparent))  #  True
print(issubclass(Parent, Child))  #  False

obj = Child()
print(isinstance(obj, Child))  #  True
print(isinstance(obj, Parent))  #  True (Because Child inherits from Parent)
print(isinstance(obj, Grandparent))  #  True (Because of Multilevel Inheritance)

# issubclass(A, B) → Checks if A is a subclass of B.
# isinstance(obj, Class) → Checks if obj is an instance of Class or its ancestors.
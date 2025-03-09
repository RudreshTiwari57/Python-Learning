# Multiple Inheritance in Python
    # What is Multiple Inheritance?
        # Multiple inheritance is when a child class inherits from more than one parent class.
        #
        #  The child class gets attributes and methods from multiple parent classes.
        #  It allows a class to have multiple functionalities without redefining them.
        #
        # ️ Real-Life Analogy
        # Imagine a child who has:
        #
        # A father who is a doctor
        # A mother who is a musician
        # The child inherits medical knowledge from the father and musical skills from the mother.
        # But the child can also develop their own unique skills (e.g., coding).
        #
        # ️ Real-life Example in Python
        # Father class → Has heal() method (Doctor skills).
        # Mother class → Has play_music() method (Musician skills).
        # Child class → Inherits both but can have its own methods.
        #  Basic Syntax of Multiple Inheritance

class Parent1:
    def method1(self):
        print("This is method from Parent1")

class Parent2:
    def method2(self):
        print("This is method from Parent2")

class Child(Parent1, Parent2):  # Inheriting from both Parent1 and Parent2
    def child_method(self):
        print("This is method from Child class")

# Creating an object of Child
obj = Child()
obj.method1()  # Inherited from Parent1
obj.method2()  # Inherited from Parent2
obj.child_method()  # Child's own method


# Explanation:
#     Parent1 and Parent2 are two separate parent classes.
#     Child class inherits from both parents.
#     The child class can use methods from both parents.
# This allows code reusability and modularity.


# ----------------------------------------Advantages of Multiple Inheritance-------------------------------
#
#
#         Code Reusability → The child class gets features from multiple parents.
#         More Functionality → A class can have combined features from different sources.
#         Less Redundancy → No need to write the same code multiple times.
#
#
#
# -------------------------------------Challenges in Multiple Inheritance------------------------------------
#
#
#     Diamond Problem (Ambiguity in Method Resolution Order – MRO)
#     Conflicts in Method Names (If both parents have a method with the same name)
#     Increased Complexity (If inheritance gets too deep, debugging is hard)
#
# ------------------------------------Accessing Methods from Multiple Parents-----------------------------
#
#
# Since the child class inherits from multiple parents, it can directly call their methods.

class Father:
    def doctor(self):
        print("Father is a doctor.")

class Mother:
    def musician(self):
        print("Mother is a musician.")

class Child(Father, Mother):
    def coder(self):
        print("Child is a coder.")

# Creating an object of Child
child1 = Child()
child1.doctor()  # Inherited from Father
child1.musician()  # Inherited from Mother
child1.coder()  # Child's own method


# The Child class inherits skills from both parents.


# ---------------------------------------------Using super() in Multiple Inheritance---------------------------
#     The super() function is used to call the parent class’s method.
#     In multiple inheritance, super() only calls the first parent listed.


class Parent1:
    def show(self):
        print("Parent1's method")

class Parent2:
    def show(self):
        print("Parent2's method")

class Child(Parent1, Parent2):
    def show(self):
        super().show()  # Calls Parent1's show()
        print("Child's method")

obj = Child()
obj.show()
# Output:
#         Parent1's method
#         Child's method
# Explanation
#         super().show() calls Parent1’s method.
#         Then, the Child class executes its own method.
# To call Parent2's method explicitly, use:
#         Parent2.show(self)


#  ------------------------------------------Diamond Problem (Ambiguity in Method Resolution Order - MRO)
# The diamond problem occurs when a class inherits from two classes that share a common ancestor.
#
# Example: The Diamond Structure
#
#        A
#       / \
#      B   C
#       \ /
#        D

class A:
    def show(self):
        print("A's method")

class B(A):
    def show(self):
        print("B's method")

class C(A):
    def show(self):
        print("C's method")

class D(B, C):  # D inherits from B and C, both inherit from A
    pass

obj = D()
obj.show()  # Which method will be called?

# Python resolves the diamond problem using MRO (C3 Linearization).
# MRO follows the order: D → B → C → A

# MRO Order for Class D

print(D.mro())
# Output:
# [<class 'D'>, <class 'B'>, <class 'C'>, <class 'A'>, <class 'object'>]
# Python resolves ambiguity by following MRO rules!


# -------------------------------------------------------Checking Inheritance with issubclass() and isinstance()
# We can check if a class is inherited from another using issubclass().


class A:
    pass

class B(A):
    pass

print(issubclass(B, A))  #  True (B inherits from A)
print(issubclass(A, B))  # False (A does not inherit from B)
# Similarly, isinstance() checks if an object belongs to a class.


obj = B()
print(isinstance(obj, B))  #  True
print(isinstance(obj, A))  #  True (Because B inherits from A)
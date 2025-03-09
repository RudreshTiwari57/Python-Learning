#  Python Inheritance – The Deepest Dive Ever!
    # ---------------------------What is Inheritance?
        # Inheritance is a fundamental OOP concept where a class (child) inherits attributes and methods
        #  from another class (parent).
        #
    # Real-Life Example
        # Imagine a father who has blue eyes and a son who also has blue eyes. The son inherits the eye color
        # from his father.
        # Similarly, in Python, a child class can reuse the properties and behaviors of its parent class.

# ---------------------------Why Use Inheritance?
#     Code Reusability → Avoid writing the same code multiple times.
#     Maintainability → Changes in the parent class automatically apply to the child class.
#     Extensibility → The child class can add new features.


#  -----------------------------------------Basic Syntax of Inheritance--------------------------------
# A child class inherits from a parent class like this:


class Parent:
    # Parent class
    pass

class Child(Parent):
    # Child class inherits from Parent
    pass

# -----------------------------------Types of Inheritance in Python------------------------------------
#
# Python supports 5 types of inheritance:
#
# Inheritance Type	    :               Description
#     1. Single Inheritance	:           One child inherits from one parent.
#     2. Multiple Inheritance :	        One child inherits from multiple parents.
#     3. Multilevel Inheritance	:       A child inherits from a parent, and that parent is also a child of another class.
#     4. Hierarchical Inheritance	:   One parent class has multiple child classes.
#     5. Hybrid Inheritance	:           A mix of two or more types of inheritance.



# ------------------------------------Method Resolution Order (MRO)-------------------------------------
# When a class inherits from multiple parents, Python follows MRO (Method Resolution Order) using the C3 linearization algorithm.
#
# Example: MRO in Multiple Inheritance


class A:
    def show(self):
        print("Class A")

class B(A):
    def show(self):
        print("Class B")

class C(A):
    def show(self):
        print("Class C")

class D(B, C):  # Multiple Inheritance
    pass

obj = D()
obj.show()  # Class B (Because Python follows MRO)
print(D.mro())  # [D, B, C, A, object]


# How Python Resolves Methods in MRO:
#     Python checks in the order of inheritance (D → B → C → A).
#     If a method is not found in D, it looks in B, then C, then A.

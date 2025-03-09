# What is Hybrid Inheritance?
#         Hybrid inheritance is a combination of multiple types of inheritance in a single program.
#         It mixes single, multiple, multilevel, and hierarchical inheritance to create a more complex hierarchy.
#
#         Hybrid inheritance helps reuse code efficiently while maintaining flexibility.
#         It can lead to method resolution order (MRO) complexities, which Python resolves using C3 Linearization (MRO algorithm).
#
# Real-Life Analogy
#     Imagine a university system:
#
#         Professor (Base class) → Teaches students.
#         Researcher (Another Base class) → Conducts research.
#         Assistant Professor (Derived from Professor) → Teaches and assists.
#         Research Professor (Derived from Researcher) → Focuses on research.
#         Senior Professor (Derived from both Assistant and Research Professors) → Does both teaching and research.
#         Hierarchy:
#                               Person
#                              /      \
#                         Professor  Researcher
#                             |         |
#                         Assistant  Research Professor
#                              \       /
#                            Senior Professor


# The Senior Professor inherits from both Assistant Professor and Research Professor,
# Each inherits from different base classes.


# -----------------------------Basic Syntax of Hybrid Inheritance----------------------------


class A:
    def method_A(self):
        print("Method from Class A")

class B(A):  # Single Inheritance
    def method_B(self):
        print("Method from Class B")

class C(A):  # Another Single Inheritance
    def method_C(self):
        print("Method from Class C")

class D(B, C):  # Multiple Inheritance
    def method_D(self):
        print("Method from Class D")

# Creating an object of D
obj = D()
obj.method_A()  # Inherited from A
obj.method_B()  # Inherited from B
obj.method_C()  # Inherited from C
obj.method_D()  # Own method of D


# D inherits from both B and C,
# B and C both inherit from A.

# Method Resolution Order (MRO)
print(D.mro())

# Output:


# [<class 'D'>, <class 'B'>, <class 'C'>, <class 'A'>, <class 'object'>]
# Python resolves inheritance order using C3 Linearization (MRO).


# ---------------------------------------------Hybrid Inheritance with super()---------------------------
# To correctly call parent methods, we must use super().


class A:
    def show(self):
        print("Class A")

class B(A):
    def show(self):
        super().show()
        print("Class B")

class C(A):
    def show(self):
        super().show()
        print("Class C")

class D(B, C):  # Inheriting from both B and C
    def show(self):
        super().show()
        print("Class D")

# Creating an object of D
obj = D()
obj.show()


# Output (Using MRO Order):
#         Class A
#         Class C
#         Class B
#         Class D
#
# Explanation:
#
# super() ensures each parent is called only once.
# Python follows C3 Linearization (MRO).


# ----------------------------------------------Hybrid Inheritance with Constructors (__init__())
# If multiple classes have __init__(), we need super() to avoid
# calling the same constructor multiple times.

class A:
    def __init__(self):
        print("Constructor of A")

class B(A):
    def __init__(self):
        super().__init__()
        print("Constructor of B")

class C(A):
    def __init__(self):
        super().__init__()
        print("Constructor of C")

class D(B, C):  # Hybrid Inheritance
    def __init__(self):
        super().__init__()
        print("Constructor of D")

# Creating an object of D
obj = D()

# Output:
#         Constructor of A
#         Constructor of C
#         Constructor of B
#         Constructor of D

# Python ensures that A's constructor is called only once using MRO.

# -------------------------Checking Inheritance with issubclass() and isinstance()----------------------------------
# Use issubclass() to check if a class inherits from another.

print(issubclass(D, B))  #  True
print(issubclass(D, C))  #  True
print(issubclass(D, A))  #  True
print(issubclass(B, C))  #  False


# Use isinstance() to check if an object belongs to a class.

obj = D()
print(isinstance(obj, D))  #  True
print(isinstance(obj, A))  #  True (Because of Hybrid Inheritance)
print(isinstance(obj, C))  #  True (Because C is a Parent of D)
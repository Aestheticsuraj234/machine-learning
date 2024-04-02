class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        print(sum(self.marks) / len(self.marks))

    @staticmethod
    def hello():
        print("Hello")


s1 = Student("John", [45, 67, 89, 90, 78])

s1.get_avg()
s1.hello()

class Car:
    def __init__(self):
        self.acc = False # attribute
        self.brk = False 
        self.clutch = False
    def start(self):
        self.clutch = True
        self.acc = True
        self.brk = False
        print("Car is starting")
# important
# Abstraction: Hiding the implementation details and showing only the functionality to the user.
# Encapsulation: Binding the data and the functions that manipulate the data into a single unit.
# Inheritance: The mechanism of deriving a new class from an existing class.
# Polymorphism: The ability to take various forms.
# Class: A blueprint for creating objects.
# Object: An instance of a class.
# Method: A function that is defined inside a class.
# Attribute: A variable that is defined inside a class.
# Self: A reference to the current instance of the class.
# Constructor: A special method that is called when an object is created.


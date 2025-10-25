# self keyword is mandatory for calling variable names into methods
# instance and class variable has whole different purpose
# constructor name should be _init_
# new keyword is not required when we create an object


class Calculator:
    num = 100  # class variables

    # default constructor
    def __init__(self, a, b):
        self.firstNumber = a  # this all instance variables
        self.secondNUmber = b  # this all instance variables. Instance variables will keep on changing but class variable will not change (num=100)
        print("I'm called automatically when the object is created")

    def getData(self):
        print("I am now executed as method in class")

    def Summation(self):
       # return self.firstNumber + self.secondNUmber + self.num
        return self.firstNumber + self.secondNUmber + Calculator.num


# Create object of the class
obj = Calculator(2, 3)  # Syntax to create object in python
print(obj.Summation())



# Create object of the class
obj1 = Calculator(4, 5)  # Syntax to create object in python
obj1.getData()
print(obj1.Summation())

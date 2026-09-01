#self keyword is mandatory for calling variable names into methods
# instance and class variables have different purposes
# constructor name should be __init__
# new keyword is not required when you create an object


class Calculator:
    num = 100  #class variables

    # default constructor
    def __init__(self, a, b):
        self.firstNumber = a  #instance variables
        self.secondNumber = b
        print("I'm called automatically when object is created")

    def getData(self):
        print("test")

    #method
    def Summation(self):
        return self.firstNumber + self.secondNumber + Calculator.num


obj = Calculator(50, 2)  # syntax to create objects
obj.getData()
print(obj.Summation())

obj = Calculator(4, 5) #syntax to create objects
obj.getData()
print(obj.Summation())



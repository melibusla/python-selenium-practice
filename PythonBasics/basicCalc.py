class BasicCalculator:
    def __init__(self, a, b):
        self.firstNumber = a
        self.secondNumber = b

    def addition(self):
        return self.firstNumber + self.secondNumber

    def subtraction(self):
        return self.firstNumber - self.secondNumber

    def multiplication(self):
        return self.firstNumber * self.secondNumber

    def division(self):
        if self.secondNumber != 0:
            return self.firstNumber / self.secondNumber
        else:
            return "Division by zero is not allowed."


obj = BasicCalculator(10, 5)
add = obj.addition()
sub = obj.subtraction()
mult = obj.multiplication()
div = obj.division()

print("Addition: ", add)
print("Subtraction: ", sub)
print("Multiplication: ", mult)
print("Division: ", div)
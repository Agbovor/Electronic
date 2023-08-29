class Calculator:
    def __init__(self, numA, numB) :
        self.numA = numA
        self.numB= numB
        # self.add = lambda numA, numB

    def addition(self):
        return self.numA + self.numB
    
    def subtraction(self):
        return self.numA - self.numB
    
    def multiplication(self):
        return self.numA * self.numB
    
    def division(self):
        if self.numB == 0:
            return("Invalid parameter /n value canot be zero ")

        return self.numA / self.numB

AlexsCalc = Calculator(6,56)
print(AlexsCalc.addition())
print(AlexsCalc.subtraction())
print(AlexsCalc.division())
print(AlexsCalc.multiplication())
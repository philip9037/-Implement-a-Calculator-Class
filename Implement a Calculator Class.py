class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def add(self):
        return self.num1 + self.num2
    
    def subtract(self):
        return self.num2 - self.num1
    
    def multiply(self):
        return self.num1 * self.num2
    
    def divide(self):
        if self.num1 == 0:
            return "Cannot divide by zero"
        else:
            return self.num2 / self.num1
calc = Calculator(5, 2)

print(calc.add())        
print(calc.subtract())   
print(calc.multiply())   
print(calc.divide())     


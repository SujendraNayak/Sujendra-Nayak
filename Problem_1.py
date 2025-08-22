class Calculator:
    def __init__(self, a, b, operation):
        self.a = a
        self.b = b
        self.operation = operation.lower()

    def calculate(self):
        if self.operation == "add":
            return self.a + self.b
        elif self.operation == "sub":
            return self.a - self.b
        elif self.operation == "mul":
            return self.a * self.b
        elif self.operation == "div":
            if self.b != 0:
                return self.a / self.b
            else:
                return "Error: Division by zero!"
        else:
            return "Invalid operation!"


# Taking input from user
a = float(input("Enter first number: ")) #In Python, there is no separate double type like in C, C++ or Java.
b = float(input("Enter second number: "))
operation = input("Enter operation (add, sub, mul, div): ")

calc = Calculator(a, b, operation)
print("Result:", calc.calculate())

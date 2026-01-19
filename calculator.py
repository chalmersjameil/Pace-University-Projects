def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is undefined."
    return a / b

def calculator():
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            operand = input("Enter an operand (+, -, *, /): ")
            num2 = float(input("Enter the second number: "))
            
            if operand == '+':
                result = add(num1, num2)
            elif operand == '-':
                result = subtract(num1, num2)
            elif operand == '*':
                result = multiply(num1, num2)
            elif operand == '/':
                result = divide(num1, num2)
            else:
                print("Invalid operand. Please use +, -, *, or /.")
                continue

            print("Result:", result)
            break

        except ValueError:
            print("Invalid input. Please enter numbers for calculations.")

def main():
    calculator()

if __name__ == '__main__':
    main()

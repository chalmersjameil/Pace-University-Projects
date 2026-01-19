#CALCULATIOR
import math

def display_menu():
    print("Welcome to the Advanced Calculator Program!")
    print("Please select an option:")
    print("1. Basic Arithmetic Operations")
    print("2. Advanced Functions (Exponents, Square Roots, Trigonometry)")
    print("3. Solve an Algebraic Equation")
    print("4. Percentage Calculations")
    print("5. Exit")

def basic_arithmetic():
    print("\nBasic Arithmetic Operations:")
    num1 = float(input("Enter the first number: "))
    operator = input("Enter an operator (+, -, *, /): ")
    num2 = float(input("Enter the second number: "))
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            return "Error: Division by zero is not allowed."
    else:
        return "Error: Invalid operator."
    return f"Result: {result}"

def advanced_functions():
    print("\nAdvanced Functions:")
    print("1. Exponentiation")
    print("2. Square Root")
    print("3. Trigonometric Calculations")
    choice = input("Choose an option (1/2/3): ")
    if choice == "1":
        base = float(input("Enter the base: "))
        exponent = float(input("Enter the exponent: "))
        return f"Result: {base ** exponent}"
    elif choice == "2":
        num = float(input("Enter the number: "))
        if num >= 0:
            return f"Result: {math.sqrt(num)}"
        else:
            return "Error: Square root of a negative number is not allowed."
    elif choice == "3":
        angle = float(input("Enter the angle in degrees: "))
        radians = math.radians(angle)
        return (f"Sine: {math.sin(radians)}\n"
                f"Cosine: {math.cos(radians)}\n"
                f"Tangent: {math.tan(radians)}")
    else:
        return "Error: Invalid choice."

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")
        if choice == "1":
            print(basic_arithmetic())
        elif choice == "2":
            print(advanced_functions())
        elif choice == "3":
            print("Algebraic equation solving will be added soon!")
        elif choice == "4":
            print("Percentage calculations will be added soon!")
        elif choice == "5":
            print("Thank you for using the Advanced Calculator Program. Goodbye!")
            break
        else:
            print("Error: Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

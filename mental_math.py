import random

def get_random_numbers():
    return random.randint(1, 10), random.randint(1, 10)

def test_addition(num1, num2):
    answer = int(input(f"What is {num1} + {num2}? "))
    return answer == num1 + num2

def test_subtraction(num1, num2):
    if num1 < num2:
        num1, num2 = num2, num1
    answer = int(input(f"What is {num1} - {num2}? "))
    return answer == num1 - num2

def test_multiplication(num1, num2):
    answer = int(input(f"What is {num1} * {num2}? "))
    return answer == num1 * num2

def test_division(num1, num2):
    while num1 % num2 != 0:
        num1, num2 = get_random_numbers()
    answer = int(input(f"What is {num1} / {num2}? "))
    return answer == num1 // num2

def mental_math_quiz():
    score = 0
    for _ in range(5):
        num1, num2 = get_random_numbers()
        operation = random.choice(['+', '-', '*', '/'])
        if operation == '+':
            score += test_addition(num1, num2)
        elif operation == '-':
            score += test_subtraction(num1, num2)
        elif operation == '*':
            score += test_multiplication(num1, num2)
        elif operation == '/':
            score += test_division(num1, num2)
    print("Your score:", score)

def main():
    mental_math_quiz()

if __name__ == '__main__':
    main()

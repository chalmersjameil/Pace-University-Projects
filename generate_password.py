import random
import string

def generate_password(num_chars):
    if num_chars < 10:
        print("Warning: Passwords should be at least 10 characters long.")
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all_characters) for _ in range(num_chars))
    return password

def main():
    try:
        num_chars = int(input("Enter the length of the password: "))
        print("Generated password:", generate_password(num_chars))
    except ValueError:
        print("Invalid input. Please enter an integer.")

if __name__ == '__main__':
    main()

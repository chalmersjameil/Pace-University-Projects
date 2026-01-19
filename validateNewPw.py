import re

def is_valid_password(password):
    if len(password) < 10:
        return False

    # Check for each category: special character, uppercase, lowercase, number
    categories = [
        bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password)),  # Special characters
        bool(re.search(r'[A-Z]', password)),                   # Uppercase letters
        bool(re.search(r'[a-z]', password)),                   # Lowercase letters
        bool(re.search(r'[0-9]', password))                    # Numbers
    ]
    # Ensure at least 3 out of 4 categories are present
    return sum(categories) >= 3

def main():
    while True:
        password = input("Enter a password: ")
        if is_valid_password(password):
            print("Password is valid!")
            break
        else:
            print("Password must be at least 10 characters long and include at least 3 of the following: special characters, uppercase letters, lowercase letters, numbers.")

if __name__ == '__main__':
    main()

import random

def generate_random_number():
    return random.randint(1, 100)

def get_user_guess(remaining_attempts):
    try:
        guess = int(input(f"You have {remaining_attempts} guesses left. Enter your guess: "))
        return guess
    except ValueError:
        print("Invalid input. Please enter a number.")
        return None

def check_guess(user_guess, target):
    if user_guess < target:
        print("Too low!")
        return False
    elif user_guess > target:
        print("Too high!")
        return False
    else:
        print("Correct!")
        return True

def play_game():
    target = generate_random_number()
    attempts = 10
    while attempts > 0:
        guess = get_user_guess(attempts)
        if guess is None:
            continue
        if check_guess(guess, target):
            break
        attempts -= 1
    if attempts == 0:
        print(f"Game over! The number was {target}.")

if __name__ == '__main__':
    play_game()

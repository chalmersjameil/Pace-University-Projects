import random

def generate_random_number():
    """Generates and returns a random target number between 1 and 100."""
    return random.randint(1, 100)

def get_user_guess(attempt):
    """Prompts the user to enter a guess and validates that it’s an integer."""
    while True:
        guess = input(f"Attempt {attempt}: Enter your guess: ")
        if guess.isdigit():
            return int(guess)
        print("Please enter a valid number.")

def check_guess(guess, target_number):
    """Checks if the guess is correct, too low, or too high."""
    if guess == target_number:
        return "correct"
    elif guess < target_number:
        return "low"
    else:
        return "high"


def test_generate_random_number():
    num = generate_random_number()
    assert isinstance(num, int), "generate_random_number should return an integer."
    assert 1 <= num <= 100, "generate_random_number should return a value between 1 and 100."

    random.seed(0)  
    num = generate_random_number()
    assert 1 <= num <= 100, "generate_random_number should return a value between 1 and 100 even with set seed."
    random.seed(99)
    num = generate_random_number()
    assert 1 <= num <= 100, "generate_random_number should return a value between 1 and 100 with different seeds."

    random.seed(0) 
    num = generate_random_number()
    assert isinstance(num, int), "generate_random_number should always return an integer even with corner cases."


def test_check_guess():
    
    assert check_guess(50, 50) == "correct", "check_guess should return 'correct' for a correct guess."
    assert check_guess(25, 50) == "low", "check_guess should return 'low' if the guess is lower than the target."
    assert check_guess(75, 50) == "high", "check_guess should return 'high' if the guess is higher than the target."

   
    assert check_guess(1, 100) == "low", "check_guess should return 'low' if the guess is 1 and the target is 100."
    assert check_guess(100, 1) == "high", "check_guess should return 'high' if the guess is 100 and the target is 1."

    
    assert check_guess(50, 51) == "low", "check_guess should handle cases close to the target and return 'low' if just under target."


if __name__ == '__main__':
    test_generate_random_number()
    test_check_guess()
    print("All tests executed (some may not pass based on conditions).")

   
    def play_game():
        """Controls the game flow, calling other functions and managing guesses."""
        target_number = generate_random_number()
        max_guesses = 7
        print("Welcome to the Guess the Number Game!")
        print(f"I'm thinking of a number between 1 and 100. You have {max_guesses} tries to guess it.")

        for attempt in range(1, max_guesses + 1):
            guess = get_user_guess(attempt)
            result = check_guess(guess, target_number)

            if result == "correct":
                print("Congratulations! You guessed the number correctly!")
                break
            elif result == "low":
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")

            guesses_left = max_guesses - attempt
            if guesses_left > 0:
                print(f"You have {guesses_left} guesses left.")
            else:
                print(f"Sorry, you've used all your guesses. The number was {target_number}.")

    play_game()


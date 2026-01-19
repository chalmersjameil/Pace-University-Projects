import random

def main():
    target_number = random.randint(1, 100)
    max_guesses = 7
    print("Welcome to the Guess the Number Game!")
    print(f"I'm thinking of a number between 1 and 100. You have {max_guesses} tries to guess it.")

    for attempt in range(max_guesses):
        guess = input(f"Attempt {attempt + 1}: Enter your guess: ")

        if not guess.isdigit():
            print("Please enter a valid number.")
            continue

        guess = int(guess)

        if guess == target_number:
            print("Congratulations! You guessed the number correctly!")
            break
        elif guess < target_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")
    else:
        print(f"Sorry, you've used all your guesses. The number was {target_number}.")

if __name__ == '__main__':
    main()

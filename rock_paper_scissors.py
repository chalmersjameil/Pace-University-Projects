import random

def rock_paper_scissors(player, computer):
    if player == computer:
        return 0
    elif (player == 'rock' and computer == 'scissors') or \
         (player == 'scissors' and computer == 'paper') or \
         (player == 'paper' and computer == 'rock'):
        return 1
    else:
        return 2

def get_player_choice():
    choice = input("Enter rock, paper, or scissors: ").lower()
    if choice in ['rock', 'paper', 'scissors']:
        return choice
    else:
        print("Invalid choice. Please try again.")
        return None

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def play():
    player_choice = get_player_choice()
    if player_choice is None:
        return
    computer_choice = get_computer_choice()
    print(f"Computer chose: {computer_choice}")
    result = rock_paper_scissors(player_choice, computer_choice)
    if result == 0:
        print("It's a tie!")
    elif result == 1:
        print("You win!")
    else:
        print("Computer wins!")

# Start the game
if __name__ == '__main__':
    play()

def main():
    user_input = input("Enter a string: ")
    words = user_input.split()

    print(f"First: {user_input[0]}, Middle: {user_input[len(user_input) // 2]}, Last: {user_input[-1]}")
    print(f"Reversed words: {' '.join(reversed(words))}")
    print(f"Reversed letters: {user_input[::-1]}")
    print(f"Every other character: {user_input[1::2]}")
    print(f"First letter of each word: {' '.join(word[0] for word in words)}")

    
    return

if __name__ == '__main__':
    main()
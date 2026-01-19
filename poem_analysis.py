def main():
    path = "poems/I_built_my_hut.txt"
    with open(path, "r") as f:
        poem = f.read()

    num_chars = len(poem)
    num_words = len(poem.split())
    num_lines = len(poem.split("\n"))
    avg_word_len = sum(len(word) for word in poem.split()) / num_words
    avg_line_len = sum(len(line) for line in poem.split("\n")) / num_lines
    avg_words_per_line = num_words / num_lines

    print(f"Characters: {num_chars}")
    print(f"Words: {num_words}")
    print(f"Lines: {num_lines}")
    print(f"Average word length: {avg_word_len}")
    print(f"Average line length: {avg_line_len}")
    print(f"Average words per line: {avg_words_per_line}")

    return

if __name__ == '__main__':
    main()

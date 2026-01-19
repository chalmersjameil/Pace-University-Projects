def main():
    files = ['file1.txt', 'file2.txt', 'file3.txt']

    char_counts = [len(open(f"data/{file}", 'r').read()) for file in files]
    line_counts = [open(f"data/{file}", 'r').read().count('\n') + 1 for file in files]
    word_counts = [len(open(f"data/{file}", 'r').read().split()) for file in files]

    print(f"File with most characters: {files[char_counts.index(max(char_counts))]} ({max(char_counts)} characters)")
    print(f"File with most lines: {files[line_counts.index(max(line_counts))]} ({max(line_counts)} lines)")
    print(f"File with most words: {files[word_counts.index(max(word_counts))]} ({max(word_counts)} words)")

if __name__ == '__main__':
    main()

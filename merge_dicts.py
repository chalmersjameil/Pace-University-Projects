def main():
    glossary = {}

    # Function to read a glossary from a file and merge it into the main dictionary
    def read_glossary(filename):
        with open(f"data/{filename}", 'r') as file:
            for line in file:
                word, definition = line.strip().split(':', 1)
                word = word.strip()
                definition = definition.strip()

                # Combine definitions if the word already exists
                glossary[word] = glossary.get(word, '') + (f" / {definition}" if word in glossary else definition)

    # Read both glossary files
    read_glossary('ch10glossary.txt')
    read_glossary('ch11glossary.txt')

    # Write the combined glossary to 'combined_glossary.txt'
    with open('data/combined_glossary.txt', 'w') as combined_file:
        for word, definition in sorted(glossary.items()):
            combined_file.write(f"{word}: {definition}\n")

    print("Combined glossary has been created in 'combined_glossary.txt'.")

if __name__ == '__main__':
    main()

def main():
    pronouns = ['he', 'she', 'they', 'it', 'him', 'her', 'them', 'his', 'hers', 'their', 'its']
    pronoun_counts = {p: 0 for p in pronouns}

    with open('data/dunequotes.txt', 'r', encoding="utf8") as file:
        content = file.read().lower()

    for pronoun in pronouns:
        pronoun_counts[pronoun] = content.count(f' {pronoun} ')

    total = sum(pronoun_counts.values())
    most_frequent = max(pronoun_counts, key=pronoun_counts.get)

    print(f"Total pronouns: {total}")
    print(f"Most used pronoun: '{most_frequent}' ({pronoun_counts[most_frequent]} times)")

if __name__ == '__main__':
    main()

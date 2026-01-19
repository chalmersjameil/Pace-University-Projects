class Puzzle:
    def __init__(self, title, pieces, company=None):
        """
        Initialize a Puzzle instance.
        :param title: Title of the puzzle
        :param pieces: Number of pieces in the puzzle
        :param company: (Optional) Company that made the puzzle
        """
        self.title = title
        self.pieces = pieces
        self.company = company

    def sort_priority(self):
        """
        Returns the number of pieces for sorting.
        """
        return self.pieces

    def __str__(self):
        """
        Returns a string representation of the Puzzle.
        """
        return self.title


def main():
    """Main function to create, sort, and display puzzles."""
    puzzle_details = [
        ('The Greatest Bookshop', 1000, 'Ravensburger'),
        ('China Cupboard', 1000, 'Ravensburger'),
        ('The New Yorker', 1000),
        ('Van Dael', 1000, 'Clementoni'),
        ('The New Yorker', 500),
        ('State Birds & Flowers', 1000, 'White Mountain'),
        ('The World of Horses', 1000, 'White Mountain'),
        ('Monopoly', 550),
        ('The Christmas Village', 1000, 'Ravensburger'),
        ('The Global Puzzle', 2000, 'A Broader View'),
        ('Friends in Autumn', 1000, 'White Mountain'),
        ('Old Bookstore', 1000, 'White Mountain'),
        ('Winder Wonderland', 1000, 'White Mountain'),
        ('Summer Cottage by Fred Swan', 1000, 'White Mountain'),
    ]

    puzzles = []

    for details in puzzle_details:
        title, pieces, *company = details
        company = company[0] if company else None
        puzzles.append(Puzzle(title, pieces, company))

    sorted_puzzles = sorted(puzzles, key=lambda p: p.sort_priority())

    print("Sorted puzzles by number of pieces:")
    for puzzle in sorted_puzzles:
        company_info = f" by {puzzle.company}" if puzzle.company else ""
        print(f"{puzzle} ({puzzle.pieces} pieces{company_info})")


if __name__ == "__main__":
    main()

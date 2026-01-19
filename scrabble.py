import random

class LetterTile:
    def __init__(self, letter: str, points: int):
        self.letter = letter
        self.points = points

    def get_letter(self):
        return self.letter

    def get_points(self):
        return self.points

    def __str__(self):
        return self.letter

class BlankTile(LetterTile):
    def __init__(self):
        super().__init__("_", 0)
        self.assigned_letter = None

    def assign_letter(self, letter: str):
        self.assigned_letter = letter

    def get_letter(self):
        return self.assigned_letter if self.assigned_letter else self.letter

def create_letters():
    letter_distribution = {
        "E": (12, 1), "A": (9, 1), "I": (9, 1), "O": (8, 1), "N": (6, 1), "R": (6, 1),
        "T": (6, 1), "L": (4, 1), "S": (4, 1), "U": (4, 1), "D": (4, 2), "G": (3, 2),
        "B": (2, 3), "C": (2, 3), "M": (2, 3), "P": (2, 3), "F": (2, 4), "H": (2, 4),
        "V": (2, 4), "W": (2, 4), "Y": (2, 4), "K": (1, 5), "J": (1, 8), "X": (1, 8),
        "Q": (1, 10), "Z": (1, 10)
    }
    tiles = [BlankTile() for _ in range(2)]
    for letter, (count, points) in letter_distribution.items():
        tiles.extend(LetterTile(letter, points) for _ in range(count))
    return tiles

def choose_tiles(tiles, count=7):
    return random.sample(tiles, count)

def display_tiles(player, tiles):
    """Display the tiles and their points for a given player."""
    print(f"{player}'s Tiles:")
    for tile in tiles:
        letter = tile.get_letter()
        points = tile.get_points()
        print(f"Letter: {letter}, Points: {points}")
    print()

def main():
    # Step 1: Create all tiles
    tiles = create_letters()

    # Step 2: Players pick their tiles
    player1_tiles = choose_tiles(tiles)
    player2_tiles = choose_tiles(tiles)

    # Step 3: Display tiles for both players
    display_tiles("Player 1", player1_tiles)
    display_tiles("Player 2", player2_tiles)


if __name__ == "__main__":
    main()

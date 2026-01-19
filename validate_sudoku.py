def is_valid_sudoku(grid):
    for row in grid:
        if sorted(row) != list(range(1, 10)):
            return False

    for col in range(9):
        column = [grid[row][col] for row in range(9)]
        if sorted(column) != list(range(1, 10)):
            return False

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            block = []
            for row in range(i, i + 3):
                for col in range(j, j + 3):
                    block.append(grid[row][col])
            if sorted(block) != list(range(1, 10)):
                return False

    return True

def main():
    sudokus = [
        [
            [2,6,1,4,7,3,8,9,5],
            [5,3,4,6,8,9,1,7,2],
            [7,9,8,5,1,2,6,4,3],
            [1,8,3,9,4,6,2,5,7],
            [6,7,2,8,3,5,4,1,9],
            [4,5,9,1,2,7,3,6,8],
            [9,2,5,3,6,1,7,8,4],
            [3,4,6,7,9,8,5,2,1],
            [8,1,7,2,5,4,9,3,6]
        ], 
        [
            [4,9,5,7,8,3,2,1,6],
            [7,8,3,2,1,6,9,4,5],
            [2,6,1,9,4,5,7,8,3],
            [3,4,6,1,5,9,8,7,2],
            [1,7,9,8,3,2,6,5,7],  
            [8,5,2,4,6,7,1,3,9],
            [5,2,7,3,9,1,4,6,8],
            [6,1,4,5,2,8,3,9,7],
            [9,3,8,6,7,4,5,2,1]
        ], 
        [
            [4,9,5,7,8,3,2,1,6],
            [7,8,3,2,1,6,9,4,5],
            [2,6,1,9,4,5,7,8,3],
            [3,4,6,1,5,9,8,7,2],
            [1,7,9,8,3,2,6,5,4],
            [8,5,2,4,6,7,1,3,9],
            [5,2,7,3,9,1,4,6,8],
            [6,1,4,5,2,8,3,9,7],
            [9,3,8,6,7,4,5,2,1]
        ], 
        [
            [4,9,5,7,8,3,2,1,6],
            [7,8,3,2,1,6,9,4,5],
            [2,6,1,9,4,5,7,8,3],
            [3,4,6,1,5,9,8,7,2],
            [6,1,4,5,2,8,3,9,7],
            [1,7,9,8,3,2,6,5,4],
            [8,5,2,4,6,7,1,3,9],
            [5,2,7,3,9,1,4,6,8],
            [9,3,8,6,7,4,5,2,1]  
        ]
    ]
    
    for idx, sudoku in enumerate(sudokus, start=1):
        if is_valid_sudoku(sudoku):
            print(f"Sudoku {idx} is valid.")
        else:
            print(f"Sudoku {idx} is invalid.")

if __name__ == '__main__':
    main()

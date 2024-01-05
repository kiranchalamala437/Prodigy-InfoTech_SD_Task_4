def print_grid(grid):
    for row in grid:
        print(" ".join(map(str, row)))

def is_valid_move(grid, row, col, num):
    # Check if the number is not in the current row and column
    if num in grid[row] or num in [grid[i][col] for i in range(9)]:
        return False

    # Check if the number is not in the 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if grid[start_row + i][start_col + j] == num:
                return False

    return True

def find_empty_location(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return i, j
    return None, None

def solve_sudoku(grid):
    row, col = find_empty_location(grid)

    if row is None:
        return True  # Puzzle solved

    for num in range(1, 10):
        if is_valid_move(grid, row, col, num):
            grid[row][col] = num

            if solve_sudoku(grid):
                return True  # Puzzle solved recursively

            grid[row][col] = 0  # Backtrack if the solution is not found

    return False  # No solution found

# Example unsolved Sudoku grid (0 represents empty cells)
unsolved_grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

print("Unsolved Sudoku:")
print_grid(unsolved_grid)

if solve_sudoku(unsolved_grid):
    print("\nSolved Sudoku:")
    print_grid(unsolved_grid)
else:
    print("\nNo solution exists.")
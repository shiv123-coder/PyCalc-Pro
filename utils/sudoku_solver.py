# Sudoku Solver using Backtracking (Recursion)
# Demonstrates recursive problem solving from Rubicon Training


def solve_sudoku(board):
    """
    Solve a 9x9 Sudoku puzzle using backtracking (recursion).
    board: 9x9 list of lists, 0 represents empty cells.
    Returns: True if solved (board is modified in-place), False if no solution.
    """
    empty = find_empty(board)
    if not empty:
        return True  # Puzzle solved!
    
    row, col = empty
    
    for num in range(1, 10):
        if is_valid_move(board, num, row, col):
            board[row][col] = num
            
            if solve_sudoku(board):  # Recursive call
                return True
            
            board[row][col] = 0  # Backtrack
    
    return False


def find_empty(board):
    """Find the next empty cell (value = 0)."""
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None


def is_valid_move(board, num, row, col):
    """Check if placing 'num' at (row, col) is valid."""
    # Check row
    if num in board[row]:
        return False
    
    # Check column
    for i in range(9):
        if board[i][col] == num:
            return False
    
    # Check 3x3 box
    box_row = (row // 3) * 3
    box_col = (col // 3) * 3
    for i in range(box_row, box_row + 3):
        for j in range(box_col, box_col + 3):
            if board[i][j] == num:
                return False
    
    return True


def is_valid_board(board):
    """Check if the current board state is valid (no conflicts)."""
    for i in range(9):
        for j in range(9):
            if board[i][j] != 0:
                num = board[i][j]
                board[i][j] = 0  # Temporarily remove
                if not is_valid_move(board, num, i, j):
                    board[i][j] = num  # Restore
                    return False, (i, j)
                board[i][j] = num  # Restore
    return True, None


def get_sample_puzzles():
    """Return sample Sudoku puzzles with difficulty levels."""
    return {
        "Easy": [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9],
        ],
        "Medium": [
            [0, 0, 0, 6, 0, 0, 4, 0, 0],
            [7, 0, 0, 0, 0, 3, 6, 0, 0],
            [0, 0, 0, 0, 9, 1, 0, 8, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 5, 0, 1, 8, 0, 0, 0, 3],
            [0, 0, 0, 3, 0, 6, 0, 4, 5],
            [0, 4, 0, 2, 0, 0, 0, 6, 0],
            [9, 0, 3, 0, 0, 0, 0, 0, 0],
            [0, 2, 0, 0, 0, 0, 1, 0, 0],
        ],
        "Hard": [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 3, 0, 8, 5],
            [0, 0, 1, 0, 2, 0, 0, 0, 0],
            [0, 0, 0, 5, 0, 7, 0, 0, 0],
            [0, 0, 4, 0, 0, 0, 1, 0, 0],
            [0, 9, 0, 0, 0, 0, 0, 0, 0],
            [5, 0, 0, 0, 0, 0, 0, 7, 3],
            [0, 0, 2, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 4, 0, 0, 0, 9],
        ],
    }


def board_to_string(board):
    """Convert board to a formatted string for display."""
    lines = []
    for i, row in enumerate(board):
        if i % 3 == 0 and i != 0:
            lines.append("─" * 31)
        cells = []
        for j, val in enumerate(row):
            if j % 3 == 0 and j != 0:
                cells.append("│")
            cells.append(f" {val if val != 0 else '·'} ")
        lines.append("".join(cells))
    return "\n".join(lines)

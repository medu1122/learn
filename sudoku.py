def print_sudoku(board):
    print()
    for row in board:
        print(" ".join(str(num) for num in row))

def check(board, row, col, num):
    for i in range(9):
        if board[row][i] == num:
            return False
    for i in range(9):
        if board[i][col] == num:
            return False
    box_row = 3 * (row // 3)
    box_col = 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[box_row + i][box_col + j] == num:
                return False
    return True

def giai(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if check(board, row, col, num):
                        board[row][col] = num
                        if giai(board):
                            return True
                        board[row][col] = 0
                return False
    return True

board = []
for _ in range(9):
    row = list(map(int, input().split()))  # nhap tung dong
    board.append(row)

print("Bảng Sudoku ban đầu:")
print_sudoku(board)

if giai(board):
    print("\nBảng Sudoku sau khi giải:")
    print_sudoku(board)
else:
    print("\nKhông tìm thấy lời giải!")

    

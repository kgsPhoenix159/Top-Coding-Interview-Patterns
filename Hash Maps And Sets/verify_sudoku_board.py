def verify_sudoku_board(board):
    row_sets = [set() for _ in range(9)]
    column_sets = [set() for _ in range(9)]
    subgrid_sets = [[set() for _ in range(3)] for _ in range(3)]

    for row in range(9):
        for column in range(9):
            num = board[row][column]

            if num == 0:
                continue

            if num in row_sets[row]:
                return False
            if num in column_sets[column]:
                return False
            if num in subgrid_sets[row // 3][column // 3]:
                return False
            
            row_sets[row].add(num)
            column_sets[column].add(num)
            subgrid_sets[row // 3][column // 3].add(num)
    
    return True

board = [[int(num) for num in input().strip().split()] for _ in range(9)]
# board = [[3,0,6,0,5,8,4,0,0],[5,2,0,0,0,0,0,0,0],[0,8,7,0,0,0,0,3,1],[1,0,2,5,0,0,3,2,0],[9,0,0,8,6,3,0,0,5],[0,5,0,0,9,0,6,0,0],[0,1,0,0,0,0,0,7,4],[0,3,0,0,0,8,2,5,0],[0,0,5,2,0,6,0,0,0]]
is_board_valid = verify_sudoku_board(board)
print(is_board_valid)
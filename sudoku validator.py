def valid_solution(board):
    #Validating 3x3 Squares
    for i in range(0,7,3):
        for j in range(0,7,3):
            square3x3 = [digit for three_digits in [item[j:j+3] for item in board[i:i+3]] for digit in three_digits]
            if not set([1,2,3,4,5,6,7,8,9]).issubset(set(square3x3)) : return False
    #Validating lines and columns
    for i in range(9):
        if not set([1,2,3,4,5,6,7,8,9]).issubset(set(board[i])) : return False
        if not set([1,2,3,4,5,6,7,8,9]).issubset(set([item[i] for item in board])) : return False

    return True

sudoku = [
  [5, 3, 4, 6, 7, 8, 9, 1, 2],
  [6, 7, 2, 1, 9, 5, 3, 4, 8],
  [1, 9, 8, 3, 4, 2, 5, 6, 7],
  [8, 5, 9, 7, 6, 1, 4, 2, 3],
  [4, 2, 6, 8, 5, 3, 7, 9, 1],
  [7, 1, 3, 9, 2, 4, 8, 5, 6],
  [9, 6, 1, 5, 3, 7, 2, 8, 4],
  [2, 8, 7, 4, 1, 9, 6, 3, 5],
  [3, 4, 5, 2, 8, 6, 1, 7, 9]
]


print(valid_solution(sudoku))

input()

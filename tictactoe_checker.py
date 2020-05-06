# check_row(sym, single_row) return True if all items in single_row are
#   equal to sym. Otherwise, it returns False.
def check_row(sym, single_row):
    i = 0
    answer = True
    while i < len(single_row):
        if sym != single_row[i]:
            answer = False
            break
        i = i + 1
    return answer


# check_rows(sym, grid) returns True if all items in any row of grid is
#   equal to sym. Otherwise, it returns False.
def check_rows(sym, grid):
    i = 0
    answer = False
    while i < len(grid):
        if check_row(sym, grid[i]):
            answer = True
            break
        i = i + 1
    return answer


# check_columns(sym, grid) returns True if all items in any column of grid is
#   equal to sym. Otherwise, it returns False.
def check_columns(sym, grid):
    col_num = 0
    answer = False
    while col_num < len(grid):
        if sym == grid[0][col_num] and sym == grid[1][col_num] \
                and sym == grid[2][col_num]:
            answer = True
            break
        col_num = col_num + 1
    return answer


# check_diagonals(sym, grid) returns True if all items in any diagonal of grid is
#   equal to sym. Otherwise, it returns False.
def check_diagonals(sym, grid):
    answer = False
    if sym == grid[1][1]:
        if (sym == grid[0][0] and sym == grid[2][2]) \
                or (sym == grid[0][2] and sym == grid[2][0]):
            answer = True
    return answer


# check_win(sym, grid) returns True if the sym has won the game of tic tac toe.
#   Otherwise, it returns False.
# Time: O(n) where n is len(grid)
def check_win(sym, grid):
    if check_rows(sym, grid) or check_columns(sym, grid) or check_diagonals(sym, grid):
        return True
    else:
        return False

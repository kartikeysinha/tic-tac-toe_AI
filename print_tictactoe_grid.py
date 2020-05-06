# print_grid(grid) prints the grid as a tic tac toe figure.
# time: O(n) where n is len(grid)
def print_grid(grid):
    for i in range(0, 3):
        for j in range(0, 3):
            if grid[i][j] == 0:
                print("  ", end=" ")
            else:
                print(" " + grid[i][j], end=" ")

            if j != 2:
                print("|", end="")
            else:
                print("")
        if i != 2:
            print("---|---|---")

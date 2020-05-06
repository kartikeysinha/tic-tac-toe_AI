import tictactoe_checker as tc
import print_tictactoe_grid as pg
import tictactoe_moves as move

grid = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]

print("Welcome to the classic tic-tac-toe game!")
print("You will be playing against the computer!")

while True:
    level = input("Which level would you like to play? " +
                  "EASY  (e)    HARD  (h)   IMPOSSIBLE  (i): ")
    if (level != "e") and (level != 'h') and (level != 'i'):
        print("Wrong Symbol! Try again. Be mindful of the case.")
    else:
        break

while True:
    user_sym = input("What would you like to be? Type o for circle and x for cross: ")
    if (user_sym != "x") and (user_sym != 'o'):
        print("Wrong Symbol! Try again. Be mindful of the case.")
    else:
        break

if user_sym == 'x':
    comp_sym = 'o'
else:
    comp_sym = 'x'

while True:
    cur_move = input("Who goes first? Type u for User and c for Comp: ")
    if cur_move != 'u' and cur_move != 'c':
        print("Wrong entry! Try again. Be mindful of the case.")
    else:
        break


pg.print_grid(grid)

free_indices = [0, 1, 2, 3, 4, 5, 6, 7, 8]

while True:
    if move.grid_full(free_indices):
        print("Good Game! It is a draw!")
        break
    else:
        if cur_move == 'u':
            move.next_move(level, comp_sym, user_sym, grid, cur_move, free_indices)
            pg.print_grid(grid)
            if tc.check_win(user_sym, grid):
                print("You won! Congratulations!")
                break
            cur_move = 'c'
        else:
            move.next_move(level, comp_sym, user_sym, grid, cur_move, free_indices)
            pg.print_grid(grid)
            if tc.check_win(comp_sym, grid):
                print("You lost! Better luck next time!")
                break
            cur_move = 'u'


import random
import tictactoe_checker as tc
import copy


def check_valid_spot(index, list_indices):
    if index in list_indices and index < 9:
        return True
    else:
        return False


def user_move(user_sym, grid, list_indices):
    index = input("Where do you want to move? Type a number between 1 to 9." +
                  " 1, 2, 3 = first row; " +
                  "4, 5, 6 = second row; " +
                  "7, 8, 9 = third row: ")
    index = int(index) - 1
    if not check_valid_spot(index, list_indices):
        print("Not a valid spot! Try again.")
        user_move(user_sym, grid, list_indices)
    else:
        row = index // 3
        column = index % 3
        grid[row][column] = user_sym
        list_indices.remove(index)


def comp_move(level, comp_sym, user_sym, grid, list_indices):
    print("Computer Move:")

    if level == 'e':
        pos = random.randint(0, 8) % len(list_indices)
        index = list_indices[pos]
        row = index // 3
        column = index % 3
        grid[row][column] = comp_sym
        list_indices.remove(index)

    elif level == 'h':
        state = 1
        for i in range(0, 3):
            if state:
                for j in range(0, 3):
                    board_copy = [copy.copy(element) for element in grid]
                    index = (3 * i) + j
                    if index in list_indices:
                        board_copy[i][j] = comp_sym
                        if tc.check_win(comp_sym, board_copy):
                            grid[i][j] = comp_sym
                            list_indices.remove(index)
                            state = 0
                            break

        if state:
            for i in range(0, 3):
                if state:
                    for j in range(0, 3):
                        board_copy = [copy.copy(element) for element in grid]
                        index = (3 * i) + j
                        if index in list_indices:
                            board_copy[i][j] = user_sym
                            if tc.check_win(user_sym, board_copy):
                                grid[i][j] = comp_sym
                                list_indices.remove(index)
                                state = 0
                                break

        if state:
            comp_move('e', comp_sym, user_sym, grid, list_indices)

    else:
        state = 1
        list_corners = [0, 2, 6, 8]
        list_edges = [1, 3, 5, 7]
        centre = 4

        for i in range(0, 3):
            if state:
                for j in range(0, 3):
                    board_copy = [copy.copy(element) for element in grid]
                    index = (3 * i) + j
                    if index in list_indices:
                        board_copy[i][j] = comp_sym
                        if tc.check_win(comp_sym, board_copy):
                            grid[i][j] = comp_sym
                            list_indices.remove(index)
                            state = 0
                            break

            if state:
                for i in range(0, 3):
                    if state:
                        for j in range(0, 3):
                            board_copy = [copy.copy(element) for element in grid]
                            index = (3 * i) + j
                            if index in list_indices:
                                board_copy[i][j] = user_sym
                                if tc.check_win(user_sym, board_copy):
                                    grid[i][j] = comp_sym
                                    list_indices.remove(index)
                                    state = 0
                                    break

            if state:
                for i in list_corners:
                    row = i // 3
                    column = i % 3
                    if grid[row][column] == 0:
                        grid[row][column] = comp_sym
                        list_indices.remove(i)
                        state = 0
                        break

            if state:
                if grid[1][1] == 0:
                    grid[1][1] = comp_sym
                    list_indices.remove(centre)
                    state = 0

            if state:
                for i in list_edges:
                    row = i // 3
                    column = i % 3
                    if grid[row][column] == 0:
                        grid[row][column] = comp_sym
                        list_indices.remove(i)
                        state = 0
                        break


def grid_full(list_indices):
    answer = False
    if len(list_indices) == 0:
        answer = True
    return answer


def next_move(level, comp_sym, user_sym, grid, move, list_indices):
        if move == 'u':
            user_move(user_sym, grid, list_indices)
        else:
            comp_move(level, comp_sym, user_sym, grid, list_indices)

# amount of cells
board_size = 3

board = [1,2,3,4,5,6,7,8,9]

def draw_board():
    """Print game board"""
    print('_' * 4 * board_size)
    for i in range(board_size):
        print((' ' * 3 + '|') * 3)
        print('', board[i*3], '|', board[1 + i * 3], '|', board[2 + i * 3], '|')
        print((' ' * 3 + '|') * 3)
    pass

def game_step(index, char):
    """action"""
    if (index > 9 or index < 1 or board[index-1] in ('X', 'O')):
        return False

    board[index-1] = char
    return True
def check_win():
    win = False

    win_combination = (
        (0, 1, 2), (3, 4, 5), (6, 7, 8), # gorizontal lines
        (0, 3, 6), (1, 4, 7), (2, 5, 8), # vertical lines
        (0, 4, 8), (2, 4 ,6) # diagonal lines
    )

    for pos in win_combination:
        if(board[pos[0]] == board[pos[1]] and board[pos[1]] == board[pos[2]]):
            win = board[pos[0]]

    return win

def start_game():
    current_player = 'X'
    # number of step
    step = 1
    draw_board()

    while (step < 10) and (check_win() == False):
        index = input(f'Player {current_player} moves. Print number of squere (0 - exit()): ')

        if (index == '0'):
            break

        if (game_step(int(index), current_player)):
            print("Successful move")

            if (current_player == 'X'):
                current_player = 'O'
            else:
                current_player = 'X'

            draw_board()
            # + step
            step+=1
        else:
            print("Error")

    if (step == 10):
        print('Friend wins!')
    else:
        print(f'Wined: {check_win()}')


print('Welcome to XO Rastaman Prod.')
start_game()
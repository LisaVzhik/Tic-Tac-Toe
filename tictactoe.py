def print_board(str_board):
    print('---------')
    print(f'| {str_board[0]} {str_board[1]} {str_board[2]} |')
    print(f'| {str_board[3]} {str_board[4]} {str_board[5]} |')
    print(f'| {str_board[6]} {str_board[7]} {str_board[8]} |')
    print('---------')


def matrix_to_str(matrix):
    return ''.join(matrix[0] + matrix[1] + matrix[2])


def check_enter(x, y):
    if not x.isdigit() or not y.isdigit():
        print('You should enter numbers!')
    elif not 0 < int(x) < 4 or not 0 < int(y) < 4:
        print('Coordinates should be from 1 to 3!')
    elif matrix[int(x) - 1][int(y) - 1] != ' ':
        print('This cell is occupied! Choose another one!')
    else:
        return True


def check_win(str_board):
    check = [str_board[0:3], str_board[3:6], str_board[6:9], str_board[0:7:3],
             str_board[1:8:3], str_board[2:9:3], str_board[0:9:4], str_board[2:7:2]]
    return True if 'XXX' in check or 'OOO' in check else False


if __name__ == '__main__':
    matrix = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    str_board = matrix_to_str(matrix)
    print_board(str_board)
    count = 2

    while ' ' in str_board:
        x, y = input().split()
        if check_enter(x, y):
            matrix[int(x) - 1][int(y) - 1] = 'X' if count % 2 == 0 else 'O'
            str_board = matrix_to_str(matrix)
            print_board(str_board)
            if check_win(str_board):
                print('X wins' if count % 2 == 0 else 'O wins')
                break
            else:
                count += 1
                continue
    else:
        print('Draw')

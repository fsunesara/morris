import sys

def generate_add(board):
    L = []
    for i in range(len(board)):
        if board[i] == 'x':
            b = list(board)
            b[i] = 'W'
            b = ''.join(b)
            if close_mill(i, b):
                generate_remove(b, L)
            else:
                L.append(b)
    return L

def generate_remove(board, L):
    for i in range(len(board)):
        if board[i] == 'B':
            if not close_mill(i, board):
                b = list(board)
                b[i] = 'x'
                b = ''.join(b)
                L.append(b)
            
def close_mill(j, board):
    c = board[j]

    if j == 0: #a0
        return (board[2] == c and board[4] == c) or (board[6] == c and board[18] == c)
    elif j == 1: #g0
        return (board[3] == c and board[5] == c) or (board[11] == c and board[20] == c)
    elif j == 2: #b1
        return (board[0] == c and board[4] == c) or (board[7] == c and board[15] == c)
    elif j == 3: #f1
        return (board[1] == c and board[5] == c) or (board[10] == c and board[17] == c)
    elif j == 4: #c2
        return (board[0] == c and board[2] == c) or (board[8] == c and board[12] == c)
    elif j == 5: #e2
        return (board[1] == c and board[3] == c) or (board[9] == c and board[14] == c)
    elif j == 6: #a3
        return (board[0] == c and board[18] == c) or (board[7] == c and board[8] == c)
    elif j == 7: #b3
        return (board[6] == c and board[8] == c) or (board[2] == c and board[15] == c)
    elif j == 8: #c3
        return (board[4] == c and board[12] == c) or (board[6] == c and board[7] == c)
    elif j == 9: #e3
        return (board[5] == c and board[14] == c) or (board[10] == c and board[11] == c)
    elif j == 10: #f3
        return (board[3] == c and board[17] == c) or (board[9] == c and board[11] == c)
    elif j == 11: #g3
        return (board[1] == c and board[20] == c) or (board[9] == c and board[10] == c)
    elif j == 12: #c4
        return (board[4] == c and board[8] == c) or (board[13] == c and board[14] == c) or (board[15] == c and board[18] == c)
    elif j == 13: #d4
        return (board[16] == c and board[19] == c) or (board[12] == c and board[14] == c)
    elif j == 14: #e4
        return (board[5] == c and board[9] == c) or (board[12] == c and board[13] == c) or (board[17] == c and board[20] == c)
    elif j == 15: #b5
        return (board[2] == c and board[7] == c) or (board[16] == c and board[17] == c) or (board[12] == c and board[18] == c)
    elif j == 16: #d5
        return (board[13] == c and board[19] == c) or (board[15] == c and board[17] == c)
    elif j == 17: #f5
        return (board[3] == c and board[10] == c) or (board[15] == c and board[16] == c) or (board[14] == c and board[20] == c)
    elif j == 18: #a6
        return (board[0] == c and board[6] == c) or (board[19] == c and board[20] == c) or (board[12] == c and board[15] == c)
    elif j == 19:
        return (board[13] == c and board[16] == c) or (board[18] == c and board[20] == c)
    elif j == 20:
        return (board[1] == c and board[11] == c) or (board[18] == c and board[19] == c) or (board[14] == c and board[17] == c)
    else:
        return False

def static_estimation(board):
    return board.count('W') - board.count('B')

def black_move_generator(board):
    tempb = swap_colors(board)
    L = generate_add(tempb)

    for b in L:
        b = swap_colors(b)
        
    return L

def swap_colors(board):
    temp = list(board)
    
    for i in range(0, len(temp)):
        if temp[i] == 'B':
            temp[i] = 'W'
        elif temp[i] == 'W':
            temp[i] = 'B'

    return ''.join(temp)

def min_max(board, depth, alpha, beta):
    global minimax_estimate, num_positions_evaluated, board_position, global_depth
    if depth == 0:
        num_positions_evaluated += 1
        return static_estimation(board)
    else:
        v = 1000000
        children = black_move_generator(board)
        for y in children:
            prev = v
            v = min(v, max_min(y, depth-1, alpha, beta))
            if prev > v:
                board_position = y
                minimax_estimate = v
            elif v <= alpha:
                return v
            else:
                beta = min(v, beta)
        return v

def max_min(board, depth, alpha, beta):
    global minimax_estimate, num_positions_evaluated, board_position, global_depth
    if depth == 0:
        num_positions_evaluated += 1
        return static_estimation(board)
    else:
        v = -1000000
        if depth < global_depth:
            board = swap_colors(board)
        children = generate_add(board)
        for y in children:
            prev = v
            v = max(v, min_max(y, depth-1, alpha, beta))
            if prev < v:
                board_position = y
                minimax_estimate = v
            elif v >= beta:
                return v
            else:
                alpha = max(v, alpha)
        return v

input_board = ''
swapped = False

with open(sys.argv[1]) as ib:
    input_board = ib.readline()

board_position = input_board
num_positions_evaluated = 0
minimax_estimate = 0
output_file_name = sys.argv[2]
global_depth = int(sys.argv[3])

minimax_estimate = max_min(input_board, global_depth, -1000000, 1000000)
if global_depth % 2 == 0 and global_depth > 0:
    board_position = swap_colors(board_position)
with open(output_file_name, 'w') as of:
    of.write(board_position)
print('Board Position:', board_position)
print('Positions Evaluated by static estimation:', num_positions_evaluated)
print('MINIMAX estimate:', minimax_estimate)

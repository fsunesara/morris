import sys

def generate_moves_midgame_endgame(board):
    if board.count('W') == 3:
        return generate_hopping(board)
    else:
        return generate_move(board)

def generate_hopping(board):
    L = []
    for i in range(0, len(board)):
        if board[i] == 'W':
            for j in range(0, len(board)):
                if board[j] == 'x':
                    b = list(board)
                    b[i] = 'x'
                    b[j] = 'W'
                    b = ''.join(b)
                    if close_mill(j, b):
                        generate_remove(b, L)
                    else:
                        L.append(b)
    return L

def generate_move(board):
    L = []
    for i in range(0, len(board)):
        if board[i] == 'W':
            n = neighbors(i)
            if n is None:
                print('woo')
            for j in n:
                if board[j] == 'x':
                    b = list(board)
                    b[i] = 'x'
                    b[j] = 'W'
                    b = ''.join(b)
                    if close_mill(j, b):
                        generate_remove(b, L)
                    else:
                        L.append(b)
    return L

#TODO FINISH NEIGHBORS
def neighbors(j):
    if j == 0:
        return [1, 2, 6]
    elif j == 1:
        return [0, 3, 11]
    elif j == 2:
        return [0, 3, 4, 7]
    elif j == 3:
        return [1, 2, 6, 10, 11]
    elif j == 4:
        return [2, 5, 8]
    elif j == 5:
        return [3, 4, 8]
    elif j == 6:
        return [0, 7, 18]
    elif j == 7:
        return [2, 6, 8, 15]
    elif j == 8:
        return [4, 7, 12]
    elif j == 9:
        return [5, 10, 14]
    elif j == 10:
        return [3, 9, 11, 17]
    elif j == 11:
        return [1, 10, 20]
    elif j == 12:
        return [8, 13, 15]
    elif j == 13:
        return [12, 14, 16]
    elif j == 14:
        return [9, 13, 17]
    elif j == 15:
        return [7, 12, 16, 18]
    elif j == 16:
        return [13, 15, 17, 19]
    elif j == 17:
        return [10, 12, 16, 20]
    elif j == 18:
        return [6, 15, 19]
    elif j == 19:
        return [16, 18, 20]
    elif j == 20:
        return [11, 16, 19]
    else:
        return []

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
    elif j == 19: #d6
        return (board[13] == c and board[16] == c) or (board[18] == c and board[20] == c)
    elif j == 20: #g6
        return (board[1] == c and board[11] == c) or (board[18] == c and board[19] == c) or (board[14] == c and board[17] == c)
    else:
        return False

def black_move_generator(board):
    tempb = swap_colors(board)
    L = generate_moves_midgame_endgame(tempb)

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

def static_estimation(board):
    L = black_move_generator(board)
    if board.count('B') <= 2:
        return 10000
    elif board.count('W') <= 2:
        return -10000
    elif len(L) == 0:
        return 10000
    else:
        return 1000*(board.count('W') - board.count('B') - len(L))

def min_max(board, depth, alpha, beta):
    global minimax_estimate, num_positions_evaluated, board_position
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
    global minimax_estimate, num_positions_evaluated, board_position
    if depth == 0:
        num_positions_evaluated += 1
        return static_estimation(board)
    else:
        v = -1000000
        if depth < global_depth:
            board = swap_colors(board)
        children = generate_moves_midgame_endgame(board)
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

with open(sys.argv[1]) as ib:
    input_board = ib.readline()

board_position = input_board
output_file_name = sys.argv[2]
global_depth = int(sys.argv[3])

minimax_estimate = 0
num_positions_evaluated = 0

minimax_estimate = max_min(input_board, global_depth, -1000000, 1000000)
if global_depth % 2 == 0 and global_depth > 0:
    board_position = swap_colors(board_position)
print('Board Position:', board_position)
print('Positions Evaluated by static estimation:', num_positions_evaluated)
print('MINIMAX estimate:', minimax_estimate)
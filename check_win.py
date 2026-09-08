import numpy as np

def check_win(board,row,col):
    cur_color = board[row][col]

    if cur_color == 0:
        return 0

    directions = [(0,1),(1,0),(1,1),(1,-1)]
    

    for dr,dc in directions:
        count = 1

        for sign in (1,-1):
            for i in range(1,5):
                next_row = row + dr * i * sign
                next_col = col + dc * i * sign

                if 0<= next_row < board.shape[0] and 0<=next_col<board.shape[1]:
                    if board[next_row][next_col] == cur_color:
                        count += 1

                    else:
                        break

                else:
                    break

        if count >= 5:
            return cur_color

    return 0         
            

               










   

    

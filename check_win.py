import numpy as np

# 승리판별 함수
# 나중에 리펙토링을 위해 분리
def check_win(board,row,col):
    cur_color = board[row][col]

    if cur_color == 0:
        return 0
    # 4방향 탐색
    directions = [(0,1),(1,0),(1,1),(1,-1)]
    

    for dr,dc in directions:
        count = 1

        # 정방향 및 역방향 탐색
        for sign in (1,-1):
            for i in range(1,5):
                next_row = row + dr * i * sign
                next_col = col + dc * i * sign

                # 범위 조건
                if 0<= next_row < board.shape[0] and 0<=next_col<board.shape[1]:
                    if board[next_row][next_col] == cur_color:
                        count += 1

                    else:
                        break

                else:
                    break
        # 장목 허용
        if count >= 5:
            return cur_color

    return 0         
            

               










   

    

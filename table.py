import pygame 
import check_win
import numpy as np


pygame.init()
clock= pygame.time.Clock()
BLACK = (0,0,0)
WHITE = (255,255,255)
player = {1:BLACK,2:WHITE}


# 바둑판 그리기
def draw_board(screen,width,height):

    
    for i in range(width//20,width-1,width//20):
        pygame.draw.line(screen, BLACK, [width//20, i], [width-width//20,i], 2)
    for i in range(height//20,height-1,height//20):
        pygame.draw.line(screen, BLACK, [i, height//20], [i,height-height//20], 2)
    for i in range((width//20)*4-3,width-1,(width//20)*6):
        for j in range(int(height/20)*4-3,height-1,(height//20)*6):
            pygame.draw.rect(screen,BLACK,[i, j, 8, 8],4)

    




# 마우스 좌표를 행렬기준 좌표로 변환
def mouse_to_board(x,y):
    col = round(x / 30) - 1
    row = round(y / 30) - 1

    return row,col


# 행렬에 색 칠하기
def place_stone(board,row,col,color):
    if board[row,col]:
        return False
    board[row,col] = color

    return True

# 스크린에 돌 그리기
def draw_stones(screen, board):
   
    
    for row in range(board.shape[0]):
        for col in range(board.shape[1]):

            if board[row][col] == 0:
                continue
    
            x = (col + 1)*30
            y = (row + 1)*30
            pygame.draw.circle(screen,player[board[row,col]],(x,y),13)
            


def main():
    Background = (242,176,109)
    font = pygame.font.SysFont("나눔스퀘어라운드",20)
    width = 600
    height = 600
    size = [width,height]
    screen = pygame.display.set_mode(size)
    
    
    board = np.zeros((19,19))
    turn = 1
    winner = 0

    Done = False
    

    while not Done:
        

        clock.tick(10)
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                Done = True
            # 마우스 입력
            if event.type == pygame.MOUSEBUTTONDOWN:
                # 승리자가 나오면 클릭을 정지시킨다.
                if winner == 0:
                    if event.button == 1:
                        row,col = mouse_to_board(*event.pos) 
                        if 0<= row < board.shape[0] and 0<=col<board.shape[1]:
                            if place_stone(board,row,col,turn):
                                winner = check_win.check_win(board,row,col)
                                if winner == 0:
                                    turn = turn%2 + 1
                

            # 키보드 R을 누르면 재시작.
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    board = np.zeros((19, 19), dtype=int)
                    turn = 1
                    winner = 0

        # 스크린 칠하기
        screen.fill(Background)
        draw_board(screen,width,height)
        draw_stones(screen,board)

        #승리자 판별
        if winner != 0:
            if winner == 1:
                text = "BLACK WIN"
            else:
                text = "WHITE WIN"
        else:
            if turn == 1:
                text = "BLACK TURN"
            else:
                text = "WHITE TURN"
        text_surface = font.render(text,True,player[turn])
        text_rect = text_surface.get_rect(center=(width//2,15))
        screen.blit(text_surface,text_rect)
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
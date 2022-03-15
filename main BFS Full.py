# %%
from ricochet import Ricochet
from visualizer import Visualizer
from constants import *
from board_layouts.board_1 import goal_list
import pygame
from BFS_solver_full import Solver
import time

pygame.init()

colorMap = {'R': 'red', 'Y': 'yellow', 'G': 'green', 'B': 'blue'}


font = pygame.font.Font('freesansbold.ttf', 16)

textX = 820
textY = 50


FPS = 30

WIN = pygame.display.set_mode((WIDER_WIDTH, HEIGHT))
pygame.display.set_caption('Ricochet Robots!')


def show_amount_of_moves(win, x, y, MOVES, time):
    amount_of_moves = font.render("Moves: " + str(MOVES), True, BLACK)
    time_in_s = font.render("Seconds: " + str(time/1000), True, BLACK)
    win.blit(amount_of_moves, (x, y))
    win.blit(time_in_s, (x, y+50))


def main():
    cnt = 0
    Robot_moves = 0
    Old_key = None
    run = True
    clock = pygame.time.Clock()

    passed_time = 0

    game = Ricochet()

    # game.goal = {'color': 'B', 'num': 2, 'row': 5, 'col': 14}
    # game.blue["row"] = 2
    # game.blue["col"] = 11

    # game.red["row"] = 6
    # game.red["col"] = 5n

    # game.yellow["row"] = 11
    # game.yellow["col"] = 10

    # game.green["row"] = 15
    # game.green["col"] = 13
    
    visu = Visualizer(game)
    visu.draw_board(WIN)

    pygame.display.update()

    BFS = None
    BFS = Solver(game)
    print("Goal: ", BFS.goal)
    print("Goal path: ", BFS.path)
    if BFS.path is None:
        print('No solution found')
        
    


    while run:
        clock.tick(FPS)

        passed_time = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()

        ######## AI ###########
        if BFS.path is not None:
            move = BFS.path[cnt]
            move

            color = move[0]
            ag = getattr(game, color)
            visu.selected = ag

        ######## Draw the selected robot ##########
        if visu.selected is not None:
            pygame.draw.circle(WIN, BLACK, ((SQUARE_SIZE//2)+SQUARE_SIZE *
                               visu.selected['col'], (SQUARE_SIZE//2)+SQUARE_SIZE*visu.selected['row']), radius-10)

            # show path

            if keys_pressed[pygame.K_n]:
                time.sleep(0.5)
                game.move(ag, move[1])
                cnt += 1

        else:
            break

        visu.draw_board(WIN)

        pygame.display.update()

        if game.goal_check():
            print('!!!GOAL REACHED!!!')
            time.sleep(3)
            break
    pygame.quit()


main()

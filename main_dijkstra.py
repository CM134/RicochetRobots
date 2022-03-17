# %%

import random

random.seed(123)

from ricochet import Ricochet
from visualizer import Visualizer
from constants import *
from board_layouts.board_1 import goal_list
import pygame
from Dijstar import Dijkstra
import time


pygame.init()

colorMap = {'R': 'red', 'Y': 'yellow', 'G': 'green', 'B': 'blue'}


font = pygame.font.Font('freesansbold.ttf', 16)

textX = 820
textY = 50


FPS = 30

WIN = pygame.display.set_mode((WIDER_WIDTH, HEIGHT))
pygame.display.set_caption('Ricochet Robots!')


def show_text(win, x, y, solver, time, comp_time):
    if solver is not None:
        amount_of_moves = font.render("AI Path Length: " + str(len(solver.path)), True, BLACK)
        instruct = font.render('move by pressing N',True,BLACK)
        win.blit(instruct, (x, y+150))
    else:
        amount_of_moves = font.render("AI Path Length: " + '...', True, BLACK)
    time_in_s = font.render("Seconds: " + str(time/1000), True, BLACK)
    time_sol = font.render("Path found after: " + str(comp_time), True, BLACK)
    win.blit(amount_of_moves, (x, y))
    win.blit(time_in_s, (x, y+50))
    win.blit(time_sol, (x, y+100))


def main():
    cnt = 0
    Robot_moves = 0
    Old_key = None
    run = True
    clock = pygame.time.Clock()

    passed_time = 0

    game = Ricochet()

    game.goal = {'color': 'B', 'num': 2, 'row': 3, 'col': 5}
    game.blue["row"] = 2
    game.blue["col"] = 11

    game.red["row"] = 6
    game.red["col"] = 2

    game.yellow["row"] = 1
    game.yellow["col"] = 4

    game.green["row"] = 13
    game.green["col"] = 13
    # #---------------------------------
    game.goal = {'color': 'R', 'num': 3, 'row': 12, 'col': 14}

    game.blue["row"] = 4
    game.blue["col"] = 15

    game.red["row"] = 0
    game.red["col"] = 14
    # ------------------

    visu = Visualizer(game)
    visu.draw_board(WIN)
    
    dijkstra = None
    show_text(WIN,820,50,dijkstra,passed_time,0)

    pygame.display.update()

    print("Goal: ", game.goal)

    start_time = time.time()

  
    dijkstra = Dijkstra(game)
    print("Goal: ", dijkstra.goal)
    print("Goal path: ", dijkstra.path)
    if dijkstra.path is None:
        print('No solution found')
        
    stop_time = time.time()
    comp_time = stop_time - start_time
    comp_time = round(comp_time,1)

    while run:
        clock.tick(FPS)
        visu.draw_board(WIN)


        passed_time = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()

        ######## AI ###########
        if dijkstra.path is not None:
            move = dijkstra.path[cnt]

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

        show_text(WIN,820,50,dijkstra,passed_time,comp_time)
        pygame.display.update()

        if game.goal_check():
            print('!!!GOAL REACHED!!!')
            time.sleep(3)
            break
    pygame.quit()


main()

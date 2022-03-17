# %%
import random

random.seed(15)

from tracemalloc import start
from ricochet import Ricochet
from visualizer import Visualizer
from constants import *
from board_layouts.board_1 import goal_list
import pygame
from a_star import AStar
from BFS_solver import Solver as BFS_S
from BFS_solver_full import Solver as BFS
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


def show_text(win, x, y, solver, time, comp_time,selected_solver):
    if solver is not None:
        amount_of_moves = font.render("AI Path Length: " + str(len(solver.path)), True, BLACK)
        instruct = font.render('move by pressing N',True,BLACK)
        win.blit(instruct, (x, y+150))
    else:
        amount_of_moves = font.render("AI Path Length: " + '...', True, BLACK)
    time_in_s = font.render("Seconds: " + str(time/1000), True, BLACK)
    time_sol = font.render("Path found after: " + str(comp_time), True, BLACK)
    sol = font.render('Selected solver: ' + selected_solver,True,BLACK)
    win.blit(sol, (x, y+250))
    win.blit(amount_of_moves, (x, y))
    win.blit(time_in_s, (x, y+50))
    win.blit(time_sol, (x, y+100))


    
        


def main():
    cnt = 0
    run = True
    clock = pygame.time.Clock()

    passed_time = 0

    game = Ricochet()

    visu = Visualizer(game)
    visu.draw_board(WIN)

    solver = None
    # Decide for agent prompt
    while solver is None and run:
        clock.tick(FPS)
        visu.draw_board(WIN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()
        # draw rect
        
        # disp = pygame.Rect(HEIGHT//5,,3*HEIGHT//5,3*WIDER_WIDTH//5)
        pygame.draw.rect(WIN,(173,216,230),(WIDER_WIDTH//5,HEIGHT//5, 3*WIDER_WIDTH//5,3*HEIGHT//5) )
        # display text
        text1 = 'Choose your agent:'
        text2 = 'For BFS single agent press S (might not find a solution)'
        text3 = 'For BFS with all agents press B'
        text4 = 'For A* press A'
        text5 = 'For Greedy-Search Press G'
        instr1 = font.render(text1, True, BLACK)
        instr2 = font.render(text2, True, BLACK)
        instr3 = font.render(text3, True, BLACK)
        instr4 = font.render(text4, True, BLACK)
        instr5 = font.render(text5, True, BLACK)
        WIN.blit(instr1, (WIDER_WIDTH//4,HEIGHT//4))
        WIN.blit(instr2, (WIDER_WIDTH//4+100,HEIGHT//4+50))
        WIN.blit(instr3, (WIDER_WIDTH//4+100,HEIGHT//4+100))
        WIN.blit(instr4, (WIDER_WIDTH//4+100,HEIGHT//4+150))
        WIN.blit(instr5, (WIDER_WIDTH//4+100,HEIGHT//4+200))

        pygame.display.update()
        # get keyboard and set
        if keys_pressed[pygame.K_s]:
            solver = BFS_S(game)
            selected_solver = 'BFS single'
        if keys_pressed[pygame.K_b]:
            solver = BFS(game)
            selected_solver = 'BFS full'
        if keys_pressed[pygame.K_a]:
            solver = AStar(game)
            selected_solver = 'A*'
        if keys_pressed[pygame.K_g]:
            solver = Dijkstra(game)
            selected_solver = 'Greedy'

    visu.draw_board(WIN)
    show_text(WIN,820,50,solver,passed_time,0,selected_solver)

    pygame.display.update()

    print("Goal: ", game.goal)

    start_time = time.time()
    
    solver = AStar(game)
    print("Goal: ", solver.goal)
    print("Goal path: ", solver.path)
    if solver.path is None:
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
        if solver.path is not None:
            move = solver.path[cnt]

            color = move[0]
            ag = getattr(game, color)
            visu.selected = ag
    
        # show path

        if keys_pressed[pygame.K_n]:
            time.sleep(0.5)
            game.move(ag, move[1])
            cnt += 1
        
        visu.draw_board(WIN)

         ######## Draw the selected robot ##########
        if visu.selected is not None:
            pygame.draw.circle(WIN, BLACK, ((SQUARE_SIZE//2)+SQUARE_SIZE *
                               visu.selected['col'], (SQUARE_SIZE//2)+SQUARE_SIZE*visu.selected['row']), radius-10)

        show_text(WIN,820,50,solver,passed_time,comp_time,selected_solver)

        pygame.display.update()

        if game.goal_check():
            print('!!!GOAL REACHED!!!')
            print('New goal is set in 3 sec')
            time.sleep(3)
            cnt = 0
            if len(game.goals_remain) != 0:
                game.setGoal()
                print("Goal: ", game.goal)
                visu.draw_board(WIN)

                # Re init AI game:
                passed_time = 0
                solver = None
                show_text(WIN,820,50,solver,passed_time,0,selected_solver)
                pygame.display.update()
                

                start_time = time.time()
                solver = AStar(game)
                print("Goal path: ", solver.path)
                if solver.path is None:
                    print('No solution found')
                stop_time = time.time()
                comp_time = stop_time - start_time
                comp_time = round(comp_time,1)
                
            else:
                print('no more goals, game over')
                break

        
    pygame.quit()


main()

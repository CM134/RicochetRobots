# %%
from ricochet import Ricochet
from visualizer import Visualizer
from constants import *
from board_layouts.board_1 import goal_list
import pygame
from BFS_solver import Solver
import time

pygame.init()


# b1 = Ricochet(10)
# print(b1.board)
# print(b1.yellow)
# print('\n')
# b1.yellow["row"] = 0
# b1.yellow["col"] = 1
# b1.board[0, :] = "S"
# print(b1.availableMoves(b1.yellow))
# print("")
# b1.move(b1.yellow,'UP')
# print(b1.board)


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
    visu = Visualizer(game)

    BFS = None

    try:
        BFS = Solver(game)
    except:
        print('No solution found')

    while run:
        clock.tick(FPS)

        passed_time = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()

        ######## AI ###########
        if BFS is not None:
            color = BFS.color
            ag = getattr(game, color)

            # show path

            if keys_pressed[pygame.K_n]:
                time.sleep(0.5)
                game.move(ag, BFS.path[cnt])
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

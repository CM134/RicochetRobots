# %%
from ricochet import Ricochet
from visualizer import Visualizer
from constants import *
from board_layouts.board_1 import goal_list
import pygame

pygame.init()



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

    Robot_moves = 0
    Old_key = None
    run = True
    clock = pygame.time.Clock()

    passed_time = 0

    game = Ricochet()
    visu = Visualizer(game)

    while run:
        clock.tick(FPS)

        passed_time = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()


######## Choose color ###########

        if keys_pressed[pygame.K_r]:
            visu.selected = game.red
            Robot_moves = 0
        if keys_pressed[pygame.K_b]:
            visu.selected = game.blue
            Robot_moves = 0
        if keys_pressed[pygame.K_y]:
            visu.selected = game.yellow
            Robot_moves = 0
        if keys_pressed[pygame.K_g]:
            visu.selected = game.green
            Robot_moves = 0


######## Move robot ###########

        if keys_pressed[pygame.K_LEFT]:
            if Old_key != 'LEFT':
                game.move(visu.selected, 'LEFT')
                Robot_moves += 1
            Old_key = 'LEFT'
        if keys_pressed[pygame.K_RIGHT]:
            if Old_key != 'RIGHT':
                game.move(visu.selected, 'RIGHT')
                Robot_moves += 1
            Old_key = 'RIGHT'
        if keys_pressed[pygame.K_UP]:
            if Old_key != 'UP':
                game.move(visu.selected, 'UP')
                Robot_moves += 1
            Old_key = 'UP'

        if keys_pressed[pygame.K_DOWN]:
            if Old_key != 'DOWN':
                game.move(visu.selected, 'DOWN')
                Robot_moves += 1
            Old_key = 'DOWN'

        # TODO:
        # goal check -> assign new goal game.setGoal()

        # Celebrate we made it to the goal

        # print(goal_list[0])#['color'])

        visu.draw_board(WIN)

######## Draw the selected robot ##########
        if visu.selected is not None:  # and visu.selected['name'] == 'Y':
            pygame.draw.circle(WIN, BLACK, ((SQUARE_SIZE//2)+SQUARE_SIZE *
                               visu.selected['col'], (SQUARE_SIZE//2)+SQUARE_SIZE*visu.selected['row']), radius-10)

            Av_moves = game.availableMoves(visu.selected)

            # draw available moves!
            for AvMove in Av_moves:
                # print(AvMove)
                pygame.draw.circle(WIN, BLACK, ((SQUARE_SIZE//2)+SQUARE_SIZE *
                                   Av_moves[AvMove][1], (SQUARE_SIZE//2)+SQUARE_SIZE*Av_moves[AvMove][0]), radius-10)

            # Celebrate we made it to the goal

            for GOLAZO_name in visu.selected:
                for GOLAZO_color in goal_list[0]:
                    pass
            # if visu.selected


######## Count amount of moves #######
        show_amount_of_moves(WIN, textX, textY, Robot_moves, passed_time)
        pygame.display.update()
    pygame.quit()


main()

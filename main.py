# %%
from ricochet import Ricochet
from visualizer import Visualizer
from constants import WIDTH, HEIGHT, SQUARE_SIZE, RED, BLUE
import pygame




#b1 = Ricochet(10)
#print(b1.board)
#print(b1.yellow)
#print('\n')
# b1.yellow["row"] = 0
# b1.yellow["col"] = 1
# b1.board[0, :] = "S"
#print(b1.availableMoves(b1.yellow))
#print("")
#b1.move(b1.yellow,'UP')
#print(b1.board)


FPS = 30

WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Ricochet Robots!')

def main():
	run = True
	clock = pygame.time.Clock()
	#b1 = Ricochet(16) 
	#print(b1)
	game = Ricochet()
	visu = Visualizer(game)
	#b1.draw_squares(WIN)
	
	while run:
		clock.tick(FPS)
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

		keys_pressed = pygame.key.get_pressed()

		if keys_pressed[pygame.K_r]:
			visu.selected = game.red
		if keys_pressed[pygame.K_b]:
			visu.selected = game.blue
		if keys_pressed[pygame.K_y]:
			visu.selected = game.yellow
		if keys_pressed[pygame.K_g]:
			visu.selected = game.green

		if keys_pressed[pygame.K_LEFT]:
			game.move(visu.selected, 'LEFT')
		if keys_pressed[pygame.K_RIGHT]:
			game.move(visu.selected, 'RIGHT')
		if keys_pressed[pygame.K_UP]:
			game.move(visu.selected, 'UP')
		if keys_pressed[pygame.K_DOWN]:
			game.move(visu.selected, 'DOWN')


		#TODO: visu which brick (blick)
		# show available moves
		# show how many moves
		# goal check -> assign new goal game.setGoal()
		# timer
		# show goal in the middel
		# draw all goals
		

		visu.draw_board(WIN)
		pygame.display.update()
	pygame.quit()

main()
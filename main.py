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
	b1 = Visualizer(Ricochet(16).board)
	#b1.draw_squares(WIN)
	
	while run:
		clock.tick(FPS)
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

		b1.draw_board(WIN)
		pygame.display.update()
	pygame.quit()

main()
import pygame
from pygame.locals import *

pygame.init()
window = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Hola mundo')

while True:
    for event in pygame.event.get():
    	if event.type == QUIT:
    		pygame.quit()
    		sys.exit()
    pygame.display.update()
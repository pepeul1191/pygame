import pygame
from pygame.locals import *


color = (0, 0, 255)
color2 = pygame.Color(0, 0, 255)

pygame.init()
window = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Hola mundo')

while True:
    window.fill(color)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
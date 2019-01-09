import pygame
from pygame.locals import *


color = (255, 255, 0) # rgb
color2 = pygame.Color(0, 0, 255)

pygame.init()
window = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Hola mundo')

window.fill(color2)
pygame.draw.line(window, color, (60, 80), (160, 100), 8)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
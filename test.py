import pygame
from pygame.locals import *

pygame.init()

pantalla = pygame.display.set_mode((620, 540), 0, 32)
pos = [10, 10]
imagen = pygame.image.load("img/doge.png").convert()

reloj = pygame.time.Clock()
pantalla.blit(imagen, pos)
while True:
    for eventos in pygame.event.get():
        if eventos.type == pygame.QUIT:
            exit()
        elif eventos.type == pygame.MOUSEBUTTONDOWN:
            pantalla.fill((0, 0, 0))
            pantalla.blit(imagen, pos)
    pos = pygame.mouse.get_pos()
    reloj.tick(25)
    pygame.display.update()

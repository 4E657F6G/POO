import pygame
from pygame.locals import *

pygame.init()

pantalla = pygame.display.set_mode((620, 540), 0, 32)
imagen = pygame.image.load("img/ficha.jpg").convert()

pos = [10, 10]

reloj = pygame.time.Clock()
while True:
    for eventos in pygame.event.get():
        if eventos.type == pygame.QUIT:
            exit()
<<<<<<< HEAD
        elif eventos.type == pygame.MOUSEBUTTONDOWN:
=======
        elif eventos.type == pygame.MOUSEBUTTONUP:
>>>>>>> 831d8fb7e25d842171603145ed569a8784ee33f7
            reloj.tick(10)
            pantalla.fill((0, 0, 0))
            pantalla.blit(imagen, pos)
            pos = pygame.mouse.get_pos()

    pygame.display.update()

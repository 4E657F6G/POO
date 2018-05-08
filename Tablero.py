import pygame

class Tablero():

    def HacerTablero(self):

        NEGRO = (0, 0, 0)
        BLANCO = (255, 255, 255)

        pygame.init()

        dimensiones = [600, 600]
        pantalla = pygame.display.set_mode(dimensiones)
        pygame.display.set_caption("TABLERO")

        juego_terminado = False

        reloj = pygame.time.Clock()
        ancho = int(dimensiones[0] / 8)
        alto = int(dimensiones[1] / 8)
        rojo = (255, 0, 0)

        '''carga de imagen'''
        imagen = pygame.image.load("img/ficha.jpg").convert()
        posimg = [38, 100]

        def tablero():
            pantalla.fill(BLANCO)
            color = 0
            for i in range(0, dimensiones[0], ancho):
                for j in range(0, dimensiones[1], alto):
                    if color % 2 == 0:
                        pygame.draw.rect(pantalla, NEGRO, [i, j, ancho, alto], 0)
                    else:
                        pygame.draw.rect(pantalla, BLANCO, [i, j, ancho, alto], 0)
                    color += 1
                color += 1

        def fichitas():
            pos = [38, 38]
            for i in range(4):
                pygame.draw.circle(pantalla, rojo, pos, 27, 0)
                pos[0] = pos[0] + 150

        while juego_terminado is False:
            tablero()
            pantalla.blit(imagen, posimg)
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    juego_terminado = True
                elif evento.type == pygame.MOUSEBUTTONDOWN:
                    reloj.tick(10)
                    pantalla.blit(imagen, posimg)
                    posimg = pygame.mouse.get_pos()
            fichitas()
            #reloj.tick(10)
            pygame.display.flip()
        pygame.quit()


if __name__=="__main__":
    tablero = Tablero()
    tablero.HacerTablero()


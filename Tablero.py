import pygame
# import Negra
# import Blanca
import Checker


class Tablero():
    NEGRO = (0, 0, 0)
    BLANCO = (255, 255, 255)
    AZUL = (20, 80, 240)
    FONDO = (24, 25, 30)
    SELECCIONA = (220, 200, 0)
    DIMENCIONES = (600, 600)
    LETRAS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    screen = pygame.display.set_mode(DIMENCIONES)
    imgfn = None

    def jugar(self):
        pygame.init()
        pygame.display.set_caption("__Tablero__")
        game_over = False
        clock = pygame.time.Clock()
        tamanio_fuente = 30
        seleccion = ['Z', -1]
        img = pygame.image.load("img/grumpy.png").convert_alpha()

        def dibujartablero(screen, dimension, p_inicio, seleccion):
            color = 0
            for i in range(8):
                for j in range(8):
                    x = i * dimension + p_inicio[0]
                    y = j * dimension + p_inicio[1]
                    if color % 2 == 0:
                        pygame.draw.rect(screen, self.NEGRO, [x, y, dimension, dimension], 0)
                    else:
                        pygame.draw.rect(screen, self.BLANCO, [x, y, dimension, dimension], 0)
                    if seleccion[0] == self.LETRAS[i] and j == seleccion[1] - 1:
                        pygame.draw.rect(screen, self.SELECCIONA, [x, y, dimension, dimension], 0)
                    color += 1
                color += 1

        def ajustarmedidas(tamanio_fuente):
            if self.DIMENCIONES[1] < self.DIMENCIONES[0]:
                ancho = int((self.DIMENCIONES[1] - (tamanio_fuente * 2)) / 8)
                inicio = ((self.DIMENCIONES[0] - self.DIMENCIONES[1]) / 2) + tamanio_fuente, tamanio_fuente
            else:
                ancho = int((self.DIMENCIONES[0] - (tamanio_fuente * 2)) / 8)
                inicio = tamanio_fuente, ((self.DIMENCIONES[1] - self.DIMENCIONES[0]) / 2) + tamanio_fuente
            return [inicio, ancho]

        puntoInicio, dimension = ajustarmedidas(tamanio_fuente)

        def obtenerposicion(mouse, dimension, p_inicio, actual):
            xr, yr = mouse[0], mouse[1]
            for i in range(8):
                for j in range(8):
                    x = i * dimension + p_inicio[0]
                    y = j * dimension + p_inicio[1]
                    if (xr >= x) and (xr <= x + dimension) and (yr >= y) and (yr <= y + dimension):
                        actual = [self.LETRAS[i], j + 1]
            return actual

        def cargarfichas():
            for lista in Checker.posiciones:
                print(lista)

            '''fichanegra = Negra.Negra("img/doge.png", pos)
            fichanegra.cargarimg()
            fichanegra.blitimg()
            self.screen.blit(img, pos2)
            self.screen.blit(img, [100, 502])
            self.screen.blit(img, [234, 502])
            self.screen.blit(img, [368, 502])
            self.screen.blit(img, [502, 502])'''

        pos2 = [100, 100]
        while game_over is False:
            '''botones = pygame.mouse.get_pressed()
            if botones[0]:
                pos = pygame.mouse.get_pos()
                seleccion = obtenerposicion(pos, dimension, puntoInicio, seleccion)'''
            self.screen.fill(self.FONDO)
            dibujartablero(self.screen, dimension, puntoInicio, seleccion)

            cargarfichas()
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    game_over = True
                elif evento.type == pygame.MOUSEBUTTONDOWN:
                    botones = pygame.mouse.get_pressed()
                    if botones[0]:
                        pos = pygame.mouse.get_pos()
                        seleccion = obtenerposicion(pos, dimension, puntoInicio, seleccion)
                    if seleccion == ['B', 2]:
                        self.screen.blit(img, pos2)
                        print("se movió a: ", pos2)
                    pos2 = pygame.mouse.get_pos()
            clock.tick(60)
            pygame.display.flip()
        pygame.quit()


if __name__ == "__main__":
    tablero = Tablero()
    tablero.jugar()

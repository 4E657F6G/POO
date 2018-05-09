import abc
import pygame
import Tablero


class Ficha(metaclass=abc.ABCMeta):
    def __init__(self, img, pos): # tipoficha
        # self.color = color
        # self.tipoficha = tipoficha
        self.img = img
        self.pos = pos

    ''''@abc.abstractmethod
    def settipoficha(self, tipo):
        self.tipoficha = tipo

    def gettipoficha(self):
        return self.tipoficha

    @abc.abstractmethod
    def setcolor(self, color):
        pass

    @abc.abstractmethod
    def comer(self, color):
        pass'''

    @abc.abstractmethod
    def cargarimg(self, imagen):
        Tablero.Tablero.imgfn = pygame.image.load(imagen).convert_alpha()
        #print("todo bien")

    @abc.abstractmethod
    def blitimg(self, posicion):
        Tablero.Tablero.screen.blit(Tablero.Tablero.imgfn, posicion)
        #print("todo bien")

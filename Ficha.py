import abc
import pygame
import Tablero


class Ficha(metaclass=abc.ABCMeta, Tablero.Tablero):
    def __init__(self, color, tipoficha, img):
        self.color = color
        self.tipoficha = tipoficha
        self.img = img

    @abc.abstractmethod
    def settipoficha(self, tipo):
        self.tipoficha = tipo

    def gettipoficha(self):
        return self.tipoficha

    @abc.abstractmethod
    def setcolor(self, color):
        pass

    @abc.abstractmethod
    def comer(self, color):
        pass

    @abc.abstractmethod
    def cargarimg(self, imagen):
        self.img = pygame.image.load(imagen).convert()

    @abc.abstractmethod
    def blitimg(self, imagen, posimg):
        Tablero.Tablero.pantalla.blit(imagen, posimg)
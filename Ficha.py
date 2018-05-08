import abc
import Checker


class Ficha(metaclass=abc.ABCMeta, Checker):
    def __init__(self, ficha, color, tipoficha):
        self.ficha = ficha
        self.color = color
        self.tipoficha = tipoficha

    @abc.abstractmethod
    def setcolor(self, color):
        pass

    @abc.abstractmethod
    def comer(self, color):
        pass

    def moverficha(self, ficha):
        pass
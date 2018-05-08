import Ficha


class Blanca(Ficha):
    def __init__(self, imagen, color, posimg):
        self.imagen = imagen
        self.color = color
        self.posimg = posimg

    def cargarimg(self, imagen):
        super().cargarimg(imagen)

    def blitimg(self, imagen, posimg):
        super().blitimg(imagen, posimg)
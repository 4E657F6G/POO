import Ficha


class Negra(Ficha.Ficha):
    def __init__(self, img, pos):
        self.img = img
        self.pos = pos

    def cargarimg(self):
        super().cargarimg(self.img)

    def blitimg(self):
        super().blitimg(self.pos)

import Ficha


class Negra(Ficha.Ficha):
    def __init__(self, img, pos):
        super(Negra, self).__init__(img, pos)

    def cargarimg(self):
        super().cargarimg(self.img)

    def blitimg(self):
        super().blitimg(self.img, self.pos)

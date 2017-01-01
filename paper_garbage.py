from garbage import Garbage


class PaperGarbage(Garbage):
    is_squeezed = False

    def squeeze(self):
        self.is_squeezed = True
        return self.is_squeezed

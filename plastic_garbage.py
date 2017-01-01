from garbage import Garbage


class PlasticGarbage(Garbage):
    is_clean = False

    def clean(self):
        self.is_clean = True
        return self.is_clean

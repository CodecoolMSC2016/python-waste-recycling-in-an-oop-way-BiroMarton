from garbage import Garbage
from paper_garbage import PaperGarbage
from plastic_garbage import PlasticGarbage
from dustbin_content_error import DustbinContentError


class Dustbin:

    def __init__(self, color,):
        self.color = color

        self.plastic_content = []
        self.paper_content = []
        self.house_waste_content = []

    def throw_out_garbage(self, garbage):

        if isinstance(garbage, PlasticGarbage) is True:
            if garbage.is_clean is True:
                self.plastic_content.append(garbage.name)
                return
            else:
                raise DustbinContentError
        elif isinstance(garbage, PaperGarbage) is True:
            if garbage.is_squeezed is True:
                self.paper_content.append(garbage.name)
                return
            else:
                raise DustbinContentError
        elif isinstance(garbage, Garbage) is True:
            self.house_waste_content.append(Garbage(garbage).name)
        else:
            raise DustbinContentError

    def empty_contents(self):
        del self.paper_content[:]
        del self.plastic_content[:]
        del self.house_waste_content[:]

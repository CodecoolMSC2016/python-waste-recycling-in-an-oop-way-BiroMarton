from garbage import Garbage
from paper_garbage import PaperGarbage
from plastic_garbage import PlasticGarbage
from dustbin_content_error import DustbinContentError


class Dustbin:
    def __init__(self, color,):
        self.color = color

    plastic_content = []
    paper_content = []
    house_waste_content = []

    def throw_out_garbage(self, garbage):

        if isinstance(garbage, PlasticGarbage) == True:
            if garbage.is_clean == True:
                self.plastic_content.append(garbage.name)
                #print(self.plastic_content)
                #print(self.paper_content)
                #print(self.house_waste_content)
                return
            else:
                raise DustbinContentError
        elif isinstance(garbage, PaperGarbage) == True:
            if garbage.is_squeezed == True:
                self.paper_content.append(garbage.name)
                #print(self.plastic_content)
                #print(self.paper_content)
                #print(self.house_waste_content)
                return
            else:
                raise DustbinContentError
        elif isinstance(garbage, Garbage) == True:
            self.house_waste_content.append(Garbage(garbage).name)
        else:
            raise DustbinContentError

    def empty_contents(self):
        del self.paper_content[:]
        del self.plastic_content[:]
        del self.house_waste_content[:]

"""paper_garbage = PaperGarbage("Paper garbage", True)
dustbin = Dustbin("red")
dustbin.throw_out_garbage(paper_garbage)

dustbin.empty_contents()
print("")

plastic_garbage = PlasticGarbage("Plastic garbage", True)
dustbin = Dustbin("red")
dustbin.throw_out_garbage(plastic_garbage)"""
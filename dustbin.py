from garbage import Garbage
from paper_garbage import PaperGarbage
from plastic_garbage import PlasticGarbage
from dustbin_content_error import DustbinContentError


class Dustbin:
    def __init__(self, color,):
        self.color = color

    paper_content = []
    plastic_content = []
    house_waste_content = []

    def throw_out_garbage(self, garbage):
        pass

    def empty_contents(self):
        self.paper_content = []
        self.plastic_content = []
        self.house_waste_content = []
    
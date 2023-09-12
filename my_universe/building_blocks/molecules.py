from ..universe import StateOfMatter
from elements import Element

class Molecule:
    """Group of Elements"""
    def __init__(self, elements: tuple):
        self.elements = elements

class GroupOfMolecules(Molecule):
    """Group of Molecules and its State of Matter"""
    state: StateOfMatter = 0
    weight: int | float = 0

    def set_weight(self, weight: int | float):
        self.weight = weight
    
    def get_weight(self):
        return self.weight